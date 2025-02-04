from escpos.printer import Network

class Devolucion_Tiketera:

    def impresion(ip: str, data: dict) -> str:
        try:
            kitchen = Network(f"{ip}")
            encabezado = data['encabezado']
            detalle = data['detalles']

            kitchen.text(f"DOCUMENTO DE DEVOLUCION  {encabezado['DESCRIPCION_CLIENTE']['SEDE']}\n")
            kitchen.text(f"{encabezado['DESCRIPCION_CLIENTE']['DESCRIPCION_MERCADO']}   {encabezado['NROSERIE']}-{encabezado['ID_DEV_RET']}\n")
            kitchen.text(f"FECHA :{encabezado['FECHA_EMISION']}\n")
            kitchen.text(f"USUARIO :{encabezado['DESCRIPCION_VENDEDOR']}\n")
            kitchen.text(f"________________________________________\n")
            kitchen.text(f"CANTIDAD======DEVOLUCION======RETORNO\n")

            for item in detalle:
                descripcion_articulo = item['DESCRIPCION_ARTICULO']['DESCRIPCION_ARTICULO']
                cantidad_devolucion = str(item['CANTIDAD_DEVOLICION'])
                cantidad_retorno = str(item['CANTIDAD_RETORNO'])

                kitchen.text(f"{descripcion_articulo}\n")

                detalle_linea = f"{cantidad_devolucion.ljust(10)}{cantidad_retorno.ljust(10)}"
                kitchen.text(f"{detalle_linea}\n")
                kitchen.text(f"________________________________________\n")

            kitchen.text(f"USUARIO :{encabezado['USUARIO']}\n")

        except Exception as e:
            print(e)
            return False
        finally:
            kitchen.cut()
            kitchen.close()
            return {
                'message': 'Impresion exitosa'
            }

