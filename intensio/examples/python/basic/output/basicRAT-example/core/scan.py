# -*- coding: utf-8 -*-
import socket
qjWGDJYOgzuHacnJwhJGEynETjOWfFao = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def gwhsEXhmXTHzYVlQiiEdGOqoneHqHRbR(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = ''
    for gFsSukpmrcgWJfrmLhgayqqAVmsbyWUi in qjWGDJYOgzuHacnJwhJGEynETjOWfFao:
        OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        LEatxLisbDvTmqMNouFMWYbWdrXRQSuy = OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.connect_ex((ip, gFsSukpmrcgWJfrmLhgayqqAVmsbyWUi))
        socket.setdefaulttimeout(0.5)
        FZIWIhvqdZYeZoNRoeRHkBfakHLwHgQR = 'open' if not LEatxLisbDvTmqMNouFMWYbWdrXRQSuy else 'closed'
        clbTiTFqUxkqbuQVZtaTgDqCquqcATPC += '{:>5}/tcp {:>7}\n'.format(gFsSukpmrcgWJfrmLhgayqqAVmsbyWUi, FZIWIhvqdZYeZoNRoeRHkBfakHLwHgQR)
    return clbTiTFqUxkqbuQVZtaTgDqCquqcATPC.rstrip()
