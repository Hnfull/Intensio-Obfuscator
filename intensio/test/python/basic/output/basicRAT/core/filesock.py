# -*- coding: utf-8 -*-















import socket



import struct







from crypto import PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg



from crypto import rzqOergcOwAqdICMWbxRcgDNsPNjYbRy



















def zyRDURipqNGanqOrKlMjDpZeOKOMCXCv(sock, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, key):



    with open(IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, 'wb') as f:



        ZjJwxywWVDXzGxjFOJePnlFxgsnOqLqe = struct.unpack("!I", sock.recv(4))[0]



        while ZjJwxywWVDXzGxjFOJePnlFxgsnOqLqe:



            znHRxERtkpIuXagwMBLvjzaFtvCMFteC = sock.recv(ZjJwxywWVDXzGxjFOJePnlFxgsnOqLqe)



            f.write(rzqOergcOwAqdICMWbxRcgDNsPNjYbRy(znHRxERtkpIuXagwMBLvjzaFtvCMFteC, key))



            ZjJwxywWVDXzGxjFOJePnlFxgsnOqLqe = struct.unpack("!I", sock.recv(4))[0]











def dAejAiYnebfrVxzpVgcryDbVphqVKBRb(sock, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, key):



    with open(IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, 'rb') as f:



        znHRxERtkpIuXagwMBLvjzaFtvCMFteC = f.read(4096)



        while len(znHRxERtkpIuXagwMBLvjzaFtvCMFteC):



            kgSBDOsnshaPeujmDLfATkkGqtOGsoEf = PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(znHRxERtkpIuXagwMBLvjzaFtvCMFteC, key)



            sock.send(struct.pack("!I", len(kgSBDOsnshaPeujmDLfATkkGqtOGsoEf)))



            sock.send(kgSBDOsnshaPeujmDLfATkkGqtOGsoEf)



            znHRxERtkpIuXagwMBLvjzaFtvCMFteC = f.read(4096)



        sock.send('\x00\x00\x00\x00') 



