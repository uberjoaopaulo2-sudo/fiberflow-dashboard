from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import callback

import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

import random

from datetime import datetime

# =========================
# LAYOUT
# =========================

def layout():

    df = pd.read_csv(
        "data/clientes.csv"
    )

    horario = datetime.now().strftime(
        "%H:%M:%S"
    )

    # =========================
    # DADOS INICIAIS
    # =========================

    cidades = (

        df["cidade"]

        .value_counts()

        .head(10)

        .reset_index()

    )

    cidades.columns = [
        "cidade",
        "clientes"
    ]

    # =========================
    # BAR CHART
    # =========================

    fig = px.bar(

        cidades,

        x="cidade",

        y="clientes",

        template="plotly_dark",

        color="clientes",

        text_auto=True

    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="Clientes Online por Cidade",

        title_x=0.5

    )

    # =========================
    # LINE CHART
    # =========================

    horas = [

        "08h",
        "09h",
        "10h",
        "11h",
        "12h",
        "13h",
        "14h",
        "15h"

    ]

    trafego = [

        random.randint(40, 100)

        for _ in horas

    ]

    df_line = pd.DataFrame({

        "hora": horas,
        "trafego": trafego

    })

    fig_line = px.line(

        df_line,

        x="hora",

        y="trafego",

        template="plotly_dark",

        markers=True

    )

    fig_line.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="📈 Tráfego de Rede em Tempo Real",

        title_x=0.5

    )

    # =========================
    # LAYOUT
    # =========================

    return html.Div([

        # =========================
        # INTERVAL REALTIME
        # =========================

        dcc.Interval(

            id="intervalo-realtime",

            interval=3000,

            n_intervals=0

        ),

        # =========================
        # TOAST
        # =========================

        dbc.Toast(

            id="toast-alerta",

            header="🚨 Alerta Telecom",

            is_open=True,

            dismissable=True,

            duration=4000,

            icon="danger",

            style={

                "position": "fixed",

                "top": 20,

                "right": 20,

                "width": 350,

                "zIndex": 9999

            }

        ),

        # =========================
        # STATUS BAR
        # =========================

        html.Div([

            html.Div([

                html.Span(
                    "🟢 Sistema Operacional"
                )

            ]),

            html.Div(
                f"Última atualização: {horario}"
            )

        ],

        style={

            "display": "flex",

            "justifyContent": "space-between",

            "marginBottom": "20px",

            "color": "white"

        }),

        # =========================
        # TITLE
        # =========================

        html.H1(

            "📊 Telecom Analytics",

            style={

                "color": "white",

                "marginBottom": "30px"

            }

        ),

        # =========================
        # KPI CARDS
        # =========================

        dbc.Row([

            # CLIENTES

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H6(
                            "Clientes"
                        ),

                        html.H2(

                            "3000",

                            id="clientes-kpi",

                            className="text-info"

                        )

                    ])

                ],

                className="shadow-lg")

            ], md=3),

            # RECEITA

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H6(
                            "Receita"
                        ),

                        html.H2(

                            "R$ 450000",

                            id="receita-kpi",

                            className="text-success"

                        )

                    ])

                ],

                className="shadow-lg")

            ], md=3),

            # UPTIME

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H6(
                            "Uptime"
                        ),

                        html.H2(

                            "99.98%",

                            id="uptime-kpi",

                            className="text-warning"

                        )

                    ])

                ],

                className="shadow-lg")

            ], md=3),

            # CHAMADOS

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H6(
                            "Chamados"
                        ),

                        html.H2(

                            "143",

                            id="chamados-kpi",

                            className="text-danger"

                        )

                    ])

                ],

                className="shadow-lg")

            ], md=3),

        ],

        className="g-4"),

        html.Br(),

        # =========================
        # ALERTA
        # =========================

        html.Div(

            id="alerta-rede",

            style={

                "animation": "pulse 2s infinite"

            }

        ),

        html.Br(),

        # =========================
        # GRÁFICOS
        # =========================

        dbc.Card([

            dbc.CardBody([

                dcc.Graph(

                    id="grafico-realtime",

                    figure=fig

                ),

                html.Br(),

                dcc.Graph(

                    id="grafico-linha",

                    figure=fig_line

                )

            ])

        ],

        className="shadow-lg"),

        html.Br(),

        # =========================
        # REDE
        # =========================

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4(
                            "📡 Rede Telecom"
                        ),

                        html.P(
                            "18 falhas nas últimas 24h."
                        ),

                        html.P(
                            "Latência média: 12ms"
                        ),

                        html.P(
                            "5 regiões críticas."
                        )

                    ])

                ],

                className="shadow-lg")

            ], md=6),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4(
                            "🌎 Infraestrutura"
                        ),

                        html.P(
                            "42 torres monitoradas."
                        ),

                        html.P(
                            "97% SLA."
                        ),

                        html.P(
                            "2 regiões instáveis."
                        )

                    ])

                ],

                className="shadow-lg")

            ], md=6)

        ])

    ],

    style={

        "backgroundColor": "#0f172a",

        "minHeight": "100vh",

        "padding": "20px"

    })

