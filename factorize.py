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
            if zero[k] == nn:
                count = count + 1
    return count


def factorize(num):
    l = len(num)
    sum11 = 0
    sum12 = 0
    zero_index = 1
    i = 0
    less = 0
    greater = 0
    equal = 0
    while True:
        l1 = _synthesize_(0, num, i % l, zero_index)
        l2 = _synthesize_(1, num, i % l, zero_index)
        if l1 == l2 and l1 > 0:
            equal = equal + 1
        elif l1 < l2:
            less = less + 1
        elif l1 > l2:
            greater = greater + 1
        zero_index = zero_index + 8
        i = i + 1
        print([i, l1, l2])
        if l1 == l2 and l1 == 0:
            y= input([i, l1, l2, equal, greater, less])
            equal = 0
            greater = 0
            lesser = 0
            if y == "0":
                break

def tokenize(num):
    tokens = []
    c = 0
    token = ""
    l = len(num)
    while c < l:
        if len(token) > 0 and token[-1] == num[c]:
            token = token + num[c]
        else:
            if len(token) > 0:
                tokens.append(token)
                token = ""
            token = num[c]
        c = c + 1
    if len(token) > 0:
        tokens.append(token)
    return tokens

if __name__ == "__main__":
    num = str(sys.argv[1])
    tokens = tokenize(num)
    factorize(tokens)
