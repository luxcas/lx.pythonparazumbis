# encoding: utf-8
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print 'Número maior: %d' %a
elif b >= c:
    print 'Número maior: %d' %b
else:
    print 'Número maior: %d' %c

