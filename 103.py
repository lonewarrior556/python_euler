import math

def first_n_digits(num, n):
    return str(num // 10 ** (int(math.log(num, 10)) + 1 - n ))

f0 = 0
f1 = 1
f2 = 1

seq = 2
while True:
    seq+=1
    f0 = f1
    f1 = f2
    f2 = f0 + f1
    last = str(f2 % 1000000000)
    if (''.join(sorted(last)) == '123456789'):
        print 'seq-last', seq
        first = first_n_digits(f2, 9)
        if (''.join(sorted(first)) == '123456789'):
            print 'seq-both', seq
            break
