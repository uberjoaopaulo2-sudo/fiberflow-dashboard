from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

# =========================
# FUNÇÃO
# =========================

def layout():

    # =========================
    # DADOS
    # =========================

    df = pd.read_csv("data/vendas.csv")

    # =========================
    # KPIS
    # =========================

    total_vendas = int(df["vendas"].sum())

    media_vendas = int(df["vendas"].mean())

    maior_venda = int(df["vendas"].max())

    # =========================
    # GRÁFICO
    # =========================

    grafico = px.line(

        df,

        x="data",

        y="vendas",

        template="plotly_dark"
    )

    grafico.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="Vendas Últimos 365 Dias",

        title_x=0.5
    )

    # =========================
    # LAYOUT
    # =========================

    return html.Div([

        html.H1(
            "Vendas",
            className="title-main"
        ),

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Total Vendas"),

                        html.H2(
                            f"R$ {total_vendas}",
                            className="text-success"
                        )

                    ])

                ],
                className="card-style")

            ], md=4),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Média"),

                        html.H2(
                            f"R$ {media_vendas}",
                            className="text-info"
                        )

                    ])

                ],
                className="card-style")

            ], md=4),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Maior Venda"),

                        html.H2(
                            f"R$ {maior_venda}",
                            className="text-warning"
                        )

                    ])

                ],
                className="card-style")

            ], md=4),

        ], className="mb-4"),

        dbc.Card([

            dbc.CardBody([

                dcc.Graph(
                    figure=grafico
                )

            ])

        ],
        className="card-style")

    ])