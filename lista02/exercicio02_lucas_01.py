# encoding: utf-8
a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > a + c or c > a + b:
  print ('Não pode ser um triângulo')
  print ('Um dos lados é maior que a soma dos outros')
elif a == b == c:
  print ('Triângulo equilátero')
elif a == b or b == c or a == c:
  print ('Triângulo isósceles')
else:
  print ('Triângulo escaleno')
  
