# {
#     "detalles": [
#         {
#             "CANTIDAD_DEVOLICION": 7,
#             "CANTIDAD_RETORNO": 5,
#             "CODARTICULO": "A0024",
#             "CODARTICULO_CAMBIO": "",
#             "DESCRIPCION_ARTICULO": {
#                 "CODIGO": "PANCO30TSB",
#                 "DESCRIPCION_ARTICULO": "PAN COLIZA x 30",
#                 "DESCRIPCION_MARCA": "TORRES",
#                 "DESCRIPCION_UNIDAD_MEDIDA": "BOLSA",
#                 "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#                 "UM": "BLS",
#                 "UM_PRESENTACION": null
#             },
#             "DESCRIPCION_ARTICULO_CAMBIO": {
#                 "CODIGO": null,
#                 "DESCRIPCION_ARTICULO": null,
#                 "DESCRIPCION_MARCA": null,
#                 "DESCRIPCION_UNIDAD_MEDIDA": null,
#                 "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#                 "UM": null,
#                 "UM_PRESENTACION": null
#             },
#             "FECHA_PRODUCCION": "2024-09-24",
#             "FECHA_VENCIMIENTO": "2024-09-24",
#             "ID_DEV_RET": 3,
#             "MOTIVO": "ninguno",
#             "OBSERVACION": "",
#             "TIPO_DEVOLUCION": "ninguno",
#             "UNIDAD": "BOLSA"
#         },
#         {
#             "CANTIDAD_DEVOLICION": 0,
#             "CANTIDAD_RETORNO": 7,
#             "CODARTICULO": "A0301",
#             "CODARTICULO_CAMBIO": "",
#             "DESCRIPCION_ARTICULO": {
#                 "CODIGO": "PANT12SMB",
#                 "DESCRIPCION_ARTICULO": "PANETON x 12 BOLSA BLANCA",
#                 "DESCRIPCION_MARCA": ".",
#                 "DESCRIPCION_UNIDAD_MEDIDA": "BOLSA",
#                 "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#                 "UM": "BLS",
#                 "UM_PRESENTACION": null
#             },
#             "DESCRIPCION_ARTICULO_CAMBIO": {
#                 "CODIGO": null,
#                 "DESCRIPCION_ARTICULO": null,
#                 "DESCRIPCION_MARCA": null,
#                 "DESCRIPCION_UNIDAD_MEDIDA": null,
#                 "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#                 "UM": null,
#                 "UM_PRESENTACION": null
#             },
#             "FECHA_PRODUCCION": "2024-09-24",
#             "FECHA_VENCIMIENTO": "2024-09-24",
#             "ID_DEV_RET": 3,
#             "MOTIVO": "ninguno",
#             "OBSERVACION": "",
#             "TIPO_DEVOLUCION": "ninguno",
#             "UNIDAD": "BOLSA"
#         }
#     ],
#     "encabezado": {
#         "ANULADO": 0,
#         "CANTIDAD_DETALLE": 2,
#         "CODCALIDAD": "dan@test.com ",
#         "CODCLIENTE_MERCADO": "M0107",
#         "CODVENDEDOR": "P0065",
#         "DESCRIPCION_CALIDAD": null,
#         "DESCRIPCION_CLIENTE": {
#             "DESCRIPCION_MERCADO": "LIMA NORTE 2",
#             "SEDE": "Lima"
#         },
#         "DESCRIPCION_GUIA": "001-073904",
#         "DESCRIPCION_SUB_CANAL": {
#             "CODIGO_INTERNO": "LN1",
#             "DESCRIPCION_DETSUBCLIENTE": "LIMA NORTE 1"
#         },
#         "DESCRIPCION_VENDEDOR": "Torres Olarte Donato",
#         "FECHA_EMISION": "2024-09-24 00:00:00",
#         "FECHA_REGISTRO": "2024-09-24 00:00:00",
#         "HORA_EMISION": "2024-09-24 16:13:15",
#         "IDGUIA": 69307,
#         "ID_DEV_RET": 3,
#         "NROSERIE": "1100003",
#         "SUB_CANAL": "1",
#         "USUARIO": "dan@test.com "
#     }
# }

from escpos.printer import Network

class Devolucion_Tiketera:

    def impresion(ip: str, data: dict) -> str:
        try:
            
            kitchen = Network(f'{ip}')
            encabezado = data['encabezado'] 
            detalle = data['detalles']

            kitchen.text(f'DOCUMENTO DE DEVOLUCION  {encabezado['DESCRIPCION_CLIENTE']['SEDE']}\n')
            kitchen.text(f'{encabezado['DESCRIPCION_CLIENTE']['DESCRIPCION_MERCADO']}   {encabezado['NROSERIE']}-{encabezado['ID_DEV_RET']}\n')
            kitchen.text(f'FECHA :{encabezado['FECHA_EMISION']}\n')
            kitchen.text(f'USUARIO :{encabezado['DESCRIPCION_VENDEDOR']}\n')
            kitchen.text(f'________________________________________\n')
            kitchen.text(f'CANTIDAD======DEVOLUCION======RETORNO\n')

            for item in detalle:
                descripcion_articulo = item['DESCRIPCION_ARTICULO']['DESCRIPCION_ARTICULO']
                cantidad_devolucion = str(item['CANTIDAD_DEVOLICION'])
                cantidad_retorno = str(item['CANTIDAD_RETORNO'])

                kitchen.text(f"{descripcion_articulo}\n")

                detalle_linea = f"{cantidad_devolucion.ljust(10)}{cantidad_retorno.ljust(10)}"
                kitchen.text(f"{detalle_linea}\n")
                kitchen.text(f'________________________________________\n')

            kitchen.text(f'USUARIO :{encabezado['USUARIO']}\n')

        except Exception as e:
            print(e)
            return False
        finally:
            kitchen.cut()
            kitchen.close()
            return {
                'message': 'Impresion exitosa'
            }
