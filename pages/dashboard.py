from dash import html, dcc
from dash import callback
from dash import Input
from dash import Output
from dash import State

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

    return html.Div([

        # =========================
        # AUTO UPDATE
        # =========================

        dcc.Interval(

            id="interval-update",

            interval=3000,

            n_intervals=0

        ),

        # =========================
        # TOAST ALERT
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
        # MODAL REGIÕES
        # =========================

        dbc.Modal([

            dbc.ModalHeader(

                dbc.ModalTitle(
                    "🚨 Regiões Críticas"
                )

            ),

            dbc.ModalBody([
                html.Hr(),

                html.H5(
                    "Fortaleza/CE"
                ),

                html.P(
                    "Bairro: Aldeota"
                ),

                html.P(
                    "Status: INSTÁVEL"
                ),

                html.P(
                    "Chamados: 27"
                ),

                html.Hr(),

                html.H5(
                    "Belo Horizonte/MG"
                ),

                html.P(
                    "Bairro: Savassi"
                ),

                html.P(
                    "Status: OFFLINE"
                ),

                html.P(
                    "Chamados: 63"
                ),
                html.H5(
                    "Campinas/SP"
                ),

                html.P(
                    "Bairro: Centro"
                ),

                html.P(
                    "Status: OFFLINE"
                ),

                html.P(
                    "Chamados: 48"
                ),

                html.Hr(),

                html.H5(
                    "Osasco/SP"
                ),

                html.P(
                    "Bairro: KM18"
                ),

                html.P(
                    "Status: INSTÁVEL"
                ),

                html.P(
                    "Chamados: 31"
                ),

                html.Hr(),

                html.H5(
                    "Curitiba/PR"
                ),

                html.P(
                    "Bairro: Boqueirão"
                ),

                html.P(
                    "Status: OFFLINE"
                ),

                html.P(
                    "Chamados: 52"
                ),

            ]),

            dbc.ModalFooter(

                dbc.Button(

                    "Fechar",

                    id="fechar-modal",

                    className="ms-auto",

                    n_clicks=0

                )

            ),

        ],

        id="modal-regioes",

        is_open=False),

        # =========================
        # STATUS BAR
        # =========================

        html.Div([

            html.Div([

                html.Span(
                    className="online-dot"
                ),

                html.Span(
                    " Sistema Operacional"
                )

            ]),

            html.Div(
                f"Última atualização: {horario}"
            )

        ],
        className="status-bar"),

        # =========================
        # TÍTULO
        # =========================

        html.H1(

            "ISP Telecom Analytics",

            className="title-main"

        ),

        # =========================
        # FILTRO
        # =========================

        dbc.Row([

            dbc.Col([

                dcc.Dropdown(

                    id="filtro_estado",

                    options=[

                        {
                            "label": i,
                            "value": i
                        }

                        for i in sorted(
                            df["estado"].unique()
                        )

                    ],

                    placeholder="Selecionar Estado",

                    clearable=True

                )

            ], md=4),

        ], className="mb-4"),

        # =========================
        # KPIS
        # =========================

        html.Div(
            id="kpis-dashboard"
        ),

        html.Br(),

        # =========================
        # ALERTA
        # =========================

        html.Div(
            id="alerta-rede"
        ),

        html.Br(),

        # =========================
        # GRÁFICO
        # =========================

        dbc.Card([

            dbc.CardBody([

                dcc.Graph(
                    id="grafico-estados"
                )

            ])

        ],
        className="card-style"),

        html.Br(),

        # =========================
        # ACCORDION
        # =========================

        dbc.Accordion([

            # =========================
            # CLIENTES
            # =========================

            dbc.AccordionItem([

                html.H5(
                    "Clientes Ativos"
                ),

                html.P(
                    "12.482 clientes ativos."
                ),

                html.Hr(),

                html.H5(
                    "Motivos Cancelamento"
                ),

                html.Ul([

                    html.Li(
                        "Concorrência"
                    ),

                    html.Li(
                        "Problemas conexão"
                    ),

                    html.Li(
                        "Mudança cidade"
                    ),

                    html.Li(
                        "Valor alto"
                    ),

                ])

            ],
            title="👥 Clientes"),

            # =========================
            # REDE
            # =========================

            dbc.AccordionItem([

                html.H5(
                    "Rede Telecom"
                ),

                html.P(
                    "18 falhas nas últimas 24h."
                ),

                html.P(
                    "Latência média: 12ms"
                ),

                html.Button(

                    "5 regiões críticas",

                    id="btn-regioes",

                    className="btn btn-danger"

                ),

            ],
            title="📡 Rede"),

            # =========================
            # FINANCEIRO
            # =========================

            dbc.AccordionItem([

                html.H5(
                    "Financeiro"
                ),

                html.P(
                    "Receita mensal: R$ 182K"
                ),

                html.P(
                    "Gastos operacionais: R$ 62K"
                ),

                html.P(
                    "Lucro estimado: R$ 120K"
                )

            ],
            title="💰 Financeiro"),

            # =========================
            # FROTA
            # =========================

            dbc.AccordionItem([

                html.H5(
                    "Frota"
                ),

                html.P(
                    "42 veículos ativos."
                ),

                html.P(
                    "18.420 KM rodados."
                ),

                html.P(
                    "9 manutenções pendentes."
                )

            ],
            title="🚗 Frota"),

        ],
        always_open=True,
        start_collapsed=True)

    ])

