from collections import deque

# ---------------------- DEFINIÇÃO DO GRAFO ----------------------
acoes = {
    1: ['BA',  'S', 320],   2:  ['S',  'BA', 320],
    3: ['S',  'A', 110],    4:  ['A',  'S', 110],
    5: ['A',  'P', 360],    6:  ['P',  'A', 360],
    7: ['P', 'PB', 260],    8: ['PB',  'P', 220],
    9: ['PB', 'RN', 290],   10: ['RN', 'PB', 290],
   11: ['C', 'RN', 420],   12: ['RN',  'C', 420],
   13: ['PB',  'C', 500],  14:  ['C', 'PB', 500],
   15: ['P', 'PI',1120],   16: ['PI',  'P',1120],
   17: ['PI',  'C', 590],  18:  ['C', 'PI', 590],
   19: ['PI',  'M', 450],  20:  ['M', 'PI', 450],
   21: ['BA', 'PI',1150],  22: ['PI',  'BA',1150]
}

# -------------------- OBTÉM TODOS OS ESTADOS --------------------
def extrair_estados(acoes):
    estados = set()
    for origem, destino, _ in acoes.values():
        estados.add(origem)
        estados.add(destino)
    return sorted(estados)

# ---------------------- CRIAÇÃO DE NÓ ----------------------
def criaNo(estado, noPai=None, custo=0, acao=None, profundidade=0):
    return {
        'estado'      : estado,
        'noPai'       : noPai,
        'custo'       : custo,
        'acao'        : acao,
        'profundidade': profundidade
    }

# ---------------------- EXPANSÃO DE NÓ ----------------------
def expandeNo(no, acoes):
    filhos = []
    for origem, destino, custo_acao in acoes.values():
        if origem == no['estado']:
            filhos.append(
                criaNo(destino, no,
                       custo=no['custo'] + custo_acao,
                       acao=(origem, destino, custo_acao),
                       profundidade=no['profundidade'] + 1)
            )
    return filhos

# ---------------------- BUSCA EM LARGURA ----------------------
def buscaEmArvore(estado_inicial, estado_objetivo, acoes):
    borda = deque([criaNo(estado_inicial)])
    visitados = set()
    ordem_visita = []

    while borda:
        no_atual = borda.popleft()
        if no_atual['estado'] in visitados:
            continue

        visitados.add(no_atual['estado'])
        ordem_visita.append(no_atual['estado'])
        print("Explorando:", no_atual['estado'])

        if no_atual['estado'] == estado_objetivo:
            caminho = []
            while no_atual:
                caminho.insert(0, no_atual['estado'])
                no_atual = no_atual['noPai']
            print("\n✅ Objetivo encontrado!")
            print("🛣️ Caminho até o objetivo:", caminho)
            print("🔍 Ordem de nós visitados:", ordem_visita)
            return caminho

        for filho in expandeNo(no_atual, acoes):
            if (filho['estado'] not in visitados and
                all(filho['estado'] != n['estado'] for n in borda)):
                borda.append(filho)

    print("❌ Objetivo não encontrado.")
    print("🔍 Ordem de nós visitados:", ordem_visita)
    return None

# ---------------------- INTERFACE DE USUÁRIO ----------------------
if __name__ == "__main__":
    estados = extrair_estados(acoes)
    print("🌐 Estados disponíveis no mapa:")
    print(", ".join(estados))

    estado_inicial = input("🔽 Digite o estado inicial: ").strip().upper()
    estado_objetivo = input("🔼 Digite o estado objetivo: ").strip().upper()

    if estado_inicial not in estados or estado_objetivo not in estados:
        print("❗Erro: Um dos estados digitados não é válido.")
    else:
        buscaEmArvore(estado_inicial, estado_objetivo, acoes)
