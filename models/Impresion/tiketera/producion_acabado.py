# {
#   "detalles": [
#     {
#       "CANTIDAD": 35,
#       "COD_ARTICULO": "A0005",
#       "DESCRIPCION_ARTICULO": {
#         "CODIGO": "A18TNOT",
#         "DESCRIPCION_ARTICULO": "ALFAJOR x 18 UND DE 950 G",
#         "DESCRIPCION_MARCA": "TORRINO",
#         "DESCRIPCION_UNIDAD_MEDIDA": "TAPER",
#         "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#         "UM": "TAP",
#         "UM_PRESENTACION": null
#       },
#       "IDCONFIRMACION": null,
#       "IDCONTROL": 1
#     },
#     {
#       "CANTIDAD": 23,
#       "COD_ARTICULO": "A0004",
#       "DESCRIPCION_ARTICULO": {
#         "CODIGO": "BIZ12TSB",
#         "DESCRIPCION_ARTICULO": "BIZCOCHO ESPECIAL X 12 780 G UND",
#         "DESCRIPCION_MARCA": "TORRES",
#         "DESCRIPCION_UNIDAD_MEDIDA": "BOLSA",
#         "DESCRIPCION_UNIDAD_MEDIDA_PRESENTACION": null,
#         "UM": "BLS",
#         "UM_PRESENTACION": null
#       },
#       "IDCONFIRMACION": null,
#       "IDCONTROL": 1
#     }
#   ],
#   "encabezado": {
#     "ANULADO": 0,
#     "FECHA_ENTREGA": "2023-05-12 00:00:00",
#     "FECHA_REF_PRODUCCION": "2023-05-12 00:00:00",
#     "FECHA_REGISTRO": "2025-02-17 10:18:13",
#     "IDCONTROL": 1,
#     "USUARIO": "TEST POST"
#   }
# }

from escpos.printer import  Network

class Acabado_Producion:
    @staticmethod
    def imprimir_guiones(kitchen):
        # Imprime un guion bajo "_" 30 veces en la impresora
        kitchen.text("_" * 30 + "\n")

    @staticmethod
    def impresion (ip , data:dict) -> bool:
        encabezado = data['encabezado']
        detalles = data['detalles']


        try:
            kitchen = Network(f'{ip}')

            kitchen.text('PRODUCCION ACABADO\n')

            id = str(encabezado['IDCONTROL'])

            kitchen.text(f"{id}")

            fecha_entrega = str(encabezado['FECHA_ENTREGA'])
            fecha_ref_produccion = str(encabezado['FECHA_REF_PRODUCCION'])
            fecha_registro = str(encabezado['FECHA_REGISTRO'])

            kitchen.text(f"FEC. ENTREGA: {fecha_entrega}\n")

            kitchen.text(f"FEC. REF PRODUCCION: {fecha_ref_produccion}\n")

            kitchen.text(f"FEC. REGISTRO: {fecha_registro}\n")

            usuario = str(encabezado['USUARIO'])

            Acabado_Producion.imprimir_guiones(kitchen)
            kitchen.text("CODARTICULO====CODIGO====CANTIDAD\n")
            Acabado_Producion.imprimir_guiones(kitchen)

            for det in detalles:
                art = det['DESCRIPCION_ARTICULO']
                cod_art = det['COD_ARTICULO']
                cod = art['CODIGO']
                cantidad = det['CANTIDAD']
                kitchen.text(f"{cod_art}===={cod}===={cantidad}\n")


            kitchen.text(f"{usuario}: \n")
            Acabado_Producion.imprimir_guiones()

            kitchen.cut()
            kitchen.close()
            return {
                'message': 'Impresión exitosa'
            }
        except Exception as e:
            print(e)
            raise Exception(e)
















