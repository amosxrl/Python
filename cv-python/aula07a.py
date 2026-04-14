
'''
Operadores Logicos
	+ Adição
	- Subtração
	* Multiplicação
	/ Divisão
	** Potencia
	
	// Divisão inteira
	% Resto da divisão

Dentro de uma espreção
	1°() 
	2°** 
	3°* / // %
	4°+ -

'''
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Escreva um número: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2

print('A soma é {}, o produto é {}, e a divisão {:.3f},'.format(s, m, d))
print('A potencia é {}, \n a dividão inteira {}'.format(e, di), end=' ')
print('e o resto é {}'.format(rd))
