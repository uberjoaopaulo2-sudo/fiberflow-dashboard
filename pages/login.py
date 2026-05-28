from dash import html
from dash import dcc

import dash_bootstrap_components as dbc

# =========================
# LOGIN PAGE
# =========================

def layout():

    return html.Div([

        dbc.Container([

            dbc.Row([

                dbc.Col([

                    dbc.Card([

                        dbc.CardBody([

                            html.H1(

                                "FiberFlow",

                                className="text-center text-info mb-3"

                            ),

                            html.H4(

                                "Telecom Analytics",

                                className="text-center text-light mb-4"

                            ),

                            dbc.Input(

                                placeholder="Usuário",

                                type="text",

                                className="mb-3"

                            ),

                            dbc.Input(

                                placeholder="Senha",

                                type="password",

                                className="mb-4"

                            ),

                            dcc.Link(

                                dbc.Button(

                                    "Entrar",

                                    color="primary",

                                    size="lg",

                                    className="w-100"

                                ),

                                href="/dashboard",

                                style={

                                    "textDecoration": "none"

                                }

                            ),

                            html.Br(),
                            html.Br(),

                            html.Div(

                                "Sistema Corporativo FiberFlow",

                                className="text-center text-secondary"

                            )

                        ])

                    ],

                    className="shadow-lg p-4"

                    )

                ],

                md=4)

            ],

            justify="center",

            className="vh-100 align-items-center"

            )

        ],

        fluid=True)

    ],

    style={

        "backgroundColor": "#0f172a",

        "height": "100vh"

    })