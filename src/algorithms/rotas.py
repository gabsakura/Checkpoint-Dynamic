from __future__ import annotations

from src.graphs.redes import REDES

import functools

"""uso de grafoskkkkk não entendi muito certinho como funciona"""
import networkx as nx

"""fator horario que o professor tinha pedido -> se quiser alternar mais em baixo esta comentado mais em baixo"""
def fator_horario(hora: int) -> float:
    """Multiplica o tempo por trecho conforme a hora inteira (-23).

    - 5h-7h: x0,6 — metrô vazio, embarque rápido (bônus).
    - 7h-9h: x1,5 — pico da manhã.
    - 9h-17h: x1,0 — fluxo regular.
    - 17h-20h: x2,0 — pico da tarde (penalidade).

    Limites: cada faixa usa [início, fim) em horas inteiras (ex.: 7h entra no pico da manhã).
    Fora dessas faixas: x1,0 (neutro).
    """
    if 5 <= hora < 7:
        return 0.6
    if 7 <= hora < 9:
        return 1.5
    if 9 <= hora < 17:
        return 1.0
    if 17 <= hora < 20:
        return 2.0
    return 1.0

"""não entendi muito bem como funciona a memoização (basicamente sistema de memorias) mas ta assim escrito para usar ++ calcula o tempo minimo de viagem entre estações"""
@functools.lru_cache(maxsize=None)
def menor_custo(
    rede_id: str, origem: str, destino: str, horario: int, visitados: frozenset[str]
) -> float:
    grafo = REDES[rede_id]["grafo"]
    if origem == destino:
        return 0.0
    if origem not in grafo:
        return float("inf")
    fator = fator_horario(horario)
    melhor = float("inf")
    for vizinho, peso in grafo[origem]:
        if vizinho not in visitados:
            custo = fator * peso + menor_custo(
                rede_id, vizinho, destino, horario, visitados | {origem}
            )
            melhor = min(melhor, custo)
    return melhor

"""converção de dicionarios para os grafos do networkx -> não entendi muito bem ainda"""
def grafo_networkx(grafo: dict[str, list[tuple[str, float]]]) -> nx.Graph:
    G = nx.Graph()
    for u, vizinhos in grafo.items():
        for v, w in vizinhos:
            G.add_edge(u, v, weight=w, minutes=w)
    return G

"""Sugestões de rotas com a memoria ativa"""
def sugestoes_todas_pares(
    rede_id: str, horario: int
) -> list[tuple[str, str, float, list[str]]]:
    grafo = REDES[rede_id]["grafo"]
    estacoes = list(grafo.keys())
    G = grafo_networkx(grafo)
    out: list[tuple[str, str, float, list[str]]] = []
    for o in estacoes:
        for d in estacoes:
            if o == d:
                continue
            custo = menor_custo(rede_id, o, d, horario, frozenset())
            if nx.has_path(G, o, d):
                caminho = nx.shortest_path(G, o, d, weight="weight")
            else:
                caminho = []
            out.append((o, d, custo, caminho))
    return out

"""outras rotas alternativas usando o networkxx -> peguei da documentação -> usa o all_simples_paths para encontrar literal todos os caminhoskkkk"""
def caminhos_simples_distintos(
    G: nx.Graph, origem: str, destino: str, max_caminhos: int = 8
) -> list[list[str]]:
    try:
        gen = nx.all_simple_paths(G, origem, destino, cutoff=len(G) + 1)
        return [p for _, p in zip(range(max_caminhos), gen)]
    except nx.NodeNotFound:
        return []

def maior_caminho_simples(
    rede_id: str,
    origem: str,
    destino: str,
    visitados: set[str] | None = None,
) -> tuple[float, list[str]]:
    if visitados is None:
        visitados = set()
    grafo = REDES[rede_id]["grafo"]
    if origem == destino:
        return 0.0, [origem]
    visitados.add(origem)
    melhor_custo = float("-inf")
    melhor_caminho: list[str] = []
    for vizinho, peso in grafo.get(origem, []):
        if vizinho not in visitados:
            custo_sub, caminho_sub = maior_caminho_simples(
                rede_id, vizinho, destino, visitados.copy()
            )
            if custo_sub != float("-inf"):
                custo_total = peso + custo_sub
                if custo_total > melhor_custo:
                    melhor_custo = custo_total
                    melhor_caminho = [origem] + caminho_sub
    return melhor_custo, melhor_caminho

"""limpar cache, evitar recalculos aparentemente"""
def limpar_cache_menor_custo() -> None:
    menor_custo.cache_clear()