import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

clientes = []
vendas = []

# =========================
# ESTADOS
# =========================

estados = {

    "SP": {
        "cidade": "São Paulo",
        "lat": -23.5505,
        "lon": -46.6333
    },

    "RJ": {
        "cidade": "Rio de Janeiro",
        "lat": -22.9068,
        "lon": -43.1729
    },

    "MG": {
        "cidade": "Belo Horizonte",
        "lat": -19.9167,
        "lon": -43.9345
    },

    "PR": {
        "cidade": "Curitiba",
        "lat": -25.4284,
        "lon": -49.2733
    },

    "BA": {
        "cidade": "Salvador",
        "lat": -12.9714,
        "lon": -38.5014
    },

    "PE": {
        "cidade": "Recife",
        "lat": -8.0476,
        "lon": -34.8770
    },

    "CE": {
        "cidade": "Fortaleza",
        "lat": -3.7319,
        "lon": -38.5267
    }

}

planos = [
    "100MB",
    "300MB",
    "500MB",
    "1GB"
]

# =========================
# CLIENTES
# =========================

for i in range(3000):

    estado = random.choice(list(estados.keys()))

    plano = random.choice(planos)

    valor = {

        "100MB": 99,
        "300MB": 129,
        "500MB": 159,
        "1GB": 199

    }[plano]

    clientes.append({

        "nome": fake.name(),

        "estado": estado,

        "cidade": estados[estado]["cidade"],

        "lat": estados[estado]["lat"],

        "lon": estados[estado]["lon"],

        "plano": plano,

        "mensalidade": valor

    })

# =========================
# VENDAS
# =========================

for i in range(365):

    vendas.append({

        "data": (
            datetime.now() - timedelta(days=365-i)
        ).strftime("%Y-%m-%d"),

        "vendas": random.randint(10, 100)

    })

# =========================
# DATAFRAMES
# =========================

df_clientes = pd.DataFrame(clientes)
df_vendas = pd.DataFrame(vendas)

# =========================
# EXPORTAR
# =========================

df_clientes.to_csv(
    "data/clientes.csv",
    index=False
)

df_vendas.to_csv(
    "data/vendas.csv",
    index=False
)
# =========================
# HEATMAP
# =========================

heatmap = []

for hora in range(24):

    for dia in [

        "Seg",
        "Ter",
        "Qua",
        "Qui",
        "Sex",
        "Sab",
        "Dom"

    ]:

        heatmap.append({

            "hora": hora,

            "dia": dia,

            "problemas": random.randint(0, 100)

        })

df_heatmap = pd.DataFrame(heatmap)

df_heatmap.to_csv(
    "data/heatmap.csv",
    index=False
)
print("Dados gerados com sucesso!")