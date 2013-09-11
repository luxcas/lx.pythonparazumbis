d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))

tsdias = d * 24 * 60 * 60
tshoras = h * 60 * 60
tsminutos = m * 60

total = tsdias + tshoras + tsminutos + s
print "Total de segundos e: $d" %total
