from dash import html
from dash import dcc

import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

import random

# =========================
# LAYOUT
# =========================

def layout():

    # =========================
    # DADOS
    # =========================

    df = pd.read_csv(
        "data/clientes.csv"
    )

    # =========================
    # ESTADOS
    # =========================

    estados = (

        df["estado"]

        .value_counts()

        .reset_index()

    )

    estados.columns = [
        "estado",
        "clientes"
    ]

    # =========================
    # COORDENADAS
    # =========================

    coordenadas = {

        "SP": [-23.5505, -46.6333],
        "RJ": [-22.9068, -43.1729],
        "MG": [-19.9167, -43.9345],
        "PR": [-25.4284, -49.2733],
        "RS": [-30.0346, -51.2177],
        "BA": [-12.9714, -38.5014],
        "PE": [-8.0476, -34.8770],
        "CE": [-3.7319, -38.5267]

    }

    estados["lat"] = estados["estado"].map(
        lambda x: coordenadas[x][0]
    )

    estados["lon"] = estados["estado"].map(
        lambda x: coordenadas[x][1]
    )

    # =========================
    # HEATMAP VALUE
    # =========================

    estados["intensidade"] = [

        random.randint(20, 100)

        for _ in range(len(estados))

    ]

    # =========================
    # MAPA HEATMAP
    # =========================

    fig = px.density_mapbox(

        estados,

        lat="lat",

        lon="lon",

        z="intensidade",

        radius=40,

        zoom=3,

        center=dict(
            lat=-15,
            lon=-50
        ),

        height=750,

        mapbox_style="carto-darkmatter",

        hover_name="estado",

        hover_data={

            "clientes": True,
            "intensidade": True

        }

    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        margin=dict(
            l=0,
            r=0,
            t=50,
            b=0
        ),

        title="🌡️ Heatmap Telecom Brasil",

        title_x=0.5
    )

    # =========================
    # KPI CARDS
    # =========================

    cards = dbc.Row([

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H5(
                        "Estados Monitorados"
                    ),

                    html.H2(
                        len(estados),
                        className="text-info"
                    )

                ])

            ],
            className="card-style")

        ], md=3),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H5(
                        "Clientes"
                    ),

                    html.H2(
                        len(df),
                        className="text-success"
                    )

                ])

            ],
            className="card-style")

        ], md=3),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H5(
                        "Regiões Críticas"
                    ),

                    html.H2(
                        "5",
                        className="text-danger"
                    )

                ])

            ],
            className="card-style")

        ], md=3),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H5(
                        "Falhas 24h"
                    ),

                    html.H2(
                        "18",
                        className="text-warning"
                    )

                ])

            ],
            className="card-style")

        ], md=3),

    ], className="mb-4")

    # =========================
    # LAYOUT
    # =========================

    return html.Div([

        html.H1(

            "🌎 Telecom Heatmap",

            className="title-main"

        ),

        cards,

        dbc.Card([

            dbc.CardBody([

                dcc.Graph(
                    figure=fig
                )

            ])

        ],
        className="card-style")

    ])