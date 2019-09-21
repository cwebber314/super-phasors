import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_core_components as dcc

import pandas as pd
import numpy as np
from numpy import sin, pi, cos, sum
from matplotlib import pyplot as plt

t = np.linspace(0,2/60.0,200)
A1 = 1
A2 = 1
f1 = 60
f2 = 180
y1 = A1 * sin(2*pi*f1 * t)
y2 = A2 * sin(2*pi*f2 * t)
ysum = y1 + y2

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=t, y=y1,
                    mode='lines',
                    name='y1'))
fig1.add_trace(go.Scatter(x=t, y=y2,
                    mode='lines',
                    name='y2'))

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=t, y=ysum,
                    mode='lines',
                    name='ysum'))

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
    value=60
)  

########### Initiate the app
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)
server = app.server
app.title='Maths!'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1("Super Sines"),
    dcc.Graph(
        id='plot1',
        figure=fig1
        ),
    ss1,
    html.P(),
    ss2,
    html.P(),
    dcc.Graph(
        id='plot2',
        figure=fig2
        ),    
    ]
)

@app.callback(
    dash.dependencies.Output('plot1', 'figure'),
    [dash.dependencies.Input('slider1', 'value'), dash.dependencies.Input('slider2', 'value')])
def update_graph1(value1, value2):
    t = np.linspace(0,2/60.0,200)
    A = 1
    f1 = value1
    f2 = value2
    y1 = A * sin(2*pi*f1 * t)
    y2 = A * sin(2*pi*f2 * t)

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=t, y=y1,
                        mode='lines',
                        name='y1'))
    fig1.add_trace(go.Scatter(x=t, y=y2,
                        mode='lines',
                        name='y2'))
    return fig1


@app.callback(
    dash.dependencies.Output('plot2', 'figure'),
    [dash.dependencies.Input('slider1', 'value'), dash.dependencies.Input('slider2', 'value')])
def update_graph2(value1, value2):
    t = np.linspace(0,2/60.0,200)
    A = 1
    f1 = value1
    f2 = value2
    y1 = A * sin(2*pi*f1 * t)
    y2 = A * sin(2*pi*f2 * t)
    ysum = y1 + y2

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=t, y=ysum,
                        mode='lines',
                        name='ysum'))
    return fig2



    
if __name__ == '__main__':
    app.run_server(debug=True)
