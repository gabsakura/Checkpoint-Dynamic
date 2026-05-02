from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx
import folium

from src.graphs.redes import REDES
from src.algorithms.rotas import grafo_networkx

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "src" / "data" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

"""famoso matplotlib pra fazer os diagramas dos grafos"""
def plot_matplotlib_rede(
    rede_id: str,
    caminho_destaque: list[str] | None = None,
    arquivo: str | None = None,
) -> Path:
    r = REDES[rede_id]
    G = grafo_networkx(r["grafo"])
    pos = nx.spring_layout(G, seed=42, k=2.0 / max(1, len(G) ** 0.5))
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_color="#1a5276", node_size=900)
    nx.draw_networkx_labels(G, pos, font_size=7, font_color="white")
    arestas = list(G.edges())
    cores: list[str] = []
    larguras: list[float] = []
    if caminho_destaque and len(caminho_destaque) >= 2:
        pares = set(zip(caminho_destaque[:-1], caminho_destaque[1:]))
        pares |= {(b, a) for (a, b) in pares}

        for u, v in arestas:
            if (u, v) in pares or (v, u) in pares:
                cores.append("#e74c3c")
                larguras.append(3.0)
            else:
                cores.append("#bdc3c7")
                larguras.append(1.2)
    else:
        cores = ["#3498db"] * len(arestas)
        larguras = [1.5] * len(arestas)
    nx.draw_networkx_edges(G, pos, edgelist=arestas, edge_color=cores, width=larguras)
    labels = {(u, v): f"{d['weight']:.0f}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)
    plt.title(r["titulo"])
    plt.axis("off")
    plt.tight_layout()
    nome = arquivo or f"metro_grafo_{rede_id}.png"
    out = OUTPUT_DIR / nome
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Figura salva em: {out}")
    return out

"""folium para criar os mapas da vida real"""
def mapa_folium_rede(
    rede_id: str, caminho: list[str], arquivo: str | None = None
) -> Path | None:
    r = REDES[rede_id]
    coords = r["coords"]
    if not caminho:
        return None
    lats = [coords[s][0] for s in caminho if s in coords]
    lons = [coords[s][1] for s in caminho if s in coords]
    if not lats:
        return None
    centro = (sum(lats) / len(lats), sum(lons) / len(lons))
    m = folium.Map(location=centro, zoom_start=12, tiles="OpenStreetMap")
    folium.PolyLine(
        locations=[(lat, lon) for lat, lon in zip(lats, lons)],
        color="red",
        weight=5,
        opacity=0.8,
    ).add_to(m)
    for nome in caminho:
        if nome not in coords:
            continue
        lat, lon = coords[nome]
        folium.Marker([lat, lon], popup=nome, tooltip=nome).add_to(m)
    nome_arq = arquivo or f"metro_mapa_{rede_id}.html"
    path = OUTPUT_DIR / nome_arq
    m.save(str(path))
    print(f"Mapa salvo em: {path}")
    return path