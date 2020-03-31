import ipaddress
from scapy.layers.inet import ICMP, IP

class Ip:

    def __init__(self, i):
        self.get_range_from_ip(i)
    
    def get_range_from_ip(self, ip):
        res = []
        if not "/" in ip:
            res.append(ip)
        elif "/32" in ip:
            res.append(ip.split("/")[0])
        else:
            for i in ipaddress.ip_network(ip):
                res.append(str(i))
        
        print(res)
        self.range = res
    
    def check_ip(self, ip):
        packet = ICMP()/IP(dst=ip)
        print(packet.show())