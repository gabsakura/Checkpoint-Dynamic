from typing import TypedDict

"""estrutura dos dados que usaremos pros metros"""
class RedeMetro(TypedDict):
    id: str
    titulo: str
    grafo: dict[str, list[tuple[str, float]]]
    coords: dict[str, tuple[float, float]]
    origem_demo: str
    destino_demo: str
    notas: str

"""as estruturas de dados de cada metro[Estações visinha, tempo +/- de viagem de cada estação](se houver outra estação tera mais outra tupla)"""
PEQUIM_GRAFO: dict[str, list[tuple[str, float]]] = {
    "Sihui East": [("Sihui", 3.0)],
    "Sihui": [("Sihui East", 3.0), ("Guomao", 3.0)],
    "Guomao": [
        ("Sihui", 3.0),
        ("Jianguomen", 3.0),
        ("Jintaio", 2.5),
    ],
    "Jintaio": [("Guomao", 2.5), ("Tuanjiehu", 2.5)],
    "Tuanjiehu": [("Jintaio", 2.5)],
    "Jianguomen": [("Guomao", 3.0), ("Dongdan", 2.5)],
    "Dongdan": [("Jianguomen", 2.5), ("Xidan", 2.5)],
    "Xidan": [("Dongdan", 2.5), ("Fuxingmen", 2.5), ("Ping'anli", 2.5)],
    "Fuxingmen": [("Xidan", 2.5), ("Chegongzhuang", 2.5)],
    "Chegongzhuang": [("Fuxingmen", 2.5), ("Xizhimen", 2.5)],
    "Ping'anli": [("Xidan", 2.5), ("Xizhimen", 2.5)],
    "Xizhimen": [("Chegongzhuang", 2.5), ("Ping'anli", 2.5)],
}

PEQUIM_COORDS: dict[str, tuple[float, float]] = {
    "Sihui East": (39.9085, 116.5155),
    "Sihui": (39.9077, 116.4965),
    "Guomao": (39.9090, 116.4600),
    "Jintaio": (39.9155, 116.4560),
    "Tuanjiehu": (39.9335, 116.4505),
    "Jianguomen": (39.9087, 116.4355),
    "Dongdan": (39.9140, 116.4175),
    "Xidan": (39.9105, 116.3740),
    "Fuxingmen": (39.9075, 116.3520),
    "Chegongzhuang": (39.9325, 116.3540),
    "Ping'anli": (39.9332, 116.3720),
    "Xizhimen": (39.9402, 116.3555),
}

BART_GRAFO: dict[str, list[tuple[str, float]]] = {
    "Dublin/Pleasanton": [("West Dublin", 3.0)],
    "West Dublin": [("Dublin/Pleasanton", 3.0), ("Castro Valley", 3.0)],
    "Castro Valley": [("West Dublin", 3.0), ("Hayward", 3.0)],
    "Hayward": [
        ("Castro Valley", 3.0),
        ("South Hayward", 3.0),
        ("Bay Fair", 3.0),
    ],
    "South Hayward": [("Hayward", 3.0), ("Union City", 3.0)],
    "Union City": [("South Hayward", 3.0), ("Fremont", 3.0)],
    "Fremont": [
        ("Union City", 3.0),
        ("Warm Springs", 3.0),
    ],
    "Warm Springs": [("Fremont", 3.0), ("Milpitas", 3.0)],
    "Milpitas": [("Warm Springs", 3.0), ("Berryessa", 3.0)],
    "Berryessa": [("Milpitas", 3.0)],
    "Bay Fair": [("Hayward", 3.0), ("San Leandro", 3.0)],
    "San Leandro": [("Bay Fair", 3.0), ("Coliseum", 3.0)],
    "Coliseum": [
        ("San Leandro", 3.0),
        ("Fruitvale", 2.5),
        ("Oakland Airport", 4.0),
    ],
    "Oakland Airport": [("Coliseum", 4.0)],
    "Fruitvale": [("Coliseum", 2.5), ("Lake Merritt", 2.5)],
    "Lake Merritt": [("Fruitvale", 2.5), ("12th St Oakland", 2.5)],
    "12th St Oakland": [("Lake Merritt", 2.5), ("19th St Oakland", 2.0)],
    "19th St Oakland": [("12th St Oakland", 2.0), ("MacArthur", 2.5)],
    "MacArthur": [
        ("19th St Oakland", 2.5),
        ("West Oakland", 2.5),
        ("Rockridge", 3.0),
    ],
    "Rockridge": [("MacArthur", 3.0), ("Orinda", 4.0)],
    "Orinda": [("Rockridge", 4.0)],
    "West Oakland": [("MacArthur", 2.5), ("Embarcadero", 3.5)],
    "Embarcadero": [("West Oakland", 3.5), ("Montgomery", 1.5)],
    "Montgomery": [
        ("Embarcadero", 1.5),
        ("Powell", 1.2),
        ("SFO Airport", 12.0),
    ],
    "Powell": [("Montgomery", 1.2), ("Civic Center", 1.2)],
    "Civic Center": [("Powell", 1.2), ("16th St Mission", 1.5)],
    "16th St Mission": [("Civic Center", 1.5), ("24th St Mission", 1.5)],
    "24th St Mission": [("16th St Mission", 1.5), ("Glen Park", 2.0)],
    "Glen Park": [("24th St Mission", 2.0), ("Balboa Park", 2.0)],
    "Balboa Park": [("Glen Park", 2.0), ("Daly City", 2.5)],
    "Daly City": [("Balboa Park", 2.5), ("Millbrae", 4.0)],
    "SFO Airport": [("Montgomery", 12.0), ("Millbrae", 6.0)],
    "Millbrae": [("Daly City", 4.0), ("SFO Airport", 6.0)],
}

