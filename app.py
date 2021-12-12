# Import the required packages using their usual aliases:
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# Create (instantiate) the app:
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create the app's layout:
app.layout = html.Div([
    html.H1(
        children='Poverty And Equity Database',
        style={
            'color': 'blue',
            'fontSize': '32px'
        }
    ),
    html.H2('The World Bank'),
    dbc.Tabs([
        dbc.Tab([
            html.Ul([
                html.Li('Number of Economies: 170'),
                html.Li('Temporal Coverage: 1974 - 2019'),
                html.Li('Update Frequency: Quarterly'),
                html.Li('Last Update: March 18, 2020'),
                html.Li([
                    'Source: ',
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                           href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                ])
            ])
        ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li([
                    'Title: ',
                    html.Strong('Poverty And Equity Analysis')
                ]),
                html.Li([
                    'Github repo: ',
                    html.A('https://github.com/igoandrade/python-dash', href='https://github.com/igoandrade/python-dash')
                ])
            ])
        ], label='Project Info')
    ])
])

# Run the app:
if __name__ == "__main__":
    app.run_server(debug=True)
