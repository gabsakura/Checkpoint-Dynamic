from __future__ import annotations

import time
import tracemalloc

"""Importando as funções de rotas.py"""
from src.algorithms.rotas import(
    menor_custo,
    grafo_networkx,
    fator_horario,
    maior_caminho_simples,
    limpar_cache_menor_custo
)

"""Importando as funções de grafos_e_mapas.py"""
from src.visualization.grafos_e_mapas import(
    plot_matplotlib_rede,
    mapa_folium_rede
)

from src.services.relatorios import(
    relatorio_pequim,
    relatorio_bart,
    relatorio_sao_paulo,
    REDES
)

"""uso de grafoskkkkk não entendi muito certinho como funciona"""
import networkx as nx

def ler_horario() -> int:
    while True:
        try:
            h = int(input("Digite a hora (0-23): "))
            if 0 <= h <= 23:
                return h
            print("Hora inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def escolher_rede() -> str:
    redes_disponiveis = list(REDES.keys())

    while True:
        print("\nRedes disponíveis:")
        for r in redes_disponiveis:
            print(f"- {r}")
        escolha = input("Escolha a rede: ").strip().lower()
        if escolha in redes_disponiveis:
            return escolha
        else:
            print("❌ Rede inválida. Tente novamente.")

def escolher_estacoes(rede_id: str) -> tuple[str, str]:
    estacoes = list(REDES[rede_id]["grafo"].keys())

    while True:
        print("\nEstações disponíveis:")
        print(", ".join(estacoes))
        origem = input("Origem: ").strip()
        destino = input("Destino: ").strip()
        if origem not in estacoes:
            print("❌ Origem inválida.")
            continue
        if destino not in estacoes:
            print("❌ Destino inválido.")
            continue
        if origem == destino:
            print("❌ Origem e destino não podem ser iguais.")
            continue
        return origem, destino

"Mudar o horario para o horario desejado"
"""def main() -> None:
    horario = 18
    limpar_cache_menor_custo()

    relatorio_pequim(horario)
    plot_matplotlib_rede("pequim", caminho_destaque=nx.shortest_path(
        grafo_networkx(REDES["pequim"]["grafo"]),
        REDES["pequim"]["origem_demo"],
        REDES["pequim"]["destino_demo"],
        weight="weight",
    ))
    mapa_folium_rede(
        "pequim",
        nx.shortest_path(
            grafo_networkx(REDES["pequim"]["grafo"]),
            REDES["pequim"]["origem_demo"],
            REDES["pequim"]["destino_demo"],
            weight="weight",
        ),
    )

    relatorio_bart(horario)
    plot_matplotlib_rede(
        "bart",
        caminho_destaque=nx.shortest_path(
            grafo_networkx(REDES["bart"]["grafo"]),
            REDES["bart"]["origem_demo"],
            REDES["bart"]["destino_demo"],
            weight="weight",
        ),
    )
    mapa_folium_rede(
        "bart",
        nx.shortest_path(
            grafo_networkx(REDES["bart"]["grafo"]),
            REDES["bart"]["origem_demo"],
            REDES["bart"]["destino_demo"],
            weight="weight",
        ),
    )

    relatorio_sao_paulo(horario)
    plot_matplotlib_rede(
        "sao_paulo",
        caminho_destaque=nx.shortest_path(
            grafo_networkx(REDES["sao_paulo"]["grafo"]),
            REDES["sao_paulo"]["origem_demo"],
            REDES["sao_paulo"]["destino_demo"],
            weight="weight",
        ),
    )
    mapa_folium_rede(
        "sao_paulo",
        nx.shortest_path(
            grafo_networkx(REDES["sao_paulo"]["grafo"]),
            REDES["sao_paulo"]["origem_demo"],
            REDES["sao_paulo"]["destino_demo"],
            weight="weight",
        ),
    )

    print("\n--- Amostra: pares na rede SP (3 primeiros) ---")
    for item in sugestoes_todas_pares("sao_paulo", horario)[:3]:
        o, d, custo, caminho = item
        print(f"  {o} -> {d}: custo ~ {custo:.2f} | {' -> '.join(caminho)}")

    tracemalloc.start()
    t0 = time.perf_counter()
    _ = menor_custo("sao_paulo", "Tucuruvi", "Capão Redondo", horario, frozenset())
    t1 = time.perf_counter()
    mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(
        f"\nChamada memoizada Tucuruvi->Capão Redondo: {t1 - t0:.6f}s | pico mem: {mem[1] / 1024:.1f} KB"
    )
    print(f"Cache LRU: {menor_custo.cache_info()}")"""

"""Agora não tem mais horário fixo e é mais interativo"""
def main():
    limpar_cache_menor_custo()
    rede = escolher_rede()
    horario = ler_horario()
    origem, destino = escolher_estacoes(rede)
    G = grafo_networkx(REDES[rede]["grafo"])
    if not nx.has_path(G, origem, destino):
        print("❌ Não existe caminho entre essas estações.")
        return
    print("\n" + "="*50)

    # Menor caminho
    caminho = nx.shortest_path(G, origem, destino, weight="weight")
    print(f"Melhor caminho: {' -> '.join(caminho)}")
    print(f"Trechos: {len(caminho) - 1}")

    # SEM cache
    limpar_cache_menor_custo()
    t0 = time.perf_counter()
    custo1 = menor_custo(rede, origem, destino, horario, frozenset())
    t1 = time.perf_counter()

    # COM cache (primeira chamada ainda popula)
    t2 = time.perf_counter()
    custo2 = menor_custo(rede, origem, destino, horario, frozenset())
    t3 = time.perf_counter()

    # COM cache REAL (já armazenado)
    t4 = time.perf_counter()
    custo3 = menor_custo(rede, origem, destino, horario, frozenset())
    t5 = time.perf_counter()

    tracemalloc.start()
    _ = menor_custo(rede, origem, destino, horario, frozenset())
    mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()


    fator = fator_horario(horario)
    print(f"Custo SEM cache: {custo1:.2f}")
    print(f"Custo COM cache (1ª): {custo2:.2f}")
    print(f"Custo COM cache (2ª): {custo3:.2f}")
    print(f"Fator de horário: x{fator}")
    print(f"Tempo SEM cache: {t1 - t0:.6f}s")
    print(f"Tempo COM cache (1ª): {t3 - t2:.6f}s")
    print(f"Tempo COM cache (2ª): {t5 - t4:.6f}s")
    print(f"Memória pico: {mem[1] / 1024:.2f} KB")

    # Maior caminho
    custo_max, caminho_max = maior_caminho_simples(rede, origem, destino)
    print()
    print("Maior caminho simples:")
    print(f"{' -> '.join(caminho_max)}")
    print(f"Custo: {custo_max:.2f}")
    print("="*50)
    print()
    plot_matplotlib_rede(rede, caminho_destaque=caminho)
    mapa_folium_rede(rede, caminho)

if __name__ == "__main__":
    main()