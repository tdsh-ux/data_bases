
import json
import dash
import urllib.request
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_cytoscape as cyto

app = dash.Dash(__name__)
app.title = "Food Graph"
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


with open('heroku_application/food.json', 'r') as f:
    data = json.loads(f.read())
    
#https://github.com/plotly/dash-cytoscape/blob/master/demos/data/edge-types/cy-style.json
with open('heroku_application/cy-style.json') as f:
    stylesheet = json.loads(f.read())

styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100%',
        'width': '100%'
    },
    'cy-container': {
        'flex': '1',
        'position': 'relative'
    },
    'cytoscape': {
        'position': 'absolute',
        'width': '100%',
        'height': '100%',
        'z-index': 999
    }
}


# App
app.layout = html.Div(style=styles['container'], children=[
    html.Div([
        html.Button("Responsive Toggle", id='toggle-button'),
        html.Div(id='toggle-text')
    ]),
    html.Div(className='cy-container', style=styles['cy-container'], children=[
        cyto.Cytoscape(
            id='cytoscape',
            elements=data['elements'],
            stylesheet=stylesheet,
            style=styles['cytoscape'],
            layout={
                'name': 'cose',
                'idealEdgeLength': 100,
                'nodeOverlap': 1,
                'refresh': 20,
                'fit': True,
                'padding': 200,
                'randomize': False,
                'componentSpacing': 100,
                'nodeRepulsion': 400000,
                'edgeElasticity': 50,
                'nestingFactor': 5,
                'gravity': 80,
                'numIter': 1000,
                'initialTemp': 200,
                'coolingFactor': 0.95,
                'minTemp': 1.0,
                'minNodeSpacing': 30
            },
            responsive=True
        )
    ])
])

