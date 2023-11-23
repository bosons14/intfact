#!/usr/bin/python3
import sys
from mpmath import mp
from mpmath import zetazero
from primes import primes
from zeros import zeros

PREC=1024
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

def primality_test(num):
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
       if zz == nn and dec != None:
           ratio = None
           if nones > 0:
               ratio = (float)(nzeros / (nones*1.0))
           if ratio == 0.5:
               return True
           elif ratio >= 0.6:
               return False
           zero_index = zero_index + 1
           zero = get_zero(zero_index)
           pos = 0
    f.close()
    g.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    is_prime = primality_test(num)
    print(is_prime)
