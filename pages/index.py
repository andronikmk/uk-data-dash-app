# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Machine Learning on Economic Data

            ✅ This is an app that uses economic data 
            to predict real consumption earnings growth in England and Great Britain, 1270 - 1870.


            """
        ),
        dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)

df1 = pd.read_csv('data/uk_pop_gdp_v2.csv')

# plot 1
fig = go.Figure()

# adding subplots
fig.add_trace(go.Scatter(x=df1['date'], y=df1['real_gdp'],
                    mode='lines',
                    name='Real GDP'))

fig.add_trace(go.Scatter(x=df1['date'], y=df1['gdp_per_head'],
                    mode='lines',
                    name='Real GDP per head'))

fig.add_trace(go.Scatter(x=df1['date'], y=df1['population'],
                    mode='lines',
                    name='Population'))

fig.update_layout(xaxis_type="log", yaxis_type="log")

fig.update_layout( 
    title='England and Great Britain: Real GDP, Real GDP per head and Population, 1270-1870',
    
    font=dict(
        size=12,
        color="#7f7f7f"
    ),
    
    xaxis=dict(
        title='Year',
        showticklabels=True,
        zeroline=False,
        ),
    
    yaxis=dict(
        title='Indexed value (1700 = 100)',
        zeroline=False,
        showticklabels=False,
       )
    )

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])