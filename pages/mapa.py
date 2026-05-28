from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import callback

import dash_bootstrap_components as dbc

import dash_leaflet as dl

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

            id="intervalo-mapa",

            interval=3000,

            n_intervals=0

        ),

        # =========================
        # TITLE
        # =========================

        html.H1(

            "🌎 Central Telecom RealTime",

            style={

                "color": "white",

                "marginBottom": "20px"

            }

        ),

        # =========================
        # ALERTA TOPO
        # =========================

        html.Div(

            id="alerta-topo",

            style={

                "marginBottom": "20px"

            }

        ),

        dbc.Row([

            # =========================
            # LATERAL
            # =========================

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4(
                            "📡 Regiões"
                        ),

                        html.Hr(),

                        html.Div(
                            id="lista-regioes"
                        )

                    ])

                ],

                className="shadow-lg")

            ],

            md=3),

            # =========================
            # MAPA
            # =========================

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.Div(
                            id="mapa-realtime"
                        )

                    ])

                ],

                className="shadow-lg")

            ],

            md=9)

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

    Output("mapa-realtime", "children"),
    Output("lista-regioes", "children"),
    Output("alerta-topo", "children"),

    Input("intervalo-mapa", "n_intervals")

)

def atualizar_mapa(n):

    cidades = [

        {

            "nome": "Campinas/SP",
            "lat": -22.9099,
            "lon": -47.0626

        },

        {

            "nome": "São Paulo/SP",
            "lat": -23.5505,
            "lon": -46.6333

        },

        {

            "nome": "Osasco/SP",
            "lat": -23.5329,
            "lon": -46.7917

        },

        {

            "nome": "Curitiba/PR",
            "lat": -25.4284,
            "lon": -49.2733

        },

        {

            "nome": "Fortaleza/CE",
            "lat": -3.7319,
            "lon": -38.5267

        }

    ]

    status_lista = []

    markers = []

    alertas_criticos = []

    # =========================
    # LOOP
    # =========================

    for cidade in cidades:

        status = random.choice([

            "🟢 ONLINE",
            "🟡 INSTÁVEL",
            "🔴 CRÍTICO"

        ])

        clientes = random.randint(

            20,
            300

        )

        # =========================
        # ALERTAS LATERAIS
        # =========================

        cor = (

            "success"

            if "ONLINE" in status

            else

            "warning"

            if "INSTÁVEL" in status

            else

            "danger"

        )

        status_lista.append(

            dbc.Alert(

                [

                    html.H6(
                        cidade["nome"]
                    ),

                    html.P(status),

                    html.P(
                        f"{clientes} clientes afetados"
                    )

                ],

                color=cor,

                className="mb-3"

            )

        )

        # =========================
        # ALERTA CRÍTICO
        # =========================

        if "CRÍTICO" in status:

            alertas_criticos.append(

                f"🚨 {cidade['nome']} em estado crítico"

            )

        # =========================
        # MAPA
        # =========================

        markers.append(

            dl.CircleMarker(

                center=[

                    cidade["lat"],
                    cidade["lon"]

                ],

                radius=25,

                color=

                "green"

                if "ONLINE" in status

                else

                "yellow"

                if "INSTÁVEL" in status

                else

                "red",

                fill=True,

                fillOpacity=0.8,

                children=[

                    dl.Popup([

                        html.H4(
                            cidade["nome"]
                        ),

                        html.P(status),

                        html.P(
                            f"{clientes} clientes afetados"
                        )

                    ])

                ]

            )

        )

    # =========================
    # MAPA
    # =========================

    mapa = dl.Map(

        center=[-23.5505, -46.6333],

        zoom=5,

        style={

            "width": "100%",
            "height": "700px"

        },

        children=[

            dl.TileLayer(),

            *markers

        ]

    )

    # =========================
    # ALERTA TOPO
    # =========================

    if len(alertas_criticos) > 0:

        alerta_topo = dbc.Alert(

            [

                html.H4(
                    "🚨 ALERTA CRÍTICO"
                ),

                html.Hr(),

                html.Div([

                    html.P(alerta)

                    for alerta in alertas_criticos

                ])

            ],

            color="danger",

            style={

                "animation": "blinker 1s linear infinite"

            }

        )

    else:

        alerta_topo = dbc.Alert(

            "🟢 Sistema operando normalmente",

            color="success"

        )

    return (

        mapa,

        status_lista,

        alerta_topo

    )