import socket

class TcpScan:

    def __init__(self, ip):
        self.ip = ip

    # 
    # Scan one TCP port with a timeout of 1s
    def scan_port(self, port):
        if port < 0 or port > 65535:
            return False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"[-] Try port {port}")
        try:
            sock.settimeout(1)
            sock.connect((self.ip, port))
            return True
        except socket.error:
            return False

    # Scan all TCP ports and print the open ones
    # TODO: return an array of open ports
    # TODO: add threads to speed up the scan
    def scan_all_ports(self):
        for i in range(0, 65536):
            if self.scan_port(i):
                print(f"[+] Open port: {i}")
