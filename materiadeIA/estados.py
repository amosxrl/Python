#   Eu me perdi no meio do caminho.
from collections import deque

# --------------------------- PROBLEMA ------------------------
#   estado_inicial  : nó de partida
#   estado_objetivo : nó que queremos alcançar
#   Acoes           : dicionário cujos valores = [origem, destino, custo]
# ------------------------------------------------------------

problema = {
    'estado_inicial': 'AL',
    'estado_objetivo': 'CE',
    'Acoes': {
        1:  ['BA', 'SA', 320],   2: ['SA', 'BA', 320],
        3:  ['SA', 'AL', 110],   4: ['AL', 'SA', 110],
        5:  ['AL', 'PE', 360],   6: ['PE', 'AL', 360],
        7:  ['PE', 'PB', 260],   8: ['PB', 'PE', 220],
        9:  ['PB', 'RN', 290],  10: ['RN', 'PB', 290],
       11:  ['CE', 'RN', 420],  12: ['RN', 'CE', 420],
       13:  ['PB', 'CE', 500],  14: ['CE', 'PB', 500],
       15:  ['PE', 'PI',1120],  16: ['PI', 'PE',1120],
       17:  ['PI', 'CE', 590],  18: ['CE', 'PI', 590],
       19:  ['PI', 'MA', 450],  20: ['MA', 'PI', 450],
       21:  ['BA', 'PI',1150],  22: ['PI', 'BA',1150]
    }
}

# ---------------------- ESTRUTURA DE NÓ ----------------------
#   estado       : vértice atual
#   noPai        : referência ao nó que o gerou
#   custo        : custo acumulado (não usado pela BFS, mas útil p/ outros algoritmos)
#   acao         : tupla (origem, destino, custo) que levou ao nó
#   profundidade : nível na árvore de busca (raiz = 0)
# ------------------------------------------------------------
def criaNo(estado, noPai=None, custo=0, acao=None, profundidade=0):
    return {
        'estado'      : estado,
        'noPai'       : noPai,
        'custo'       : custo,
        'acao'        : acao,
        'profundidade': profundidade
    }

# ---------------------- EXPANSÃO DE NÓ -----------------------
#   Percorre todas as ações do problema; se a origem coincide com
#   o estado atual, gera um filho correspondente ao destino.
# ------------------------------------------------------------
def expandeNo(no, problema):
    filhos = []
    for origem, destino, custo_acao in problema['Acoes'].values():
        if origem == no['estado']:
            filhos.append(
                criaNo(destino,                 # novo estado
                       noPai=no,                # pai = nó atual
                       custo=no['custo'] + custo_acao,
                       acao=(origem, destino, custo_acao),
                       profundidade=no['profundidade'] + 1)
            )
    return filhos

# ---------------------- BUSCA EM LARGURA --------------------
#   Utiliza uma fila FIFO (deque) para explorar por níveis.
#   visitados  : evita re‑expandir um mesmo estado
#   ordem_visita: guarda todos os estados na ordem exata de visita
# ------------------------------------------------------------
def buscaEmArvore(problema):
    # inicializa fila com o nó da raiz
    borda = deque([criaNo(problema['estado_inicial'])])

    visitados = set()   # conjunto de estados já explorados
    ordem_visita = []   # lista cronológica de visita

    # PROCESSO PRINCIPAL -------------------------------------
    while borda:
        # 1. retira o próximo nó da fila
        no_atual = borda.popleft()

        # 2. ignora se já visitamos este estado (pode ocorrer
        #    quando vários caminhos diferentes levam ao mesmo nó)
        if no_atual['estado'] in visitados:
            continue

        # 3. marca como visitado e registra ordem
        visitados.add(no_atual['estado'])
        ordem_visita.append(no_atual['estado'])
        print("Explorando:", no_atual['estado'])

        # 4. TESTE DE OBJETIVO
        if no_atual['estado'] == problema['estado_objetivo']:
            # reconstruir caminho de trás para frente
            caminho = []
            aux = no_atual
            while aux:
                caminho.insert(0, aux['estado'])
                aux = aux['noPai']

            # ---- SAÍDA DE SUCESSO ----
            print("\nObjetivo encontrado!")
            print("Caminho até o objetivo:", caminho)
            print("Ordem completa de nós visitados:", ordem_visita)
            return caminho  # encerra a função

        # 5. EXPANSÃO: gera filhos e adiciona à fila
        for filho in expandeNo(no_atual, problema):
            # coloca na fila somente se:
            #   • ainda não visitado
            #   • e não está atualmente na fila (evita duplicação)
            if (filho['estado'] not in visitados and
                all(filho['estado'] != n['estado'] for n in borda)):
                borda.append(filho)

    # ---------- SE A FILA ESVAZIAR SEM ENCONTRAR -------------
    print("Objetivo não encontrado.")
    print("Ordem completa de nós visitados:", ordem_visita)
    return None

# --------------------- ROTINA DE TESTE -----------------------
if __name__ == "__main__":
    # Executa a busca e mostra tudo na tela
    buscaEmArvore(problema)

# ------------------------------------------------------------
# --------------------- FIM DO CÓDIGO ------------------------
# ------------------------------------------------------------
