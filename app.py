from dash import Dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
import dash_bootstrap_components as dbc

# =========================
# IMPORT PAGES
# =========================

from pages import dashboard
from pages import clientes
from pages import vendas
from pages import mapa
from pages import tecnicos
from pages import rede
from pages import chamados
from pages import financeiro
from pages import frota
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

    # =========================
    # LOGO
    # =========================

    html.H1(

        "FiberFlow",

        style={

            "textAlign": "center",
            "color": "#38bdf8",
            "marginBottom": "5px"

        }

    ),

    html.P(

        "NOC Telecom Center",

        style={

            "textAlign": "center",
            "color": "#94a3b8",
            "marginBottom": "30px"

        }

    ),

    # =========================
    # PERFIL
    # =========================

    dbc.Card([

        dbc.CardBody([

            html.H4(

                "👨‍💻 Bruno",

                className="text-info"

            ),

            html.P(

                "Administrador"

            ),

            dbc.Badge(

                "ONLINE",

                color="success"

            )

        ])

    ],

    className="mb-4"),

    # =========================
    # MENU
    # =========================

    dbc.Nav([

        dbc.NavLink(

            "📊 Dashboard",

            href="/",

            active="exact"

        ),
            dbc.NavLink(

            "🚗 Frota",

             href="/frota",

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

    "🌎 Mapa Telecom",

    href="/mapa",

    active="exact"

),

   dbc.NavLink(

    "👨‍🔧 Técnicos",

    href="/tecnicos",

    active="exact"

),

dbc.NavLink(

    "📡 Rede",

    href="/rede",

    active="exact"

),

dbc.NavLink(

     "🚨 Alertas",

     href="#"

),
        dbc.NavLink(

            "🛰️ ONU Offline",

            href="#"

        ),

        dbc.NavLink(

         "📞 Chamados",

        href="/chamados",

        active="exact"

),

        dbc.NavLink(

         "💵 Financeiro",

        href="/financeiro",

          active="exact"

),
        dbc.NavLink(

            "⚙️ Configurações",

            href="#"

        )

    ],

    vertical=True,

    pills=True),

    html.Hr(),

    # =========================
    # STATUS REDE
    # =========================

    html.H5(

        "📡 Status Rede",

        className="text-info"

    ),

    dbc.Alert(

        "🟢 Servidor ONLINE",

        color="success",

        className="mb-2"

    ),

    dbc.Alert(

        "🟡 Latência Alta SP",

        color="warning",

        className="mb-2"

    ),

    dbc.Alert(

        "🔴 ONU Offline Osasco",

        color="danger",

        className="mb-2"

    ),

    html.Hr(),

    # =========================
    # INFORMAÇÕES
    # =========================

    html.H5(

        "⚡ Sistema",

        className="text-info"

    ),

    html.P(

        "Uptime: 99.98%",

        style={

            "color": "white"

        }

    ),

    html.P(

        "Ping Médio: 12ms",

        style={

            "color": "white"

        }

    ),

    html.P(

        "Técnicos Online: 14",

        style={

            "color": "white"

        }

    )

],

style={

    "position": "fixed",

    "top": 0,

    "left": 0,

    "bottom": 0,

    "width": "320px",

    "padding": "20px",

    "overflowY": "auto",

    "background": "#111827",

    "boxShadow": "0 0 25px rgba(0,0,0,0.5)"

})

# =========================
# LAYOUT
# =========================

app.layout = html.Div([

    dcc.Location(

        id="url",

        refresh=False

    ),

    html.Div(

        sidebar

    ),

    html.Div(

        id="conteudo",

        style={

            "marginLeft": "340px",

            "padding": "20px"

        }

    )

])

# =========================
# ROUTER
# =========================

@app.callback(

    Output("conteudo", "children"),

    Input("url", "pathname")

)

def render_page(pathname):

    if pathname == "/clientes":

        return clientes.layout()

    elif pathname == "/vendas":
           
           return vendas.layout()
    
    elif pathname == "/frota":
        
        return frota.layout()

    elif pathname == "/chamados":

        return chamados.layout()

    elif pathname == "/financeiro":

        return financeiro.layout()

    elif pathname == "/mapa":

        return mapa.layout()

    elif pathname == "/tecnicos":

        return tecnicos.layout()

    elif pathname == "/rede":

        return rede.layout()

    else:

        return dashboard.layout()

# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(

        debug=True

    )