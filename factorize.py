#!/usr/bin/python3
import sys
from mpmath import mp
from mpmath import zetazero
from primes import primes
from zeros import zeros

PREC=2048
_zeros_ = dict([])
def get_zero(index):
    global _zeros_
    global PREC
    mp.prec=PREC
    mp.dps=PREC
    if index in _zeros_.keys():
        return _zeros_[index]
    else:
        zero = str(zetazero(index).imag)
        idx = zero.index(".")
        zero = zero[idx + 1:]
        _zeros_[index] = zero
        return zero

def decide(ss):
    dec = None
    if ss in primes and not ss in zeros:
       dec = 0
    elif ss in primes and ss in zeros:
       dec = 1
    else:
       dec = None
    return dec

def factorize(num):
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    c = 0
    l = len(num)
    dec = None
    pos = 0
    zero_index = 1
    zero = get_zero(zero_index)
    nzeros = 0
    nones = 0
    while True:
       pp = str(f.read(1))
       ee = str(g.read(1))
       nn = num[c % l]
       c = c + 1
       ss = int(pp + nn + ee)
       dec = decide(ss)
       if dec == 0:
           nzeros = nzeros + 1
       elif dec == 1:
           nones = nones + 1
       zz = zero[pos]
       pos = pos + 1
       #input([ss, nzeros, nones, zz, nn])
       if zz == nn and dec != None:
           ratio = None
           if nones > 0:
               ratio = (float)(nzeros / (nones*1.0))
           if ratio != None and ratio == 0.5:
                input([nzeros,nones,ratio, dec])
                zero_index = zero_index + 1
                zero = get_zero(zero_index)
                pos = 0
                nzeros = 0
                nones = 0
    f.close()
    g.close()
    lower_factor_dec = ""
    higher_factor_dec = ""
    lower_factor_dec = int(lower_factor, 2)
    return lower_factor_dec

if __name__ == "__main__":
    num = str(sys.argv[1])
    factor1 = factorize(num)
    print(factor1)
