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
    synthesis_pivots = []
    interstitial_digits_list = []
    matches = []
    while True:
        zero = get_zero(zero_index)
        l1 = _synthesize_(0, num, i % l, zero)
        l2 = _synthesize_(1, num, i % l, zero)
        synthesis_pivots.append([l1, l2])
        interstitial_digits = get_interstitial_digits(zero, l1, l2)
        interstitial_digits_list.append(interstitial_digits)
        pp = f.read(1)
        ee = g.read(1)
        k = input([i, l1, l2, interstitial_digits, zero_index, pp, ee])
        if k == "y" and interstitial_digits != None:
            if l1 > l2:
                matches.append(1)
            elif l1 < l2:
                matches.append(0)
        else:
            matches.append(None)
        if k == "y" and ee == "0": 
            break
        zero_index = zero_index + 1
        i = i + 1
    f.close()
    g.close()
    return zero_index, synthesis_pivots, interstitial_digits_list, matches

def analyze(pivot, synthesis_pivots, interstitial_digits_list, matches):
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    pp = str(f.read(pivot))[::-1]
    ee = str(g.read(pivot))
    k = 0
    for zz in list(zip(ee, interstitial_digits_list, synthesis_pivots)):
        y = input([zz[0], zz[1], zz[2][::-1]])
        if y == "y":
            if zz[2][::-1][0] > zz[2][::-1][1]:
                matches[k] = 1
            elif zz[2][::-1][0] < zz[2][::-1][1]:
                matches[k] = 0
        k = k + 1
    f.close()
    g.close()
    return matches

if __name__ == "__main__":
    num = str(sys.argv[1])
    zero_index, synthesis_pivots, interstitial_digits_list, matches = synthesize(num)
    print(pivot)
    matches = analyze(zero_index, synthesis_pivots, interstitial_digits_list, matches)
    for x in matches:
        if x != None:
            input(x)
