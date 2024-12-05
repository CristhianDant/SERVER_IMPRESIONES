from models.Networth_Printer import Networth_Printer
from .model import Printer


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
            self.db.add(Printer(**printer))

        self.db.commit()
        

    def get_printers(self):
        return self.db.query(Printer).all()
    
    def get_printer(self, id):
        return self.db.query(Printer).filter(Printer.id == id).first()
    
    



            
        