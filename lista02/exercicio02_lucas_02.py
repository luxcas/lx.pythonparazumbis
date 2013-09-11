# encoding: utf-8
a = int(input('Ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print 'Ano bissexto'
else:
    print ('N‹o Ž bissexto')
