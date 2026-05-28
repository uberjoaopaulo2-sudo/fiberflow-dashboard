from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import callback

import dash_bootstrap_components as dbc

import pandas as pd

import random

# =========================
# LAYOUT
# =========================

def layout():

    return html.Div([

        # =========================
        # INTERVAL
        # =========================

        dcc.Interval(

            id="interval-clientes",

            interval=3000,

            n_intervals=0

        ),

        # =========================
        # TITLE
        # =========================

        html.H1(

            "👥 Clientes FiberFlow",

            style={

                "color": "white",

                "marginBottom": "30px"

            }

        ),

        # =========================
        # KPIS
        # =========================

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("🟢 Online"),

                        html.H2(

                            id="clientes-online"

                        )

                    ])

                ],

                color="success",

                inverse=True)

            ],

            md=4),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("🔴 Offline"),

                        html.H2(

                            id="clientes-offline"

                        )

                    ])

                ],

                color="danger",

                inverse=True)

            ],

            md=4),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("📡 Consumo Médio"),

                        html.H2(

                            id="consumo-medio"

                        )

                    ])

                ],

                color="primary",

                inverse=True)

            ],

            md=4)

        ],

        className="mb-4"),

        # =========================
        # TABELA
        # =========================

        html.Div(

            id="tabela-clientes"

        )

    ],

    style={

        "backgroundColor": "#0f172a",

        "minHeight": "100vh",

        "padding": "20px"

    })

# =========================
# CALLBACK
# =========================

@callback(

    Output("tabela-clientes", "children"),
    Output("clientes-online", "children"),
    Output("clientes-offline", "children"),
    Output("consumo-medio", "children"),

    Input("interval-clientes", "n_intervals")

)

def atualizar_tabela(n):

    nomes = [

        "Carlos",
        "Bruno",
        "Amanda",
        "Fernanda",
        "João",
        "Lucas",
        "Mariana",
        "Patricia"

    ]

    cidades = [

        "Campinas/SP",
        "São Paulo/SP",
        "Osasco/SP",
        "Curitiba/PR",
        "Fortaleza/CE"

    ]

    planos = [

        "300MB",
        "500MB",
        "700MB",
        "1GB"

    ]

    dados = []

    online = 0
    offline = 0

    consumos = []

    # =========================
    # LOOP
    # =========================

    for i in range(15):

        status = random.choice([

            "🟢 Online",
            "🔴 Offline"

        ])

        consumo = random.randint(

            50,
            900

        )

        consumos.append(consumo)

        if "Online" in status:

            online += 1

        else:

            offline += 1

        dados.append({

            "Cliente": random.choice(nomes),

            "Cidade": random.choice(cidades),

            "Plano": random.choice(planos),

            "Consumo": f"{consumo} GB",

            "Status": status

        })

    # =========================
    # DATAFRAME
    # =========================

    df = pd.DataFrame(dados)

    tabela = dbc.Table.from_dataframe(

        df,

        striped=True,

        bordered=True,

        hover=True,

        dark=True,

        responsive=True

    )

    consumo_medio = int(

        sum(consumos) / len(consumos)

    )

    return (

        dbc.Card([

            dbc.CardBody([

                tabela

            ])

        ],

        className="shadow-lg"),

        online,

        offline,

        f"{consumo_medio} GB"

    )