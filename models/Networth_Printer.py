import socket
import subprocess
import re
import ipaddress
from concurrent.futures import ThreadPoolExecutor

class Networth_Printer:
    def __init__(self, network, target_port, timeout=1):
        self.network = network
        self.target_port = target_port
        self.timeout = timeout
        self.printers = []

    def check_port(self, ip):
        try:
            sock = socket.create_connection((ip, self.target_port), timeout=self.timeout)
            sock.close()
            mac_address = self.get_mac_address(ip)
            self.printers.append({'ip': ip, 'mac': mac_address})
        except (socket.timeout, socket.error):
            pass

    def get_mac_address(self, ip):
        try:
            output = subprocess.check_output(f"arp -a {ip}", shell=True, universal_newlines=True)
            mac_address = re.findall(r"([0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2})", output)
            if mac_address:
                return mac_address[0]
            else:
                return "MAC no encontrada"
        except subprocess.CalledProcessError:
            return "Error al ejecutar ARP"

    def scan_network(self):
        net = ipaddress.IPv4Network(self.network)
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(self.check_port, (str(ip) for ip in net.hosts()))

    def search_printer(self) -> list:
        self.printers = []
        self.scan_network()
        return self.printers

