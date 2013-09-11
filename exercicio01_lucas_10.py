# encoding: utf-8
cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print 'Você perdeu aproximadamente %.2f dias' %dias_perdidos
