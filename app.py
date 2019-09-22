import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc
import numpy as np
from numpy import sin, pi, cos, sum
import dash_bootstrap_components as dbc

def get_graph(f1, f2, A1, A2, theta1, theta2, which=1):
    t = np.linspace(0,2/60.0,200)
    f1 = f1
    f2 = f2
    y1 = A1 * sin(2*pi*f1 * t + theta1)
    y2 = A2 * sin(2*pi*f2 * t + theta2)
    ysum = y1 + y2

    if which==1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=t, y=y1,
                            mode='lines',
                            name='y1'))
        fig1.add_trace(go.Scatter(x=t, y=y2,
                            mode='lines',
                            name='y2'))
        fig1.update_layout(
            title=go.layout.Title(
                text="Sine Waves",
                xref="paper",
                x=0
            ),
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text="time",
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text="Amplitude",
                )
            )
        )
        fig = fig1
    elif which == 2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=t, y=ysum,
                            mode='lines',
                            name='ysum'))
        fig2.update_layout(
            title=go.layout.Title(
                text="Sum of sine waves",
                xref="paper",
                x=0
            ),
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text="time",
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text="Amplitude",
                )
            )
        )
        fig = fig2

    return fig


fig1 = get_graph(60, 120, 1, 1, 0, 0, which=1)
fig2 = get_graph(60, 120, 1, 1, 0, 0, which=2)


sf1 = dcc.Slider(
    id='slider1_f',
    min=0,
    max=300,
    step=10,
    marks={
        0: "0 Hz",
        60: "60 Hz",
        120: "120 Hz",
        180: "180 Hz",
        240: "240 Hz",
        300: "300 Hz",
    },
    value=60
)
sa1 = dcc.Slider(
    id='slider1_a',
    min=0,
    max=2,
    step=0.1,
    marks={
        0: "0",
        1: "1",
        2: "2",
    },
    value=1
)
stheta1 = dcc.Slider(
    id='slider1_theta',
    min=-pi,
    max=pi,
    step=pi/12,
    marks={
        -pi: "-pi",
        -pi/2: "-pi/2",
        0: "0",
        pi/2: "pi/2",
        pi: "pi",
    },
    value=0
)

sf2 = dcc.Slider(
    id='slider2_f',
    min=0,
    max=300,
    step=10,
    marks={
        0: "0 Hz",
        60: "60 Hz",
        120: "120 Hz",
        180: "180 Hz",
        240: "240 Hz",
        300: "300 Hz",
    },
    value=120
)  
sa2 = dcc.Slider(
    id='slider2_a',
    min=0,
    max=2,
    step=0.1,
    marks={
        0: "0",
        1: "1",
        2: "2",
    },
    value=1
)
stheta2 = dcc.Slider(
    id='slider2_theta',
    min=-pi,
    max=pi,
    step=pi/12,
    marks={
        -pi: "-pi",
        -pi/2: "-pi/2",
        0: "0",
        pi/2: "pi/2",
        pi: "pi",
    },
    value=0
)


########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(__name__)
server = app.server
app.title='Super Phasors'

########### Set up the layout
# app.layout = html.Div(children=[
#     html.H1("Super Sines"),
#     html.P("Move the sliders to change the frequency of the two sine wavees"),
#     sf1,
#     html.P(),
#     sf2,
#     # html.P("Plot of sine waves y1, y2"),
#     dcc.Graph(
#         id='plot1',
#         figure=fig1
#         ),
#     # html.P("Plot of sum(y1+y2)"),
#     dcc.Graph(
#         id='plot2',
#         figure=fig2
#         ),    
#     ]
# )

body = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Super Sines"),
            html.P("Move the sliders to change the frequency of the two sine wavees"),
        ])
    ]),
    dbc.Row([ 
        dbc.Col([
            html.P("frequency"),
            sf1,
        ]),
        dbc.Col([
            html.P("amplitude"),
            sa1,
        ]),
        dbc.Col([
            html.P("theta"),
            stheta1,
        ]),
    ], style={'marginBottom': '3em'}),
    dbc.Row([ 
        dbc.Col([
            sf2,
        ]),
        dbc.Col([
            sa2,
        ]),
        dbc.Col([
            stheta2,
        ]),
    ], style={'marginBottom': '3em'}),
    dbc.Row([
        dbc.Col([
            # html.P(),
            # sf2,
            # html.P("Plot of sine waves y1, y2"),
            dcc.Graph(
                id='plot1',
                figure=fig1,
                ),
            # html.P("Plot of sum(y1+y2)"),
            dcc.Graph(
                id='plot2',
                figure=fig2,
                ),
            ])
        ])
    ])
app.layout = html.Div([body])


@app.callback(
    dash.dependencies.Output('plot1', 'figure'),
    [dash.dependencies.Input('slider1_f', 'value'), dash.dependencies.Input('slider2_f', 'value'),
     dash.dependencies.Input('slider1_a', 'value'), dash.dependencies.Input('slider2_a', 'value'),
     dash.dependencies.Input('slider1_theta', 'value'), dash.dependencies.Input('slider2_theta', 'value'),
     ],
    )
def update_graph1(f1, f2, a1, a2, theta1, theta2):
    fig = get_graph(f1, f2, a1, a2, theta1, theta2, which=1)
    return fig


@app.callback(
    dash.dependencies.Output('plot2', 'figure'),
    [dash.dependencies.Input('slider1_f', 'value'), dash.dependencies.Input('slider2_f', 'value'),
    dash.dependencies.Input('slider1_a', 'value'), dash.dependencies.Input('slider2_a', 'value'),
    dash.dependencies.Input('slider1_theta', 'value'), dash.dependencies.Input('slider2_theta', 'value'),
    ],
    )
def update_graph2(f1, f2, a1, a2, theta1, theta2):
    fig = get_graph(f1, f2, a1, a2, theta1, theta2, which=2)
    return fig
    
if __name__ == '__main__':
    app.run_server()
