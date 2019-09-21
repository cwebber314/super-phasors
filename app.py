import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc
import numpy as np
from numpy import sin, pi, cos, sum

def get_graph(f1, f2, which=1):
    t = np.linspace(0,2/60.0,200)
    A1 = 1
    A2 = 1
    f1 = f1
    f2 = f2
    y1 = A1 * sin(2*pi*f1 * t)
    y2 = A2 * sin(2*pi*f2 * t)
    ysum = y1 + y2

    if which==1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=t, y=y1,
                            mode='lines',
                            name='y1'))
        fig1.add_trace(go.Scatter(x=t, y=y2,
                            mode='lines',
                            name='y2'))
        fig = fig1
    elif which == 2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=t, y=ysum,
                            mode='lines',
                            name='ysum'))
        fig = fig2

    return fig


fig1 = get_graph(60, 120, which=1)
fig2 = get_graph(60, 120, which=2)


ss1 = dcc.Slider(
    id='slider1',
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
ss2 = dcc.Slider(
    id='slider2',
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

########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)
server = app.server
app.title='Super Phasors'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Super Sines"),
    html.P("Move the sliders to change the frequency of the two sine wavees"),
    ss1,
    html.P(),
    ss2,
    html.P("Plot of sine waves y1, y2"),
    dcc.Graph(
        id='plot1',
        figure=fig1
        ),
    html.P("Plot of sum(y1+y2)"),
    dcc.Graph(
        id='plot2',
        figure=fig2
        ),    
    ]
)

@app.callback(
    dash.dependencies.Output('plot1', 'figure'),
    [dash.dependencies.Input('slider1', 'value'), dash.dependencies.Input('slider2', 'value')])
def update_graph1(f1, f2):
    fig = get_graph(f1, f2, which=1)
    return fig


@app.callback(
    dash.dependencies.Output('plot2', 'figure'),
    [dash.dependencies.Input('slider1', 'value'), dash.dependencies.Input('slider2', 'value')])
def update_graph2(f1, f2):
    fig = get_graph(f1, f2, which=2)
    return fig




    
if __name__ == '__main__':
    app.run_server(debug=True)
