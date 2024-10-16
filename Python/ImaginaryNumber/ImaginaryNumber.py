import cmath

imaginarynumer = str(input())

a = int(imaginarynumer[0:imaginarynumer.index(' ')])
b = int(imaginarynumer[imaginarynumer.rindex(' '):imaginarynumer.index('j')])


print(abs(complex(a,b)))
print(cmath.phase(complex(a,b)))