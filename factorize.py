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


def _synthesize_(p, num, i, zero_index):
    nn = ""
    pivot = ""
    count = 0
    if p == 0:
        nn = num[i]
    else:
        nn = num[::-1][i]
    for j in range(zero_index, zero_index + 8):
        zero = get_zero(j)
        for k in range(0, 8):
            if zero[k:k + len(nn)] == nn:
                count = count + 1
    return count


def synthesize(num):
    l = len(num)
    sum11 = 0
    sum12 = 0
    zero_index = 1
    i = 0
    while True:
        l1 = _synthesize_(0, num, i % l, zero_index)
        l2 = _synthesize_(1, num, i % l, zero_index)
        zero_index = zero_index + 4
        i = i + 1
        k = input([i, l1, l2])
        if k == "0":
            break
    return i

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
