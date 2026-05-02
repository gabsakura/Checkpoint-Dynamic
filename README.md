# Dynamic Programming - Sistema de Rotas para o Metrô

## 🧠 1. Descrição

Este projeto consiste no desenvolvimento de um **sistema de rotas para metrôs** utilizando **Python e Programação Dinâmica**, modelando redes urbanas como **grafos ponderados**. 

A aplicação calcula o **menor caminho (com memoização)** e o **maior caminho simples (com backtracking)** entre estações, considerando **variações de custo por horário** (bônus e penalidades). 

O objetivo é explorar conceitos como:

* Grafos e algoritmos de busca
* Recursão com memoização
* Análise de desempenho (tempo e memória)
* Simulação de cenários reais de mobilidade urbana 

---

## 🧱 2. Estrutura do Projeto

```
Checkpoint_2_em_grupo/
├── src/
│   ├── graphs/                     # Definição dos grafos
│   │   └── redes.py
│   │
│   ├── algorithms/                 # Lógica dos algoritmos
│   │   └── rotas.py
│   │
│   ├── visualization/              # Mapas e gráficos
│   │   └── grafos_e_mapas.py
│   │
│   ├── services/                   # Relatórios
│   │   └── relatorios.py
|   |
│   ├── main.py                     # Orquestra tudo
│   │
│   └── data/
│   │   └── outputs/                # Só arquivos gerados
│   │      ├── metro_grafo_*.png
│   │      └── metro_mapa_*.html
│
├── .gitignore
├── notebook.ipynb
├── README.md
└── requirements.txt
```

---

## ▶️ 3. Como executar

1. Clone o repositório:

```bash
git clone https://github.com/1IMperaDOR0/Checkpoint_2_em_grupo
```

2. Acesse a pasta do projeto:

```bash
cd Checkpoint_2_em_grupo
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o programa:

```bash
python -m src.main
```

---

## 👥 Integrantes

| Nome                                  | RM     |
|---------------------------------------|--------|
| Gabriel Alexandre Fukushima Sakura    | 99522  |
| Henrique de Oliveira Gomes            | 566424 |
| Henrique Kolomyes Silveira            | 563467 |
| Lucas Henrique Viana Estevam Sena     | 566246 |
| Matheus Santos de Oliveira            | 561982 |

---

## 📜 Licença

Este projeto é de uso acadêmico e educacional.