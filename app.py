import json
import dash
# import urllib.request 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_cytoscape as cyto 
import nx_graph 
import plotly.io as pio 

import pandas as pd 
import numpy as np 

import networkx as nx 

import plotly.express as px 

# from IPython.display import Javascript 

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
            edges.append({ 
                "value": dishes[index][2], 
                "source": dishes[index][1], 
                "target": dishes[index][0] 
            }) 
    
    dish_names = set(map(lambda x: x["source"], edges)).union(set(map(lambda x: x["target"], edges))) 
        
    for name in dish_names: 
        nodes.append({
            "color": "lightblue", 
            "id": name, 
            "value": name, 
            "name": name, 
            "group": 1 
        }) 
    
    return {"nodes": nodes, "links": edges} 

def get_barplot(name, type): 
    df_node = df[(df["name_x"] == name) | (df["name_y"] == name)].to_records(index = False) 
    array = [] 
    for index in range(len(df_node)): 
        if df_node[index][0] == name: 
            array.append((df_node[index][0], df_node[index][1], df_node[index][2])) 
        else: 
            array.append((df_node[index][1], df_node[index][0], df_node[index][2]))  
    df_node = pd.DataFrame(array, columns = ["node", "dish", "count"])  
    
    if type == "bar": 
        figure = px.bar(
            df_node, 
            x = "dish", 
            y = "count", 
            height = 358 
        ) 
        
        figure.update_layout(
            xaxis_title = "Dish's name", 
            yaxis_title = "Count" 
        ) 
        
        return figure 
    elif type == "n": 
        return sum(list(map(lambda x: x[2], array))) 
        
app = dash.Dash(__name__) 
app.title = "Food Graph"
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


# with open('heroku_application/food.json', 'r') as f:
    # data = json.loads(f.read()) 
pio.templates.default = "plotly_white" 
# https://github.com/plotly/dash-cytoscape/blob/master/demos/data/edge-types/cy-style.json
# with open('../heroku_application/cy-style.json') as f: 
#    stylesheet = json.loads(f.read())

# App 
app.layout = html.Div([ 
    html.H1("What's on the menu? Let's give a look!"), 
    html.Div([  
    html.Div([ 
        html.H4("A specific dish? Choose here!"), 
        dcc.Dropdown( 
            id = "demo-dropdown", 
            options = [{"label": "Every food!", "value": "null"}] + options
        ), 
        # dcc.Graph(id = "barplot") 
    ], style = {"width": "32%", "display": "inline-block", "float": "left"}), 
    html.Div([ 
        html.H5("Choose the quantity of nodes. (type 745 for all)"), 
        dcc.Input(id = "n", type = "number", value = 128, min = 1, max = 745, step = 1)  
    ], style = {"width": "32%", "display": "inline-block", "float": "right"}) 
    ]), 
    html.Div(children=[ 
        nx_graph.NX(id = "cytoscape", data = cytoscape_data())  
    ], style = {"width": "100%", "height": "100%", "float": "center"}), 
    html.Div([ 
        html.Div([
            dcc.Graph(id = "barplot", figure = px.bar(height = 358)) 
        ], style = {"width": "38%", "float": "left", "display": "inline-block"}), 
        html.Div([ 
            html.Div(id = "dish"), 
            html.Div(id = "dish_plot", children = [
                dcc.Markdown("--" * 38) 
            ]), 
            html.Div(id = "dish_year") 
        ], style = {"width": "16%", "float": "left", "display": "inline-block", 
                    "margin-top": 49, "font-family": "Serif", "font-size": 25, "text-align": "center"}), 
        html.Div([
            dcc.Graph(id = "lineplot", figure = px.line(height = 358)) 
        ], style = {"width": "38%", "float": "left", "display": "inline-block"}), 
    ], style = {"width": "100%", "height": "34%"}), 
])

@app.callback(Output(component_id = "cytoscape", component_property = "data"), 
             [Input(component_id = "demo-dropdown", component_property = "value"), 
             Input(component_id = "n", component_property = "value")])   
def display_graph(value, n): 
    if value is not None and value != "null": 
        return cytoscape_data(name = value, n = 745) 
    else: 
        return cytoscape_data(n = n)     

@app.callback(Output(component_id = "barplot", component_property = "figure"), 
             [Input(component_id = "cytoscape", component_property = "tapNode")])   
def display_barplot(node): 
    name = node["name"] if node is not None else "bar" 
    if name == "bar": 
        return px.bar(height = 358)  
    return get_barplot(name = node["name"], type = "bar") 
    
@app.callback(Output(component_id = "lineplot", component_property = "figure"), 
             [Input(component_id = "cytoscape", component_property = "tapNode")]) 
def display_lineplot(node): 
    name = node["name"] if node is not None else "line" 
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
             [Input(component_id = "cytoscape", component_property = "tapNode")]) 
def display_text(node): 
    if node is None: 
        return "Select a node!" 
    else: 
        return "That's the dish you choose: {dish}. I love it!".format(dish = node["name"])   


@app.callback(Output(component_id = "dish_year", component_property = "children"), 
             [Input(component_id = "cytoscape", component_property = "tapNode")]) 
def display_dish_text(node): 
    if node is None: 
        return "A blue node!" 
    else: 
        n = get_barplot(name = node["name"], type = "n") 
        return "It appears on {n} menu{s}!".format(n = n, s = "" if n <= 1 else "s")   
 
if __name__ == "__main__": 
    app.run_server(debug = True,  port = 9999)   
