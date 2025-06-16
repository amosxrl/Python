problema = {
    'estado_inicial': 'A',
    'estado_objetivo': 'S',
    'Acoes': {
        1: ['B', 'S', 320],
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
    """
    Cria um nó para a árvore de busca.
    """
    no = {
        'estado': estado,
        'noPai': noPai,
        'custo': custo,
        'acao': acao,
        'profundidade': profundidade
    }
    return no

def expandeNo(no, problema):
    """
    Expande um nó, gerando seus filhos a partir das ações disponíveis.
    """
    estado_atual = no['estado']
    filhos = []
    
    for chave, acao in problema['Acoes'].items():
        origem, destino, custo_acao = acao
        if origem == estado_atual:
            novo_no = criaNo(
                estado=destino,
                noPai=no,
                custo=no['custo'] + custo_acao,
                acao=acao,
                profundidade=no['profundidade'] + 1
            )
            filhos.append(novo_no)
    return filhos

def buscaEmArvore(problema, borda):
    """
    Executa a busca em árvore com expansão de nós e verificação de objetivo.
    """
    borda.append(criaNo(problema['estado_inicial']))
    solucao = []

    while borda and not solucao:
        # Remove o primeiro nó da borda (busca em largura)
        no_atual = borda.pop(0)
        print("Explorando:", no_atual['estado'])

        # Verifica se é o objetivo
        if no_atual['estado'] == problema['estado_objetivo']:
            solucao = no_atual
            break

        # Expande o nó atual e adiciona os filhos à borda
        filhos = expandeNo(no_atual, problema)
        borda.extend(filhos)

        # Mostra o conteúdo atual da borda
        print("Borda atual:", [n['estado'] for n in borda])
    
    if solucao:
        print("\nObjetivo encontrado!\n")
        caminho = []
        no = solucao
        while no:
            caminho.insert(0, no['estado'])
            no = no['noPai']
        print("Caminho até o objetivo:", caminho)
    else:
        print("Objetivo não encontrado.")

buscaEmArvore(problema, borda)
