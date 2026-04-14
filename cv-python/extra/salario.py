aluno = 20
while (aluno > 0):
    nome = str(input('Escreva o nome do aluno: '))
    nota1 = int(input('Primeira nota: '))
    nota2 = int(input('Segunda nota: '))
    media = (nota1 + nota2)/2
    aluno = aluno - 1
    posicao = 20 - aluno
    if media >= 6:
        print('{} {}, passo com {} na media.'.format(posicao, nome, media))
    else:
        print('{} {}, foi reprovado com {} na media.'.format(posicao, nome, media))