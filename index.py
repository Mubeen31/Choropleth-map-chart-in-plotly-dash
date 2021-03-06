import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import World_covid_19_data, us_agriculture_data, all_countries_covid_19_data

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div([
        html.Div([
            html.Div([
                html.H3('Choropleth Map Chart', style = {'margin-bottom': '0px', 'color': 'black'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),

    html.Div([
      html.Div([
        dcc.Link('World Covid - 19 Data', href='/apps/World_covid_19_data', style = {"margin-bottom": "20px", 'padding': '25px', 'fontWeight': 'bold', 'color': 'blue'}),
        dcc.Link('US Agriculture Data', href='/apps/us_agriculture_data', style = {"margin-bottom": "20px", 'padding': '25px', 'fontWeight': 'bold', 'color': 'blue'}),
        dcc.Link('All Countries Covid - 19 Data', href='/apps/all_countries_covid_19_data', style = {"margin-bottom": "20px", 'padding': '25px', 'fontWeight': 'bold', 'color': 'blue'}),

        ], className = "create_container3 eight columns", id = "title1"),

    ], id = "header1", className = "row flex-display"),

    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/World_covid_19_data':
        return World_covid_19_data.layout
    elif pathname == '/apps/us_agriculture_data':
        return us_agriculture_data.layout
    elif pathname == '/apps/all_countries_covid_19_data':
        return all_countries_covid_19_data.layout
    else:
        return "Page Error! Please select a link"


if __name__ == '__main__':
    app.run_server(debug=False)