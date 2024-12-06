from escpos.printer import Network 

class Pedidos_Tiketera:
    @staticmethod
    def formatear_texto(codigo: str, cantidad: str) -> str:
        codigo_formateado = codigo[:14].ljust(14)
        cantidad_formateada = str(cantidad).ljust(8)
        resultado = codigo_formateado + cantidad_formateada + '.' * 12
        return resultado

    @staticmethod
    def impresion(ip: str, data: dict) -> bool:
        encabezado = data['encabezado']
        detalle = data['detalle']

        try:
            kitchen = Network(f'{ip}')

            kitchen.text("PEDIDOS Y/O DESPACHOS\n")

            nro_pedido = str(encabezado['NROPEDIDO'])
            fecha_emision = str(encabezado['FECHAREGISTRO'])
            fecha_despacho = str(encabezado['FECHADESPACHO'])
            vendedor = str(encabezado['NOMBRES'])
            destino = str(encabezado['ZONA'])
            observacion = str(encabezado['OBSERVACIONES'])

            kitchen.text(f"N°           : {nro_pedido}\n")
            kitchen.text(f"FEC.EMISION  : {fecha_emision}\n")
            kitchen.text(f"FEC.DESPACHO : {fecha_despacho}\n")
            kitchen.text(f"VENDEDOR     : {vendedor}\n")
            kitchen.text(f"DESTINO      : {destino}\n")
            kitchen.text(f"OBSERVACION  : {observacion}\n")
            kitchen.text('PRODUCTO===CANTIDAD\n')
            kitchen.text(' \n')

            try:
                for det in detalle:
                    cod = str(det['ARTICULO_V2']['CODIGO'])
                    cantidad = str(det['CANTIDAD'])
                    text_det = Pedidos_Tiketera.formatear_texto(cod, cantidad=cantidad)
                    kitchen.text(f'{str(text_det)}\n')
            except Exception as e:
                print(e)
                kitchen.text('Error :\n')

            kitchen.text(' \n')
            kitchen.text('  _____________     ______________\n')
            kitchen.text('   V.B ALMACEN       V.B VENDEDOR\n')
            kitchen.text(' \n')
            kitchen.cut()
            kitchen.close()
            return {
                'message': 'Impresion exitosa'
            }
        except Exception as e:
            print(e)
            return False



    