from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import callback

import dash_bootstrap_components as dbc

import plotly.express as px

import pandas as pd

import random

# =========================
# LAYOUT
# =========================

def layout():

    # =========================
    # DADOS
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

    df = pd.DataFrame({

        "hora": horas,
        "trafego": trafego

    })

    fig = px.line(

        df,

        x="hora",

        y="trafego",

        template="plotly_dark",

        markers=True

    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="📈 Tráfego de Rede",

        title_x=0.5

    )

    return html.Div([

        # =========================
        # INTERVAL
        # =========================

        dcc.Interval(

            id="interval-dashboard",

            interval=3000,

            n_intervals=0

        ),

        # =========================
        # TITLE
        # =========================

        html.H1(

            "📡 FiberFlow Dashboard",

            style={

                "color": "white",

                "marginBottom": "30px"

            }

        ),

        # =========================
        # KPI
        # =========================

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("👥 Clientes"),

                        html.H2("1.248")

                    ])

                ],

                color="primary",

                inverse=True)

            ],

            md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("🚨 Chamados"),

                        html.H2("18")

                    ])

                ],

                color="danger",

                inverse=True)

            ],

            md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("📡 Uptime"),

                        html.H2("99.9%")

                    ])

                ],

                color="success",

                inverse=True)

            ],

            md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4("⚡ Ping"),

                        html.H2("12ms")

                    ])

                ],

                color="warning",

                inverse=True)

            ],

            md=3)

        ],

        className="mb-4"),

        # =========================
        # ALERTA
        # =========================

        dbc.Alert(

            "🚨 ALERTA: Oscilação detectada em Osasco/SP",

            color="danger",

            style={

                "animation": "blinker 1s linear infinite",

                "fontWeight": "bold",

                "fontSize": "18px"

            },

            className="mb-4"

        ),

        # =========================
        # ROW CENTRAL
        # =========================

        dbc.Row([

            # =========================
            # GRAFICO
            # =========================

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        dcc.Graph(

                            id="grafico-dashboard",

                            figure=fig

                        )

                    ])

                ])

            ],

            md=8),

            # =========================
            # LOGS
            # =========================

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4(

                            "🚨 Logs RealTime",

                            className="mb-4"

                        ),

                        html.Div(

                            id="logs-dashboard"

                        )

                    ])

                ])

            ],

            md=4)

        ])

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

    Output("grafico-dashboard", "figure"),
    Output("logs-dashboard", "children"),

    Input("interval-dashboard", "n_intervals")

)

def atualizar_dashboard(n):

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

    df = pd.DataFrame({

        "hora": horas,
        "trafego": trafego

    })

    fig = px.line(

        df,

        x="hora",

        y="trafego",

        template="plotly_dark",

        markers=True

    )

    fig.update_layout(

        paper_bgcolor="#0f172a",

        plot_bgcolor="#0f172a",

        font_color="white",

        title="📈 Tráfego de Rede",

        title_x=0.5

    )

    logs = [

        "🚨 ONU offline Campinas",
        "📡 Latência alta São Paulo",
        "🟢 Cliente reconectado",
        "⚠️ Pico de tráfego Curitiba",
        "🔧 Técnico enviado Osasco"

    ]

    logs_ui = [

        dbc.Alert(

            random.choice(logs),

            color=random.choice([

                "danger",
                "warning",
                "success",
                "primary"

            ]),

            className="mb-2"

        )

        for _ in range(5)

    ]

    return (

        fig,

        logs_ui

    )