# =========================
# CALLBACK REALTIME
# =========================

@callback(

    Output("clientes-kpi", "children"),
    Output("receita-kpi", "children"),
    Output("uptime-kpi", "children"),
    Output("chamados-kpi", "children"),
    Output("grafico-realtime", "figure"),
    Output("grafico-linha", "figure"),
    Output("alerta-rede", "children"),
    Output("toast-alerta", "children"),

    Input("intervalo-realtime", "n_intervals")

)

def atualizar_dashboard(n):

    # =========================
    # KPIS
    # =========================

    clientes = random.randint(
        2800,
        3200
    )

    receita = random.randint(
        400000,
        500000
    )

    uptime = round(

        random.uniform(
            99.10,
            99.99
        ),

        2

    )

    chamados = random.randint(
        80,
        180
    )

    # =========================
    # STATUS
    # =========================

    if chamados > 150:

        status_color = "danger"

        status_text = "CRÍTICO"

    elif chamados > 110:

        status_color = "warning"

        status_text = "ATENÇÃO"

    else:

        status_color = "success"

        status_text = "ESTÁVEL"

    # =========================
    # BAR CHART REALTIME
    # =========================

    cidades = [

        "Campinas",
        "São Paulo",
        "Osasco",
        "Curitiba",
        "Fortaleza",
        "Jundiaí",
        "Sumaré",
        "Sorocaba"

    ]

    valores = [

        random.randint(50, 300)

        for _ in cidades

    ]

    df = pd.DataFrame({

        "cidade": cidades,
        "clientes": valores

    })

    fig = px.bar(

        df,

        x="cidade",

        y="clientes",

        template="plotly_dark",

        color="clientes",

        text_auto=True

    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="Clientes Online por Cidade",

        title_x=0.5

    )

    # =========================
    # LINE CHART REALTIME
    # =========================

    horas = [

        "08h",
        "09h",
        "10h",
        "11h",
        "12h",
        "13h",
        "14h",
        "15h"

    ]

    trafego = [

        random.randint(40, 100)

        for _ in horas

    ]

    df_line = pd.DataFrame({

        "hora": horas,
        "trafego": trafego

    })

    fig_line = px.line(

        df_line,

        x="hora",

        y="trafego",

        template="plotly_dark",

        markers=True

    )

    fig_line.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="📈 Tráfego de Rede em Tempo Real",

        title_x=0.5

    )

    # =========================
    # ALERTAS
    # =========================

    alertas = [

        "🚨 Fibra rompida em Campinas/SP",
        "⚠️ Alta latência em Osasco/SP",
        "🔴 Região crítica em Curitiba/PR",
        "🚨 ONU offline em Fortaleza/CE",
        "⚠️ Instabilidade em São Paulo/SP"

    ]

    alerta = random.choice(
        alertas
    )

    alerta_box = dbc.Alert(

        [

            html.H4(
                f"STATUS: {status_text}"
            ),

            html.Hr(),

            html.P(alerta)

        ],

        color=status_color,

        className="shadow-lg"

    )

    return (

        f"{clientes}",

        f"R$ {receita}",

        f"{uptime}%",

        f"{chamados}",

        fig,

        fig_line,

        alerta_box,

        alerta

    )