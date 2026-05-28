from dash import html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

# =========================
# FUNÇÃO
# =========================

def layout(estado=None):

    # =========================
    # DADOS
    # =========================

    df = pd.read_csv("data/clientes.csv")

    # FILTRO

    if estado:

        df = df[
            df["estado"] == estado
        ]

    # =========================
    # KPIS
    # =========================

    total_clientes = len(df)

    ticket_medio = round(
        df["mensalidade"].mean(),
        0
    )

    cidades = df["cidade"].nunique()

    planos = df["plano"].nunique()

    # =========================
    # GRÁFICO CIDADES
    # =========================

    top_cidades = (
        df["cidade"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    top_cidades.columns = [
        "cidade",
        "clientes"
    ]

    grafico_cidades = px.bar(

        top_cidades,

        x="cidade",
        y="clientes",

        color="clientes",

        text_auto=True,

        template="plotly_dark"
    )

    grafico_cidades.update_layout(

        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",

        font_color="white",

        title="Top 10 Cidades",

        title_x=0.5
    )

    # =========================
    # GRÁFICO PLANOS
    # =========================

    grafico_planos = px.pie(

        df,

        names="plano",

        hole=0.5,

        template="plotly_dark"
    )

    grafico_planos.update_layout(

        paper_bgcolor="#0f172a",

        font_color="white",

        title="Distribuição de Planos",

        title_x=0.5
    )

    # =========================
    # LAYOUT
    # =========================

    return html.Div([

        html.H1(
            "Clientes",
            className="title-main"
        ),

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Clientes"),

                        html.H2(
                            total_clientes,
                            className="text-info"
                        )

                    ])

                ],
                className="card-style")

            ], md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Ticket Médio"),

                        html.H2(
                            f"R$ {ticket_medio}",
                            className="text-success"
                        )

                    ])

                ],
                className="card-style")

            ], md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Cidades"),

                        html.H2(
                            cidades,
                            className="text-warning"
                        )

                    ])

                ],
                className="card-style")

            ], md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H5("Planos"),

                        html.H2(
                            planos,
                            className="text-danger"
                        )

                    ])

                ],
                className="card-style")

            ], md=3),

        ], className="mb-4"),

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        dcc.Graph(
                            figure=grafico_cidades
                        )

                    ])

                ],
                className="card-style")

            ], md=8),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        dcc.Graph(
                            figure=grafico_planos
                        )

                    ])

                ],
                className="card-style")

            ], md=4),

        ])

    ])