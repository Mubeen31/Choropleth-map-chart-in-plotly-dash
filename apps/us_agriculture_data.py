import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

expo = pd.read_csv(DATA_PATH.joinpath('2011_us_ag_exports.csv'))

layout = html.Div([

html.Div([
        html.Div([


            html.P('US Agriculture Data', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            dcc.Dropdown(id = 'select_state',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'AK',
                         placeholder = 'Select state',
                         options = [{'label': c, 'value': c}
                                    for c in (expo['code'].unique())], className = 'dcc_compon'),

            ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),

    ], className = "row flex-display"),

            html.Div([
                html.Div([

                    dcc.Graph(id = 'map_1',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 eight columns"),

            ], className = "row flex-display"),




], id="mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('map_1', 'figure'),
              [Input('select_state', 'value')])
def update_graph(select_state):
    expo1 = expo.groupby(['code', 'state'])[['total exports', 'beef', 'pork']].sum().reset_index()
    expo2 = expo1[expo1['code'] == select_state]

    return {
        'data': [go.Choropleth(
            locations = expo2['code'],
            z = expo2['total exports'],
            locationmode = 'USA-states',
            colorscale = 'HSV',
            showscale = False,
            autocolorscale = False,
            reversescale = False,
            marker = dict(line = dict(color = 'darkgray', width = 0.5)),

            hoverinfo = 'text',
            hovertext =
            '<b>State</b>: ' + expo2['state'].astype(str) + '<br>' +
            '<b>Total exports</b>: ' + [f'{x:,.0f}' for x in expo2['total exports']] + '<br>'

        )],

        'layout': go.Layout(
            margin = {"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor = '#e6e6e6',
            paper_bgcolor = '#e6e6e6',

            hovermode = 'closest',
            geo = dict(
                scope='usa',
                showframe = False,
                showcountries = True,
                countrycolor = 'rgb(40,40,40)',
                showocean = True,
                oceancolor = "LightBlue",
                showcoastlines = True,
                coastlinecolor = "RebeccaPurple",
                showland = True,
                landcolor = 'rgb(217, 217, 217)',
                showlakes = True,
                lakecolor = 'rgb(85,173,240)',
                projection = {'type': 'albers usa'}
            ),
        )

    }
