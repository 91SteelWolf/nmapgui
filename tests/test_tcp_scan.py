import tcp_scan

def test_tcpscan():
    test1 = tcp_scan.TcpScan("192.168.0.254")
    assert test1.scan_port(80)
    assert test1.scan_port(139)
    assert not test1.scan_port(-1)
    assert not test1.scan_port(100000)
    assert not test1.scan_port(25)