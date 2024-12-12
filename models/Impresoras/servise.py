from models.Networth_Printer import Networth_Printer
from .model import Printer_database


class PrinterService:
    def __init__(self , db):
        self.db = db
    
    
    def reguister_printer_tickers(self):
        print("Registrando impresoras de tickets")
        network = "192.168.1.0/24"  
        target_port = 9100
        timeout = 1 

        network_printer = Networth_Printer(network, target_port, timeout)
        printers = network_printer.search_printer()

        for printer in printers:
            printer['activo'] = True
            printer['tipo'] = 'TICKET'
            self.db.add(Printer_database(**printer))

        self.db.commit()
        

    def get_printers(self):
        result = self.db.query(Printer_database).all()
        return result
    
    def get_printer(self, id):
        return self.db.query(Printer_database).filter(Printer_database.id == id).first()
    

    
    
    



            
        