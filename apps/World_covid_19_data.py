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

covid = pd.read_csv(DATA_PATH.joinpath('Covid 19 data 2020-01-22 to 2020-12-25.csv'))

layout = html.Div([

html.Div([
        html.Div([


            html.P('World: Covid - 19 data 2020-01-22 to 2020-12-25', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            dcc.Dropdown(id = 'select_country1',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'Afghanistan',
                         placeholder = 'Select country',
                         options = [{'label': c, 'value': c}
                                    for c in (covid['Country/Region'].unique())], className = 'dcc_compon'),

            html.P('Select Category', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'radio_items',
                           labelStyle = {"display": "inline-block"},
                           options = [{'label': 'Confirmed', 'value': 'confirmed1'},
                                      {'label': 'Deaths', 'value': 'deaths1'},
                                      {'label': 'Recovered', 'value': 'recovered1'},
                                      {'label': 'Active', 'value': 'active1'}],
                           value = 'confirmed1',
                           style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

            ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),

    ], className = "row flex-display"),

            html.Div([
                html.Div([

                    dcc.Graph(id = 'map_2',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 eight columns"),

            ], className = "row flex-display"),




], id="mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('map_2', 'figure'),
              [Input('select_country1', 'value')],
              [Input('radio_items', 'value')])
def update_graph(select_country1, radio_items):
    covid1 = covid.groupby(['Country/Region'])[['confirmed', 'death', 'recovered', 'active']].max().reset_index()
    covid2 = covid1[covid1['Country/Region'] == select_country1]

    if radio_items == 'confirmed1':

     return {
        'data': [go.Choropleth(
            locations = covid2['Country/Region'],
            z = covid2['confirmed'],
            locationmode = 'country names',
            colorscale = 'Sunsetdark',
            showscale = False,
            autocolorscale = False,
            reversescale = False,
            marker = dict(line = dict(color = 'darkgray', width = 0.5)),

            hoverinfo = 'text',
            hovertext =
            '<b>Country</b>: ' + covid2['Country/Region'].astype(str) + '<br>' +
            '<b>Confirmed</b>: ' + [f'{x:,.0f}' for x in covid2['confirmed']] + '<br>'

        )],

        'layout': go.Layout(
            margin = {"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor = '#e6e6e6',
            paper_bgcolor = '#e6e6e6',

            hovermode = 'closest',
            geo = dict(
                fitbounds = 'locations',
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
                projection = {'type': 'equirectangular'}
            ),
        )

    }

    elif radio_items == 'deaths1':

     return {
        'data': [go.Choropleth(
            locations = covid2['Country/Region'],
            z = covid2['death'],
            locationmode = 'country names',
            colorscale = 'mrybm',
            showscale = False,
            autocolorscale = False,
            reversescale = False,
            marker = dict(line = dict(color = 'darkgray', width = 0.5)),

            hoverinfo = 'text',
            hovertext =
            '<b>Country</b>: ' + covid2['Country/Region'].astype(str) + '<br>' +
            '<b>Death</b>: ' + [f'{x:,.0f}' for x in covid2['death']] + '<br>'

        )],

        'layout': go.Layout(
            margin = {"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor = '#e6e6e6',
            paper_bgcolor = '#e6e6e6',

            hovermode = 'closest',
            geo = dict(
                fitbounds = 'locations',
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
                projection = {'type': 'equirectangular'}
            ),
        )

    }

    elif radio_items == 'recovered1':

     return {
        'data': [go.Choropleth(
            locations = covid2['Country/Region'],
            z = covid2['recovered'],
            locationmode = 'country names',
            colorscale = 'Tealgrn',
            showscale = False,
            autocolorscale = False,
            reversescale = False,
            marker = dict(line = dict(color = 'darkgray', width = 0.5)),

            hoverinfo = 'text',
            hovertext =
            '<b>Country</b>: ' + covid2['Country/Region'].astype(str) + '<br>' +
            '<b>Recovered</b>: ' + [f'{x:,.0f}' for x in covid2['recovered']] + '<br>'

        )],

        'layout': go.Layout(
            margin = {"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor = '#e6e6e6',
            paper_bgcolor = '#e6e6e6',

            hovermode = 'closest',
            geo = dict(
                fitbounds = 'locations',
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
                projection = {'type': 'equirectangular'}
            ),
        )

    }

    elif radio_items == 'active1':

     return {
        'data': [go.Choropleth(
            locations = covid2['Country/Region'],
            z = covid2['active'],
            locationmode = 'country names',
            colorscale = 'ice',
            showscale = False,
            autocolorscale = False,
            reversescale = False,
            marker = dict(line = dict(color = 'darkgray', width = 0.5)),

            hoverinfo = 'text',
            hovertext =
            '<b>Country</b>: ' + covid2['Country/Region'].astype(str) + '<br>' +
            '<b>Active</b>: ' + [f'{x:,.0f}' for x in covid2['active']] + '<br>'

        )],

        'layout': go.Layout(
            margin = {"r": 0, "t": 0, "l": 0, "b": 0},
            plot_bgcolor = '#e6e6e6',
            paper_bgcolor = '#e6e6e6',

            hovermode = 'closest',
            geo = dict(
                fitbounds = 'locations',
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
                projection = {'type': 'equirectangular'}
            ),
        )

    }
