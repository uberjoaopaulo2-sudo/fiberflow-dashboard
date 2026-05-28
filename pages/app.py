from dash import Dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import callback

import dash_bootstrap_components as dbc

# =========================
# IMPORTS
# =========================

from pages import dashboard
from pages import clientes
from pages import vendas
from pages import mapa
from pages import login

# =========================
# APP
# =========================

app = Dash(

    __name__,

    external_stylesheets=[
        dbc.themes.CYBORG
    ],

    suppress_callback_exceptions=True

)

server = app.server

# =========================
# SIDEBAR
# =========================

sidebar = html.Div([

    html.H2(

        "FiberFlow",

        className="text-info text-center mb-4"

    ),

    dbc.Nav([

        dbc.NavLink(
            "📊 Dashboard",
            href="/dashboard",
            active="exact"
        ),

        dbc.NavLink(
            "👥 Clientes",
            href="/clientes",
            active="exact"
        ),

        dbc.NavLink(
            "💰 Vendas",
            href="/vendas",
            active="exact"
        ),

        dbc.NavLink(
            "🌎 Mapa",
            href="/mapa",
            active="exact"
        ),

    ],

    vertical=True,
    pills=True)

],

style={

    "position": "fixed",

    "top": 0,

    "left": 0,

    "bottom": 0,

    "width": "240px",

    "padding": "20px",

    "backgroundColor": "#111827"

})

# =========================
# LAYOUT
# =========================

app.layout = html.Div([

    dcc.Location(
    id="url",
    refresh=False,
    pathname="/login"
),

    html.Div(
        id="sidebar-container"
    ),

    html.Div(
        id="conteudo"
    )

])

# =========================
# ROUTER
# =========================

@callback(

    Output(
        "conteudo",
        "children"
    ),

    Output(
        "sidebar-container",
        "children"
    ),

    Input(
        "url",
        "pathname"
    )

)

def render_page(pathname):

    # LOGIN

    if pathname == "/" or pathname == "/login":

        return (

            login.layout(),

            None

        )

    # DASHBOARD

    elif pathname == "/dashboard":

        return (

            html.Div(

                dashboard.layout(),

                style={

                    "marginLeft": "260px",
                    "padding": "20px"

                }

            ),

            sidebar

        )

    # CLIENTES

    elif pathname == "/clientes":

        return (

            html.Div(

                clientes.layout(),

                style={

                    "marginLeft": "260px",
                    "padding": "20px"

                }

            ),

            sidebar

        )

    # VENDAS

    elif pathname == "/vendas":

        return (

            html.Div(

                vendas.layout(),

                style={

                    "marginLeft": "260px",
                    "padding": "20px"

                }

            ),

            sidebar

        )

    # MAPA

    elif pathname == "/mapa":

        return (

            html.Div(

                mapa.layout(),

                style={

                    "marginLeft": "260px",
                    "padding": "20px"

                }

            ),

            sidebar

        )

    # DEFAULT

    else:

        return (

            login.layout(),

            None

        )

# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )