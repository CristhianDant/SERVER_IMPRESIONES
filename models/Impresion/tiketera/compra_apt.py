from escpos.printer import Network

class Compra_apt():
    '''
    Clase para la impresión de guias internas de AMP
    '''

    @staticmethod
    def imprimir_guiones(kitchen):
        # Imprime un guion bajo "_" 30 veces en la impresora
        kitchen.text("_" * 30 + "\n")



    @staticmethod
    def impresion(ip :str , data:dict) -> bool:
        encabezado = data['encabezado']
        detalle = data['detalle']

        try:
            kitchen = Network(f'{ip}')

            kitchen.text("COMPRAS\n")
            kitchen.text("Productos Terminados\n")
            kitchen.text(" \n")

            Compra_apt.imprimir_guiones(kitchen)

            NROSERIE = str(encabezado['NROSERIE'])
            NRODOC = str(encabezado['NRODOC'])
            kitchen.text("N° de INGRESO" + NROSERIE + " " + NRODOC + "\n")

            FECHA = str(encabezado['HORA_INGRESADO'])
            kitchen.text("FECHA: " + FECHA + "\n")

            PROVEDOR = str(encabezado['DESCRIPCION_PROVEEDOR'])
            kitchen.text("PROVEEDOR: " + PROVEDOR + "\n")

            TIPO_COMPRA = str(encabezado['TIPODOC'])
            kitchen.text("FPAGO: " + TIPO_COMPRA + "\n")

            Compra_apt.imprimir_guiones(kitchen)

            kitchen.text("INSUMO               CANTIDAD\n")

            Compra_apt.imprimir_guiones(kitchen)

            for det in detalle:
                art = det[('ARTICULO_V2')]['DESCRIPCION_ARTICULO']
                cant = str(det['CANTIDAD_P'])

                kitchen.text(f"{art}             {cant}\n")

            lista = ['Alamacen MP', 'Firma', 'Logistica', 'Firma']

            for resp in lista:
                kitchen.text(f"{resp}:\n")
                Compra_apt.imprimir_guiones(kitchen)
                kitchen.text(" \n")


            kitchen.cut()
            kitchen.close()


            return {
                'message': 'Impresion exitosa'
            }

        except Exception as e:
            print(e)
            return {
                'message': str('Error en la impresion')
            }














