from models.Networth_Printer import Networth_Printer
from .model import Printer_database


class PrinterService:
    def __init__(self , db):
        self.db = db


    
    
    def reguister_printer_tickers(self):
        print("Registrando impresoras de tickets")
        ## Eliminar todas las impresoras
        self.db.query(Printer_database).delete()
        ## Archivos de busqueda de impresoras
        network = "192.168.1.0/24"  
        target_port = 9100
        timeout = 1 

        network_printer = Networth_Printer(network, target_port, timeout)
        printers = network_printer.search_printer()

        for printer in printers:
            printer['activo'] = True
            printer['tipo'] = 'TICKET'
            printer['name_printer'] = 'No name'

            self.create_printer(Printer_database(**printer))

        self.db.commit()
        

    def get_printers(self):
        result = self.db.query(Printer_database).all()
        return result
    
    def get_printer(self, id):
        return self.db.query(Printer_database).filter(Printer_database.id == id).first()
    
    def get_printer_mac(self, mac):
        return self.db.query(Printer_database).filter(Printer_database.mac == mac).first()
    
    def create_printer(self, printer: Printer_database):
        self.db.add(printer)
        self.db.commit()
        return printer
    
    def update_name_printer(self, id: int, name: str):
        printer = self.get_printer(id)
        if not printer:
            return None
        printer.name_printer = name
        self.db.commit()
        print(printer)
        return {
            "message": "Nombre de impresora actualizado",
            "id": printer.id,
            "name": printer.name_printer
        }
    

    
    
    



            
        