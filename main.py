from models.Networth_Printer import Networth_Printer


def main():
    network = "192.168.1.0/24"  
    target_port = 9100
    timeout = 1 

    network_printer = Networth_Printer(network, target_port, timeout)
    printers = network_printer.search_printer()

    print("Impresoras encontradas:")
    for printer in printers:
        print(printer)

if __name__ == "__main__":
    main()