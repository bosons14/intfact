#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import sys
from zeros import zeros
from mpmath import mp
from mpmath import zetazero


fwd=[8,4,2,1]
bwd=[1,2,4,8]


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


BLK = 4
def _synthesize_(p, num, i, zero_index):
    nn = ""
    pivot = ""
    count = 0
    if p == 0:
        nn = num[i]
        pivot = fwd
    else:
        nn = num[::-1][i]
        pivot = bwd
    for j in range(zero_index, zero_index + BLK):
        zero = get_zero(j)
        for k in range(0, pivot[j - zero_index] + 1):
            if zero[k] == nn:
                count = count + 1
    return count


def factorize(num):
    global BLK
    l = len(num)
    sum11 = 0
    sum12 = 0
    zero_index = 1
    i = 0
    c = 0
    sum1l = []
    sum2l = []
    while True:
        l1 = _synthesize_(0, num, i % l, zero_index)
        l2 = _synthesize_(1, num, i % l, zero_index)
        sum11 = sum11 + l1
        sum12 = sum12 + l2
        sum1 = sum11 + sum12
        zero_index = zero_index + BLK
        i = i + 1
        if l1 == 0 and l2 == 0:
            sum1l.append([i,sum11])
            sum2l.append([i,sum12])
        if sum1 in zeros:
            sum1l.append([i,sum11])
            sum2l.append([i,sum12])
            print([i, sum1, sum1l, sum2l])
            if i % l == 0:
                c = c + 1
            if c == l:
                break
            sum1l = []
            sum2l = []
            sum1 = 0
            sum11 = 0
            sum12 = 0
    return zero_index - 1


if __name__ == "__main__":
    num = str(sys.argv[1])
    factorize(num)
