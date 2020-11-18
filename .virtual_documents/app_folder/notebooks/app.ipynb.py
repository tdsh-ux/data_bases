import json
import jupyter_dash
import urllib.request 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_cytoscape as cyto 

import pandas as pd 
import numpy as np 

import networkx as nx 

import plotly.express as px 

from IPython.display import Javascript 


df = pd.read_csv("../data_csv/table.csv") 
df.head() 


df_year = pd.read_csv("../data_csv/scatter_data.csv").sort_values(by = "year") 
df_year.head() 


dish_names = df["name_x"] 
options = [] 
for name in dish_names: 
    options.append({
        "label": name, 
        "value": name 
    }) 


def cytoscape_data(name = None, n = 128): 
    nodes = [] 
    edges = [] 
    # dish_names = set(df["name_x"].unique().tolist()).union(set(df["name_y"].unique().tolist())) 
    if n is not None: 
        indexes = np.random.choice(745, n) 
        dishes = np.array(df.to_records(index = False))[indexes] 
    else: 
        dishes = df.to_records(index = False) 
    
    for index in range(len(dishes)): 
        a = dishes[index][1] 
        b = dishes[index][0] 
        if a == name or b == name or name == None: 
            edges.append({"data": {
                "frequency": dishes[index][2], 
                "source": dishes[index][1], 
                "target": dishes[index][0] 
            }}) 
    
    dish_names = set(map(lambda x: x["data"]["source"], edges)).union(set(map(lambda x: x["data"]["target"], edges))) 
        
    for name in dish_names: 
        nodes.append({"data": {
            "color": "lightblue", 
            "id": name, 
            "value": name, 
            "name": name 
        }}) 
    
    return {"nodes": nodes, "edges": edges} 


with open("food.json", "r") as file: 
    data = json.loads(file.read()) 


# data["elements"]["edges"] 


app = jupyter_dash.JupyterDash(__name__)
app.title = "Food Graph"
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


# with open('heroku_application/food.json', 'r') as f:
    # data = json.loads(f.read()) 
  
# https://github.com/plotly/dash-cytoscape/blob/master/demos/data/edge-types/cy-style.json
with open('../heroku_application/cy-style.json') as f:
    stylesheet = json.loads(f.read())

styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100get_ipython().run_line_magic("',", "")
        'width': '100get_ipython().run_line_magic("',", " ")
        "float": "left"
    },
    'cy-container': {
        'flex': '4',
        'position': 'relative'
    },
    'cytoscape': {
        'position': 'absolute',
        "x": "0px", 
        "y": "0px", 
        'width': '100get_ipython().run_line_magic("',", "")
        'height': '100get_ipython().run_line_magic("',", "")
        'z-index': 999
    }, 
}


