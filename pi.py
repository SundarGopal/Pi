
import sys

def Arctan(d, ndigits):
    total = term = (10**ndigits) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d*d
        total += term // (2*n + 1)
    return total

if __name__ == '__main__':

    xdigits = 10             
    ndigits = int(input('Enter number of digits you want:'))

    pi = 4 * (4*Arctan(5,ndigits+xdigits) - Arctan(239,ndigits+xdigits))

    pi //= 10**xdigits

    text = str(pi)
    print(text[0] + '.',end='')
    text = text[1:]
    for i in text:
        print(i,end='')
