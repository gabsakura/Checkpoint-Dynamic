from src.graphs.redes import REDES

"""Importando as funções de rotas.py"""
from src.algorithms.rotas import(
    menor_custo,
    grafo_networkx,
    caminhos_simples_distintos,
)

import networkx as nx

"""Printar diferentes relatorios"""
def relatorio_pequim(horario: int) -> None:
    r = REDES["pequim"]
    G = grafo_networkx(r["grafo"])
    o, d = r["origem_demo"], r["destino_demo"]
    sp = nx.shortest_path(G, o, d, weight="weight")
    n_arestas = len(sp) - 1
    todos = caminhos_simples_distintos(G, o, d, max_caminhos=20)
    print(f"\n=== {r['titulo']} ===")
    print(r["notas"])
    print(f"Menor caminho {o} → {d}: {n_arestas} trechos | {' → '.join(sp)}")
    print(f"Caminhos simples distintos (amostra): {len(todos)}")
    for i, p in enumerate(todos[:5], 1):
        print(f"  {i}. ({len(p) - 1} trechos) {' → '.join(p)}")
    print(f"Custo memoizado (horário {horario}): {menor_custo('pequim', o, d, horario, frozenset()):.2f}")

"""Printar diferentes relatorios"""
def relatorio_bart(horario: int) -> None:
    r = REDES["bart"]
    G = grafo_networkx(r["grafo"])
    o, d = r["origem_demo"], r["destino_demo"]
    sp = nx.shortest_path(G, o, d, weight="weight")
    print(f"\n=== {r['titulo']} ===")
    print(r["notas"])
    print(f"Menor caminho {o} → {d}: {' → '.join(sp)}")
    # Bifurcações: nós com grau ≥ 3 no subgrafo relevante
    hubs = [n for n in G.nodes if G.degree(n) >= 3]
    print(f"Estações com bifurcação (grau ≥ 3): {', '.join(sorted(hubs))}")
    print(f"Custo memoizado: {menor_custo('bart', o, d, horario, frozenset()):.2f}")

"""Printar diferentes relatorios"""
def relatorio_sao_paulo(horario: int) -> None:
    r = REDES["sao_paulo"]
    G = grafo_networkx(r["grafo"])
    o, d = r["origem_demo"], r["destino_demo"]
    sp = nx.shortest_path(G, o, d, weight="weight")
    integracoes = {"Luz", "Hospital São Paulo"}
    passa = [s for s in sp if s in integracoes]
    print(f"\n=== {r['titulo']} ===")
    print(r["notas"])
    print(f"Menor caminho {o} → {d}: {' → '.join(sp)}")
    print(f"Estações de integração no percurso: {', '.join(passa) if passa else '(nenhuma — revisar grafo)'}")
    print(f"Custo memoizado: {menor_custo('sao_paulo', o, d, horario, frozenset()):.2f}")