# App
app.layout = html.Div([ 
    html.H1("What's on the menu? Let's give a lookget_ipython().getoutput(""), ")
    html.Div([  
    html.Div([ 
        html.H4("A specific dish? Choose hereget_ipython().getoutput(""), ")
        dcc.Dropdown( 
            id = "demo-dropdown", 
            options = [{"label": "Every foodget_ipython().getoutput("", "value": "null"}] + options")
        ), 
        # dcc.Graph(id = "barplot") 
    ], style = {"width": "32get_ipython().run_line_magic("",", " \"display\": \"inline-block\", \"float\": \"left\"}), ")
    html.Div([ 
        html.H5("Choose the quantity of nodes. (type 745 for all)"), 
        dcc.Input(id = "n", type = "number", value = 128, min = 1, max = 745, step = 1)  
    ], style = {"width": "32get_ipython().run_line_magic("",", " \"display\": \"inline-block\", \"float\": \"right\"}) ")
    ]), 
    html.Div(className='cy-container', style=styles['cy-container'], children=[
        cyto.Cytoscape(
            id='cytoscape',
            elements=cytoscape_data(),
            stylesheet=stylesheet,
            style=styles['cytoscape'],
            layout={
                'name': 'cose',
                'idealEdgeLength': 100,
                'nodeOverlap': 10,
                'refresh': 20,
                'fit': True,
                'padding': 200,
                'randomize': False,
                'componentSpacing': 100,
                'nodeRepulsion': 4000000,
                'edgeElasticity': 50,
                'nestingFactor': 5,
                'gravity': 80,
                'numIter': 1000,
                'initialTemp': 200,
                'coolingFactor': 0.95,
                'minTemp': 1.0,
                'minNodeSpacing': 100
            },
            responsive=True 
        ), 
    ]), 
    html.Div([ 
        html.Div([
            dcc.Graph(id = "barplot", figure = px.bar(height = 358)) 
        ], style = {"width": "38get_ipython().run_line_magic("",", " \"float\": \"left\", \"display\": \"inline-block\"}), ")
        html.Div([ 
            html.Div(id = "dish"), 
            html.Div(id = "dish_plot", children = [
                "***********************" 
            ]), 
            html.Div(id = "dish_year") 
        ], style = {"width": "16get_ipython().run_line_magic("",", " \"float\": \"left\", \"display\": \"inline-block\", ")
                    "margin-top": 49, "font-family": "Serif", "font-size": 25}), 
        html.Div([
            dcc.Graph(id = "lineplot", figure = px.line(height = 358)) 
        ], style = {"width": "38get_ipython().run_line_magic("",", " \"float\": \"left\", \"display\": \"inline-block\"}), ")
    ], style = {"width": "100get_ipython().run_line_magic("",", " \"height\": \"34%\"}), ")
], style=styles['container'])

@app.callback(Output(component_id = "cytoscape", component_property = "elements"), 
             [Input(component_id = "demo-dropdown", component_property = "value"), 
             Input(component_id = "n", component_property = "value")])   
def display_graph(value, n): 
    if value is not None and value get_ipython().getoutput("= "null": ")
        return cytoscape_data(name = value, n = 745) 
    else: 
        return cytoscape_data(n = n)     

@app.callback(Output(component_id = "barplot", component_property = "figure"), 
             [Input(component_id = "cytoscape", component_property = "tapNodeData")])   
def display_barplot(node): 
    name = node["id"] if node is not None else "bar" 
    if name == "bar": 
        return px.bar(height = 358)  
    df_node = df[df["name_x"] == name] 
    print(name) 
    fig = px.bar( 
        df_node, 
        x = "name_y", 
        y = "count", 
        height = 358 
    ) 
    fig.update_layout(
        xaxis_title = "Dish's name", 
        yaxis_title = "Count" 
    ) 
    return fig 

@app.callback(Output(component_id = "lineplot", component_property = "figure"), 
             [Input(component_id = "cytoscape", component_property = "tapNodeData")]) 
def display_lineplot(node): 
    name = node["id"] if node is not None else "line" 
    if name == "line": 
        return px.line(height = 358) 
    df_year_node = df_year[df_year["name_x"] == name] 
    fig = px.line(
        df_year_node, 
        x = "year", 
        y = "count" 
    ) 
    fig.update_layout(
        xaxis_title = "Year", 
        yaxis_title = "Count" 
    ) 
    return fig 

@app.callback(Output(component_id = "dish", component_property = "children"),  
             [Input(component_id = "cytoscape", component_property = "tapNodeData")]) 
def display_text(node): 
    if node is None: 
        return "Select a nodeget_ipython().getoutput("" ")
    else: 
        return "That's the dish you choose: {dish}. I love itget_ipython().getoutput("".format(dish = node["id"]) ")


@app.callback(Output(component_id = "dish_year", component_property = "children"), 
             [Input(component_id = "cytoscape", component_property = "tapNodeData")]) 
def display_dish_text(node): 
    if node is None: 
        return "A blue nodeget_ipython().getoutput("" ")
    else: 
        df_dish_node = df[df["name_x"] == node["id"]] 
        n = df_dish_node["count"].sum() 
        return "It appears on {n} menu{s}get_ipython().getoutput("".format(n = n, s = "" if n <= 1 else "s")   ")

if __name__ == "__main__": 
    app.run_server(debug = True,  port = 9999)  
