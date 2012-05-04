__author__ = 'Dimasik'
L = (4, 12, 16, 56, 23, 24, 17, 34, 12, 34, 5, 6, 23,18)
sum = 0
for i in L:
    sum = sum + i
print  sum
x = 0
for i in L:
     x = x+1
D = {'min': min(L), 'max': max(L), 'average': sum/x}
print D


