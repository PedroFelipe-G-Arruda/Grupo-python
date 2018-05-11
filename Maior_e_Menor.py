a = float(input('digite um numero:'))
b = float(input('digite um numero:'))
c = float(input('digite um numero:'))

if a > b:
    if a > c:
        ma = a
        if b > c:
            mi = c
        if c > b:
            mi = b

if b > a:
    if b > c:
        ma = b
        if a > c:
            mi = c
        if c > a:
            mi = a

if c > b:
    if c > a:
        ma = c
        if b > a:
            mi = a
        if a > b:
            mi = b        
        
print('O menor numero e : {} e o maior e {}'.format(mi, ma))