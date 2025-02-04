from escpos.printer import Network

class Factura_Tiketera:

    def impresion(ip: str, data: dict) -> str:
        try:
            kitchen = Network(f'{ip}')
            encabezado = data['encabezado']
            detalle = data['detalle']

            kitchen.text(f"DOCUMENTO DE VENTA  {encabezado['TIENDA']}\n")
            kitchen.text(f"{encabezado['TIPODOCUMENTO']}   {encabezado['NROSERIE']}-{encabezado['NRODOCUMENTO']}\n")
            kitchen.text(f"FECHA :{encabezado['FECHAEMISION']}\n")
            kitchen.text(f"CLIENTE :{encabezado['DESCRIPCION_CLIENTE']}\n")
            kitchen.text(f"TIPO DE PAGO :{encabezado['CONDICION_PAGO']}\n")
            kitchen.text(f"USUARIO :{encabezado['DESCRIPCION_VENDEDOR']}\n")
            kitchen.text(f"________________________________________\n")
            kitchen.text(f"CANTIDAD======P.UNITARIO======TOTAL\n")

            for item in detalle:
                descripcion_articulo = item['DESCRIPCION_ARTICULO']
                cantidad = str(item['CANTIDAD'])
                punitario = str(item['PUNITARIO'])
                totalventa = str(item['TOTALVENTA'])

                kitchen.text(f"{descripcion_articulo}\n")

                detalle_linea = f"{cantidad.ljust(10)}{punitario.ljust(10)}{totalventa.ljust(10)}"
                kitchen.text(f"{detalle_linea}\n")
                kitchen.text(f"________________________________________\n")

            kitchen.text(f"SUBTOTAL :{encabezado['SUBTOTAL']}\n")
            kitchen.text(f"IGV :{encabezado['IGV']}\n")
            kitchen.text(f"TOTAL :{encabezado['TOTAL']}\n")

        except Exception as e:
            print(e)
            return False
        finally:
            kitchen.cut()
            kitchen.close()
            return {
                'message': 'Impresion exitosa'
            }
