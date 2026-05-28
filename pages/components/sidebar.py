from dash import html

import dash_bootstrap_components as dbc

# =========================
# SIDEBAR
# =========================

sidebar = html.Div([

    html.H2(

        "FiberFlow",

        className="sidebar-title"

    ),

    html.Hr(),

    dbc.Nav([

        dbc.NavLink(

            "📊 Dashboard",

            href="/",

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

className="sidebar")