"""desgraça das cordenadas de cada estação de  metro para que o folium funcione (moh desgraçakkkkkkkkkkk)"""
BART_COORDS: dict[str, tuple[float, float]] = {
    "Dublin/Pleasanton": (37.7017, -121.8992),
    "West Dublin": (37.6997, -121.9280),
    "Castro Valley": (37.6907, -122.0758),
    "Hayward": (37.6693, -122.0870),
    "South Hayward": (37.6344, -122.0570),
    "Union City": (37.5902, -122.0170),
    "Fremont": (37.5574, -121.9764),
    "Warm Springs": (37.5022, -121.9394),
    "Milpitas": (37.4103, -121.8910),
    "Berryessa": (37.3686, -121.8747),
    "Bay Fair": (37.6969, -122.1264),
    "San Leandro": (37.7219, -122.1608),
    "Coliseum": (37.7537, -122.1974),
    "Oakland Airport": (37.7131, -122.2122),
    "Fruitvale": (37.7748, -122.2242),
    "Lake Merritt": (37.7975, -122.2654),
    "12th St Oakland": (37.8037, -122.2716),
    "19th St Oakland": (37.8077, -122.2688),
    "MacArthur": (37.8292, -122.2670),
    "Rockridge": (37.8442, -122.2512),
    "Orinda": (37.8824, -122.1838),
    "West Oakland": (37.8049, -122.2951),
    "Embarcadero": (37.7931, -122.3964),
    "Montgomery": (37.7894, -122.4014),
    "Powell": (37.7844, -122.4079),
    "Civic Center": (37.7795, -122.4136),
    "16th St Mission": (37.7651, -122.4196),
    "24th St Mission": (37.7523, -122.4184),
    "Glen Park": (37.7331, -122.4338),
    "Balboa Park": (37.7216, -122.4475),
    "Daly City": (37.7061, -122.4690),
    "SFO Airport": (37.6163, -122.3910),
    "Millbrae": (37.5998, -122.3867),
}

