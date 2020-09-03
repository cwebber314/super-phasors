"""
Play around with line constants
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc
import numpy as np
from numpy import sin, pi, cos, sum
import dash_bootstrap_components as dbc

def get_graph(tower, param):
    t = np.linspace(0,2/60.0,200)
    y = sin(2*pi*60*t)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y,
                        mode='lines',
                        name='y'))
    fig.update_layout(
        title=go.layout.Title(
            text="Positive Sequence Impedance",
            xref="paper",
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="sweep_step",
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="R(pu)",
            )
        )
    )
    return fig


fig = get_graph({}, 'R')

# Sweep Conductor1 X
slider_c1x = dcc.RangeSlider(
    tooltip={'always_visible': False},
    id='slider_c1x',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep Conductor1 Y
slider_c1y = dcc.RangeSlider(
    id='slider_c1y',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep Conductor2 X
slider_c2x = dcc.RangeSlider(
    tooltip={'always_visible': False},
    id='slider_c2x',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep Conductor2 Y
slider_c2y = dcc.RangeSlider(
    id='slider_c2y',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep Conductor3 X
slider_c3x = dcc.RangeSlider(
    tooltip={'always_visible': False},
    id='slider_c3x',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep Conductor3 Y
slider_c3y = dcc.RangeSlider(
    id='slider_c3y',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)

# Sweep ConductoShield1 X
slider_s1x = dcc.RangeSlider(
    id='slider_s1x',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)
# Sweep ConductoShield1 Y
slider_s1y = dcc.RangeSlider(
    id='slider_s1y',
    min=-20,
    max=20,
    step=1,
    value=[0, 0],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)


# Sweep Rho
slider_rho = dcc.RangeSlider(
    id='slider_rho',
    min=1,
    max=1000,
    step=1,
    value=[100, 100],
    marks={-20:'-20', -10:'-10', -5:'-5', 0:'0', 5:'5', 10:'10', 20:'20'},
)

# Conductor Select
cond_select = dcc.Dropdown(
    id='cond_select',
    options=[
        {'label': '795 KCM ACSR (Drake)', 'value': 0},
        {'label': '1590 KCM ACSR (Falcon)', 'value': 1},        
    ],
    value=0
)
shield_select = dcc.Dropdown(
    id='shield_select',
    options=[
        {'label': 'Alumoweld', 'value': 2},
        {'label': 'OPGW', 'value': 3},        
    ],
    value=2
)

in1 = dcc.Input(id="input1", type="text", placeholder=""),

c1x = dcc.Input(
    id='text_c1x',
    type="text",
    placeholder = 'C1 x',
    value = 0,
    style={'width': '100%'}
    )
c1y = dcc.Input(
    id='text_c1y',
    placeholder = 'C1 y',
    value = 0,
    style={'width': '100%'}
    )
c2x = dcc.Input(
    id='text_c2x',
    type="text",
    placeholder = 'C2 x',
    value = 0,
    style={'width': '100%'}
    )
c2y = dcc.Input(
    id='text_c2y',
    placeholder = 'C2 y',
    value = 0,
    style={'width': '100%'}
    )
c3x = dcc.Input(
    id='text_c3x',
    type="text",
    placeholder = 'C3 x',
    value = 0,
    style={'width': '100%'}
    )
c3y = dcc.Input(
    id='text_c3y',
    placeholder = 'C3 y',
    value = 0,
    style={'width': '100%'}
    )
s1x = dcc.Input(
    id='text_s1x',
    type="text",
    placeholder = 'S1 x',
    value = 0,
    style={'width': '100%'}
    )
s1y = dcc.Input(
    id='text_s1y',
    placeholder = 'S1 y',
    value = 0,
    style={'width': '100%'}
    )

########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(__name__)
server = app.server
app.title = 'Line Params'

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Line Params", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
        ),
    ],
    brand="Line Param Toy",
    brand_href="#",
    sticky="top",
)

body = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Line Param Toy"),
            html.P("Explore the affect of physical properties on overhead transmission line impedance"),
        ])
    ]),
    dbc.Row([ 
        dbc.Col([
            cond_select,
        ]),
    ], style={'marginBottom': '1em'}),
    dbc.Row([ 
        dbc.Col([
            shield_select,
        ]),
    ], style={'marginBottom': '1em'}),
    dbc.Row([ 
        dbc.Col([html.P("C1 x"), c1x], width=1),
        dbc.Col([html.P("C1 y"), c1y], width=1),
        dbc.Col([html.P("x"), slider_c1x], width=3),
        dbc.Col([html.P("y"), slider_c1y], width=3),
        ], style={'marginBottom': '1em'}),
    dbc.Row([ 
        dbc.Col([html.P("C2 x"), c2x], width=1),
        dbc.Col([html.P("C2 y"), c2y], width=1),
        dbc.Col([html.P("x"), slider_c2x], width=3),
        dbc.Col([html.P("y"), slider_c2y], width=3),
        ], style={'marginBottom': '1em'}),
    dbc.Row([ 
        dbc.Col([html.P("C3 x"), c3x], width=1),
        dbc.Col([html.P("C3 y"), c3y], width=1),
        dbc.Col([html.P("x"), slider_c3x], width=3),
        dbc.Col([html.P("y"), slider_c3y], width=3),
        ], style={'marginBottom': '1em'}),
    dbc.Row([ 
        dbc.Col([html.P("S1 x"), s1x], width=1),
        dbc.Col([html.P("S1 y"), s1y], width=1),
        dbc.Col([html.P("x"), slider_s1x], width=3),
        dbc.Col([html.P("y"), slider_s1y], width=3),
        ], style={'marginBottom': '1em'}),
    dbc.Row([
        dbc.Col([
            # html.P(),
            # sf2,
            # html.P("Plot of sine waves y1, y2"),
            dcc.Graph(
                id='plot',
                figure=fig,
                ),
            # html.P("Plot of sum(y1+y2)"),
        ])
    ])
])

app.layout = html.Div([navbar, body])


@app.callback(
    dash.dependencies.Output('plot', 'figure'),
        [
        # dash.dependencies.Input('text_c1x', 'value'), dash.dependencies.Input('text_c1y', 'value'),
        # dash.dependencies.Input('slider_rho', 'value'), dash.dependencies.Input('cond_select', 'value'),
        # dash.dependencies.Input('slider_c1x', 'value'), dash.dependencies.Input('slider_c1y', 'value'),
        ],
    )
def update_graph1():
    fig = get_graph({}, 'R')
    return fig
    
if __name__ == '__main__':
    app.run_server(debug=True)
