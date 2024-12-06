from escpos.printer import Network 

class Printing:
    def __init__(self, ip , cofig_encabezado , config_detalle , config_firma):
        self.ip = ip
        self.config_encabezado = cofig_encabezado
        self.config_detalle = config_detalle
        self.config_firma = config_firma

    