SP_GRAFO: dict[str, list[tuple[str, float]]] = {
    "Tucuruvi": [("Parada Inglesa", 3.0)],
    "Parada Inglesa": [("Tucuruvi", 3.0), ("Jardim São Paulo", 3.0)],
    "Jardim São Paulo": [("Parada Inglesa", 3.0), ("Santana", 3.0)],
    "Santana": [("Jardim São Paulo", 3.0), ("Carandiru", 2.5)],
    "Carandiru": [("Santana", 2.5), ("Portuguesa-Tietê", 2.5)],
    "Portuguesa-Tietê": [("Carandiru", 2.5), ("Armênia", 2.5)],
    "Armênia": [("Portuguesa-Tietê", 2.5), ("Tiradentes", 2.5)],
    "Tiradentes": [("Armênia", 2.5), ("Luz", 2.5)],
    "Luz": [
        ("Tiradentes", 2.5),
        ("São Bento", 2.0),
        ("Brás CPTM", 3.0),
    ],
    "Brás CPTM": [("Luz", 3.0)],
    "São Bento": [("Luz", 2.0), ("Sé", 2.0)],
    "Sé": [("São Bento", 2.0), ("Paraíso", 3.0)],
    "Paraíso": [("Sé", 3.0), ("Vergueiro", 2.0)],
    "Vergueiro": [("Paraíso", 2.0), ("São Joaquim", 2.0)],
    "São Joaquim": [("Vergueiro", 2.0), ("Saúde", 2.0)],
    "Saúde": [("São Joaquim", 2.0), ("São Judas", 2.0)],
    "São Judas": [("Saúde", 2.0), ("Hospital São Paulo", 2.0)],
    "Hospital São Paulo": [
        ("São Judas", 2.0),
        ("Giovanni Gronchi", 3.0),
    ],
    "Giovanni Gronchi": [("Hospital São Paulo", 3.0), ("Santo Amaro", 3.0)],
    "Santo Amaro": [("Giovanni Gronchi", 3.0), ("Largo Treze", 3.0)],
    "Largo Treze": [("Santo Amaro", 3.0), ("Adolfo Pinheiro", 3.0)],
    "Adolfo Pinheiro": [("Largo Treze", 3.0), ("Pedreira", 2.5)],
    "Pedreira": [("Adolfo Pinheiro", 2.5), ("Capão Redondo", 3.0)],
    "Capão Redondo": [("Pedreira", 3.0)],
}

SP_COORDS: dict[str, tuple[float, float]] = {
    "Tucuruvi": (-23.4796, -46.6038),
    "Parada Inglesa": (-23.4827, -46.6085),
    "Jardim São Paulo": (-23.4894, -46.6184),
    "Santana": (-23.4940, -46.6250),
    "Carandiru": (-23.5010, -46.6250),
    "Portuguesa-Tietê": (-23.5080, -46.6250),
    "Armênia": (-23.5150, -46.6260),
    "Tiradentes": (-23.5250, -46.6280),
    "Luz": (-23.5360, -46.6335),
    "Brás CPTM": (-23.5440, -46.6060),
    "São Bento": (-23.5440, -46.6340),
    "Sé": (-23.5500, -46.6330),
    "Paraíso": (-23.5750, -46.6405),
    "Vergueiro": (-23.5800, -46.6420),
    "São Joaquim": (-23.5860, -46.6435),
    "Saúde": (-23.5930, -46.6450),
    "São Judas": (-23.6000, -46.6465),
    "Hospital São Paulo": (-23.6065, -46.6420),
    "Giovanni Gronchi": (-23.6120, -46.6400),
    "Santo Amaro": (-23.6180, -46.6380),
    "Largo Treze": (-23.6250, -46.6360),
    "Adolfo Pinheiro": (-23.6320, -46.6340),
    "Pedreira": (-23.6400, -46.6320),
    "Capão Redondo": (-23.6480, -46.6280),
}

REDES: dict[str, RedeMetro] = {
    "pequim": {
        "id": "pequim",
        "titulo": "Pequim (L1, L2, L4, L10)",
        "grafo": PEQUIM_GRAFO,
        "coords": PEQUIM_COORDS,
        "origem_demo": "Sihui East",
        "destino_demo": "Xizhimen",
        "notas": "Dois caminhos simples distintos via L2 ou L4; trecho L10 a partir de Guomao.",
    },
    "bart": {
        "id": "bart",
        "titulo": "BART (Bay Area)",
        "grafo": BART_GRAFO,
        "coords": BART_COORDS,
        "origem_demo": "Dublin/Pleasanton",
        "destino_demo": "Daly City",
        "notas": "Ramo leste verde (Berryessa), ramo norte amarelo (Orinda), tronco SF e ramos SFO/Millbrae.",
    },
    "sao_paulo": {
        "id": "sao_paulo",
        "titulo": "Metrô + CPTM (São Paulo)",
        "grafo": SP_GRAFO,
        "coords": SP_COORDS,
        "origem_demo": "Tucuruvi",
        "destino_demo": "Capão Redondo",
        "notas": "Integração Luz (CPTM) e Hospital São Paulo (L1/L5).",
    },
}