from escpos.printer import Network

class GuiaInternaAmp():
    '''
    Clase para la impresión de guias internas de AMP
    '''

    @staticmethod
    def imprimir_guiones(kitchen):
        # Imprime un guion bajo "_" 30 veces en la impresora
        kitchen.text("_" * 30 + "\n")

    # @staticmethod
    # def process_words(kitchen, words):
    #     result = ""
    #     for word in words:
    #         codigo_formateado = word[:14].ljust(14)
    #         cantidad_formateada = ":".ljust(8)
    #         result += codigo_formateado + cantidad_formateada + '.' * 12 + "\n"
    #     kitchen.text(result)


    @staticmethod
    def impresion(ip :str , data:dict) -> bool:
        encabezado = data['encabezado']
        detalle = data['detalle']

        try:
            kitchen = Network(f'{ip}')

            kitchen.text("GUIA INTERNA-AMP\n")
            kitchen.text("MateriaPrima - Suministros\n")
            kitchen.text(" \n")

            GuiaInternaAmp.imprimir_guiones(kitchen)

            guia = str(encabezado['NROGUIA'])
            kitchen.text("N° GUIA: " + guia + "\n")

            NROSERIE = str(encabezado['NROSERIE'])
            NRODOC = str(encabezado['NRODOC'])
            kitchen.text("           " + NROSERIE + "-" + NRODOC + "\n")

            FECHA = str(encabezado['HORA_INGRESADO'])
            kitchen.text("FECHA: " + FECHA + "\n")

            PROVEDOR = str(encabezado['DESCRIPCION_PROVEEDOR'])
            kitchen.text("PROVEEDOR: " + PROVEDOR + "\n")

            TIPO_COMPRA = str(encabezado['TIPO_COMPRA'])
            kitchen.text("T.Ingreso: " + TIPO_COMPRA + "\n")

            GuiaInternaAmp.imprimir_guiones(kitchen)

            kitchen.text("INSUMO               CANTIDAD\n")

            GuiaInternaAmp.imprimir_guiones(kitchen)

            for det in detalle:
                art = det[('ARTICULO_V2')]['DESCRIPCION_ARTICULO']
                cant = str(det['CANTIDAD_P'])

                kitchen.text(f"{art}             {cant}\n")

            lista = ['Alamacen MP', 'Firma', 'Logistica', 'Firma']

            for resp in lista:
                kitchen.text(f"{resp}:\n")
                GuiaInternaAmp.imprimir_guiones(kitchen)
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














