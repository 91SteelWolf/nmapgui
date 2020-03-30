import socket

class TcpScan:

    def __init__(self, ip):
        self.ip = ip


    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[-] Try port {port}")
        try:
            sock.settimeout(1)
            sock.connect((self.ip, port))
            return True
        except socket.error:
            return False

    def scan_all_ports(self):
        for i in range(0, 65536):
            if self.scan_port(i):
                print(f"[+] Port open: {i}")

def main():
    scan = TcpScan("192.168.0.254")
    scan.scan_all_ports()

if __name__ == '__main__':
    main()