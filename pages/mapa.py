from dash import html

import dash_bootstrap_components as dbc

import dash_leaflet as dl

# =========================
# LAYOUT
# =========================

def layout():

    return html.Div([

        html.H1(

            "🌎 Mapa Telecom",

            style={

                "color": "white",

                "marginBottom": "30px"

            }

        ),

        dbc.Row([

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        html.H4(
                            "📡 Regiões Críticas"
                        ),

                        html.Hr(),

                        html.P(
                            "🔴 Campinas/SP"
                        ),

                        html.P(
                            "⚠️ São Paulo/SP"
                        ),

                        html.P(
                            "🚨 Osasco/SP"
                        ),

                        html.P(
                            "⚠️ Curitiba/PR"
                        ),

                    ])

                ],

                className="shadow-lg")

            ],

            md=3),

            dbc.Col([

                dbc.Card([

                    dbc.CardBody([

                        dl.Map(

                            center=[-23.5505, -46.6333],

                            zoom=7,

                            style={

                                "width": "100%",

                                "height": "700px"

                            },

                            children=[

                                dl.TileLayer(),

                                # =========================
                                # CAMPINAS
                                # =========================

                                dl.Marker(

                                    position=[

                                        -22.9099,
                                        -47.0626

                                    ],

                                    children=[

                                        dl.Popup(

                                            [

                                                html.H4(
                                                    "Campinas/SP"
                                                ),

                                                html.P(
                                                    "🚨 Fibra rompida"
                                                ),

                                                html.P(
                                                    "120 clientes afetados"
                                                )

                                            ]

                                        )

                                    ]

                                ),

                                # =========================
                                # SÃO PAULO
                                # =========================

                                dl.Marker(

                                    position=[

                                        -23.5505,
                                        -46.6333

                                    ],

                                    children=[

                                        dl.Popup(

                                            [

                                                html.H4(
                                                    "São Paulo/SP"
                                                ),

                                                html.P(
                                                    "⚠️ Alta latência"
                                                ),

                                                html.P(
                                                    "85ms detectados"
                                                )

                                            ]

                                        )

                                    ]

                                ),

                                # =========================
                                # OSASCO
                                # =========================

                                dl.Marker(

                                    position=[

                                        -23.5329,
                                        -46.7917

                                    ],

                                    children=[

                                        dl.Popup(

                                            [

                                                html.H4(
                                                    "Osasco/SP"
                                                ),

                                                html.P(
                                                    "🚨 ONU offline"
                                                ),

                                                html.P(
                                                    "43 clientes afetados"
                                                )

                                            ]

                                        )

                                    ]

                                ),

                                # =========================
                                # CURITIBA
                                # =========================

                                dl.Marker(

                                    position=[

                                        -25.4284,
                                        -49.2733

                                    ],

                                    children=[

                                        dl.Popup(

                                            [

                                                html.H4(
                                                    "Curitiba/PR"
                                                ),

                                                html.P(
                                                    "⚠️ Instabilidade"
                                                ),

                                                html.P(
                                                    "Packet loss detectado"
                                                )

                                            ]

                                        )

                                    ]

                                )

                            ]

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