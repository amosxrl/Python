# O código volta vazio, mas não mostra erro
problema = {'estado_inicial':'A',
            'estado_objetivo':'M',
            'Acoes':{1: ['B', 'S', 320],
                     2: ['S', 'B', 320],
                     3: ['S', 'A', 110],
                     4: ['A', 'S', 110],
                     5: ['A', 'P', 360],
                     6: ['P', 'A', 360],
                     7: ['P', 'PB', 260],
                     8: ['PB', 'P', 220],
                     9: ['PB', 'RN', 290],
                     10: ['RN', 'PB', 290],
                     11: ['C', 'RN', 420],
                     12: ['RN', 'C', 420],
                     13: ['PB', 'C', 500],
                     14: ['C', 'PB', 500],
                     15: ['P', 'PI', 1120],
                     16: ['PI', 'P', 1120],
                     17: ['PI', 'C', 590],
                     18: ['C', 'PI', 590],
                     19: ['PI', 'M', 450],
                     20: ['M', 'PI', 450],
                     21: ['B', 'PI', 1150],
                     22: ['PI', 'B', 1150]
                     }
            }
borda = []

def criaNo(estado, noPai=None, custo=0, acao=None, profundidade=0):
  no={}
  no ['estado'] = estado
  no ['noPai'] = noPai
  no ['custo'] = custo
  no ['acao'] = acao
  no ['profundidade'] = profundidade
  return no 

# usei os nomes espaço (espandir) e filhos no lugar de (sucessores)
def espandir(no, problema):
#  filhos = 'no filhos'
  sucessores = []
  for acao in problema['Acoes']:
    if problema['Acoes'][acao][0] == no['estado']:
      s = criaNo(problema['Acoes'][acao][1], no['estado'], problema['Acoes'][acao][2] + no['custo'], acao, no['profundidade'] + 1)
      sucessores.append(s)
#  estado_atual = no['estado_inicial']
#  for chave, (origem, destino, custo) in problema['Acoes'].items():
#    if origem == estado_atual:
#      filho = criaNo(
#        destino,
#        noPai=no,
#        custo=no['custo'] + custo,
#        acao=chave,
#        profundidade=no['profundidade'] + 1
#      )
#      filhos.append(filho)
  return sucessores


def buscaEmArvore(problema, borda):
  borda.append(criaNo(problema['estado_inicial']))
  solucao = []

  while solucao == []:
    if len(borda) == 0:
      raise Exception('Sem Solucao')
      break

    no = borda.pop(0)
    if problema['estado_objetivo'] == no['estado']:
      solucao = no
      return solucao
    borda.extend(espandir(no, problema))

solucao = buscaEmArvore(problema, borda)

for filho in espandir(criaNo('A'), problema):
    print(f"Estado: {filho['estado']}, Custo: {filho['custo']}, Ação: {filho['acao']}")
