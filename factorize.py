#!/usr/bin/python3
import sys
from mpmath import mp
from mpmath import zetazero

PREC=32
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


def _synthesize_(p, num, i, zero):
    nn = ""
    pivot = ""
    count = 0
    if p == 0:
        nn = num[i]
    else:
        nn = num[::-1][i]
    for k in range(0, 8):
       if zero[k] == nn:
            count = count + 1
    return count

def get_interstitial_digits(zero, l1, l2):
    if l1 > l2:
        t = l1
        l1 = l2
        l2 = t
    delta = l2 - l1
    if delta > 1:
        return zero[l1:l2-1]
    else:
        return None

def synthesize(num):
    l = len(num)
    zero_index = 1
    i = 0
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    while True:
        zero = get_zero(zero_index)
        l1 = _synthesize_(0, num, i % l, zero)
        l2 = _synthesize_(1, num, i % l, zero)
        pp = f.read(1)
        ee = g.read(1)
        k = input([i, l1, l2, get_interstitial_digits(zero, l1, l2), zero_index, pp, ee])
        if k == "y" and ee == "0": 
            c = c + 1
            if c == l:
                break
        zero_index = zero_index + 1
        i = i + 1
    return zero_index

def analyze(pivot):
    f = open("./pi.txt","r")
    g = open("./e.txt","r")
    f.read(2)
    g.read(2)
    pp = f.read(pivot)
    ee = g.read(pivot)[::-1]
    equal = 0
    greater = 0
    lesser = 0
    for k in list(zip(pp, ee)):
        print(k[0], k[1])
        if int(k[0]) < int(k[1]):
            lesser = lesser + 1
        elif int(k[0]) > int(k[1]):
            greater = greater + 1
        elif int(k[0]) == int(k[1]) and k[0] != "8":
            equal = equal + 1
        if k[0] == k[1] and k[0] == "8":
            input([equal, greater, lesser])
            equal = 0
            greater = 0
            lesser = 0
    input([equal, greater, lesser])
    f.close()
    g.close()

if __name__ == "__main__":
    num = str(sys.argv[1])
    pivot = synthesize(num)
    print(pivot)
    print("")
    analyze(pivot)
