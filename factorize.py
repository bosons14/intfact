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
    if l1 > l2 and l1 - l2 > 1:
        return zero[l2:l1-1]
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
    matches = []
    while True:
        zero = get_zero(zero_index)
        l1 = _synthesize_(0, num, i % l, zero)
        l2 = _synthesize_(1, num, i % l, zero)
        synthesis_pivots.append([l1, l2])
        interstitial_digits = get_interstitial_digits(zero, l1, l2)
        pp = f.read(1)
        ee = g.read(1)
        print([i, l1, l2, interstitial_digits, zero_index, pp, ee])
        if interstitial_digits != None and pp in interstitial_digits and interstitial_digits != None:
            if l1 > l2:
                matches.append(1)
                print("match1")
            elif l1 < l2:
                matches.append(0)
                print("match0")
            if pp == "8" and ee == "0":
                break
        else:
            matches.append(None)
            print("matchN")
        zero_index = zero_index + 1
        i = i + 1
    f.close()
    g.close()
    return zero_index, synthesis_pivots, matches

def analyze(pivot, synthesis_pivots, matches):
    f = open("./pi.txt","r")
    f.read(2)
    g = open("./e.txt","r")
    g.read(2)
    pp = str(f.read(pivot))[::-1]
    ee = str(g.read(pivot))
    f.close()
    g.close()
    k = 0
    matches = matches[::-1]
    zero_index = 1
    for zz in list(zip(pp, ee, synthesis_pivots[::-1])):
        zero = get_zero(zero_index)
        interstitial_digits = get_interstitial_digits(zero, zz[2][1], zz[2][0])
        print([zz[0], zz[1], interstitial_digits,zz[2], matches[k]])
        zero_index = zero_index + 1
        if zz[2] != None and zz[2][0] < zz[2][1]:
            if interstitial_digits != None and zz[0] in interstitial_digits:
                if matches[k] != None:
                    input("Conflict")
                else:
                    matches[k] = [zz[0], zz[1], "*"]
        else:
            if matches[k] == None:
                pass
            else:
                matches[k] = [zz[0], zz[1], "+"]
        k = k + 1
    matches = matches[::-1]
    return matches

if __name__ == "__main__":
    num = str(sys.argv[1])
    zero_index, synthesis_pivots, matches = synthesize(num)
    print(zero_index)
    matches = analyze(zero_index, synthesis_pivots, matches)
    for x in matches:
        if x != None:
            print(x)
