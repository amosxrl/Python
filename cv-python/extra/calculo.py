import math
import random

base = float(input("Escreva a base da area: "))
altura = float(input("Escreva a altura da area: "))
area = base*altura
print('A área é igual a: ', area)

branco = math.ceil(1000*random.random())
nulo = math.ceil(100*random.random())
valido = math.ceil(10000*random.random())
total = branco + nulo + valido
print("Na eleição de 2022 teve {} votos validos, {} bracos e {} nulos. Totalizando {} eleitores presentes." .format(valido, branco, nulo, total))

fabrica = int(input('Escreva o valor de produção do carro: '))
carro = (fabrica*1.28)*1.45
print('O carro vai custar: ', carro)

