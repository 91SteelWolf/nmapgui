import ipaddress

class Ip:

    def __init__(self, i):
        self.range = self.get_range_from_ip(i)
    
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
        return res