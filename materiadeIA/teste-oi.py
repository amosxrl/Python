# Definição do problema
problema = {
    'estado_inicial': 'A',
    'estado_objetivo': 'P',
    'Acoes': {
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

# Função para criar nós
def criaNo(estado_inicial, noPai=None, custo=0, acao=None, profundidade=0):
    no = {}
    no['estado_inicial'] = estado_inicial
    no['noPai'] = noPai
    no['custo'] = custo
    no['acao'] = acao
    no['profundidade'] = profundidade
    return no

# Função de expansão fictícia para teste
def espaco(no, problema):
    # Para teste, retorna um filho fictício ou lista vazia
    filho_ficticio = criaNo('X', noPai=no, custo=999, acao=999, profundidade=no['profundidade'] + 1)
    return [filho_ficticio]

# Função de busca em árvore
def buscaEmArvore(problema, borda):
    borda.append(criaNo(problema['estado_inicial']))
    solucao = []

    while solucao == []:
        if len(borda) == 0:
            raise Exception('Sem Solucao')
            break

        no = borda.pop(0)
        print(f"Expandindo nó: {no}")  # Para ver o que está sendo expandido

        if problema['estado_objetivo'] == no['estado_inicial']:
            solucao.append(no)
            return solucao

        filhos = espaco(no, problema)
        borda.extend(filhos)  # Usar extend, não append

    return solucao

# Execução do teste
solucao = buscaEmArvore(problema, borda)
print("Solução encontrada:", solucao)
