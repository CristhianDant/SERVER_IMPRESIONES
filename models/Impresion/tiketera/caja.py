from escpos.printer import Network


class Caja_Tiketera:

    @staticmethod
    def imprimir_guiones(kitchen):
        # Imprime un guion bajo "_" 30 veces en la impresora
        kitchen.text("_" * 30 + "\n")

    
    def impresion(ip: str, data: dict) -> str:
        try:
            data= data['movimiento']
            
            kitchen = Network(f'{ip}')

            kitchen.text('CAJA\n')

            # Extraemos los datos del diccionario
            tienda = str(data['TIENDA']).upper()
            tipomov = str(data['TIPOMOV']).upper()
            nro_comprobante = str(data['NROCOMPROBANTE'])
            fecha_reg = str(data['FECHA_REG'])
            descripcion_concepto = str(data['DESCRIPCION_CONCEPTO'])
            mtotal_selec = str(data['MTOTAL_SELEC'])
            monto_cheque = str(data['MONTO_CHEQUE'])
            monto_deposito = str(data['MONTO_DEPOSITO'])
            monto_efectivo = str(data['MONTO_EFECTIVO'])
            monto_transferencia = str(data['MONTO_TRANSFERENCIA'])
            detalle = str(data['DETALLE']) if data['DETALLE'] else 'No hay detalle'
            user = str(data['USUARIO'])
            entidad = str(data['NOM_ENTIDAD'])

            # Imprimir los datos
            kitchen.text(f'{tienda}\n')
            kitchen.text(f'{tipomov}\n')
            kitchen.text(f'N° COMPROBANTE: {nro_comprobante}\n')
            kitchen.text(f'F REGISTRO: {fecha_reg}\n')
            kitchen.text(f'CONCEPTO: {descripcion_concepto}\n')
            kitchen.text(f'IMPORTE: {mtotal_selec}\n')

            Caja_Tiketera.imprimir_guiones(kitchen)

            kitchen.text(f'CHEQUE: {monto_cheque}\n')
            kitchen.text(f'DEPÓSITO: {monto_deposito}\n')
            kitchen.text(f'EFECTIVO: {monto_efectivo}\n')
            kitchen.text(f'TRANSFERENCIA: {monto_transferencia}\n')

            Caja_Tiketera.imprimir_guiones(kitchen)


            kitchen.text(f'DETALLE:\n{detalle}')

        
            kitchen.text(' \n')
            kitchen.text('  _____________     ______________\n')
            kitchen.text(f'   {user}        {entidad}\n')
            kitchen.text(' \n')
            kitchen.cut()
            kitchen.close()

            return {
                'message': 'Impresion exitosa'
            }
        
        except Exception as e:
            # Manejo de excepciones en caso de error
            return f'Ocurrió un error: {str(e)}'