# =========================
# CALLBACK DASHBOARD
# =========================

@callback(

    Output(
        "kpis-dashboard",
        "children"
    ),

    Output(
        "grafico-estados",
        "figure"
    ),

    Output(
        "alerta-rede",
        "children"
    ),

    Output(
        "toast-alerta",
        "children"
    ),

    Input(
        "filtro_estado",
        "value"
    ),

    Input(
        "interval-update",
        "n_intervals"
    )

)

def atualizar_dashboard(
    estado,
    n
):

    df = pd.read_csv(
        "data/clientes.csv"
    )

    # =========================
    # FILTRO
    # =========================

    if estado:

        df = df[
            df["estado"] == estado
        ]

    # =========================
    # KPIS
    # =========================

    total_clientes = len(df)

    receita = int(
        df["mensalidade"].sum()
    )

    uptime = round(

        random.uniform(
            99.10,
            99.99
        ),

        2
    )

    chamados = random.randint(
        50,
        200
    )

    clientes_online = random.randint(
        10000,
        13000
    )

    latencia = random.randint(
        8,
        18
    )

    # =========================
    # GRÁFICO
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

        title="Top 10 Cidades",

        title_x=0.5
    )

    # =========================
    # ALERTAS
    # =========================

    cidades_alerta = [

        "Campinas/SP",
        "Osasco/SP",
        "Curitiba/PR",
        "Fortaleza/CE",
        "Belo Horizonte/MG"

    ]

    alerta = random.choice(
        cidades_alerta
    )

    alerta_box = dbc.Alert(

        f"🚨 Falha detectada em {alerta}",

        color="danger",

        className="shadow-sm"

    )

    toast_msg = f"""
    Falha detectada em {alerta}
    """

    # =========================
    # CARDS
    # =========================

    cards = dbc.Row([

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Clientes"),

                    html.H2(
                        total_clientes,
                        className="text-info"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Receita"),

                    html.H2(
                        f"R$ {receita}",
                        className="text-success"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Uptime"),

                    html.H2(
                        f"{uptime}%",
                        className="text-warning"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Chamados"),

                    html.H2(
                        chamados,
                        className="text-danger"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Clientes Online"),

                    html.H2(
                        clientes_online,
                        className="text-success"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

        dbc.Col([

            dbc.Card([

                dbc.CardBody([

                    html.H6("Latência"),

                    html.H2(
                        f"{latencia} ms",
                        className="text-warning"
                    )

                ])

            ],
            className="card-style")

        ], md=4),

    ], className="g-4")

    return (
        cards,
        fig,
        alerta_box,
        toast_msg
    )

# =========================
# CALLBACK MODAL
# =========================

@callback(

    Output(
        "modal-regioes",
        "is_open"
    ),

    Input(
        "btn-regioes",
        "n_clicks"
    ),

    Input(
        "fechar-modal",
        "n_clicks"
    ),

    State(
        "modal-regioes",
        "is_open"
    )

)

def toggle_modal(
    abrir,
    fechar,
    aberto
):

    if abrir or fechar:

        return not aberto

    return aberto