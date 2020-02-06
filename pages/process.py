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

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Div(
            """        
            Output of the industrial and service sectors achieved their late 
            medieval peaks at the opening of the fourteenth century and thereafter
            contracted respectfully over this same period as the population halved.
            Between 1450 and 1700 English industrial output grew more than five-fold, 
            while output per head doubled. This is largely due to structural redistribution 
            of labor from agriculture to industry. Output grew consistently faster than the 
            population throughout the sixteenth century, as metal and mining output fluctuated 
            but nevertheless held up well, while textile production prospered, and the 
            Reformation boosted demand for the printed book.

            """
        ,style={'width': '100%', 'textAlign': 'justify'}),

    ],md=4,
)

# import dataframe
df = pd.read_csv('https://raw.githubusercontent.com/andronikmk/uk-data-dash-app/master/data/uk_data_v7.csv')

# plot 2
fig = go.Figure()

# adding subplots
fig.add_trace(go.Scatter(x=df['Year'], y=df['Tin_Output'],
                    mode='lines',
                    name='Tin'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Iron_Output'],
                    mode='lines',
                    name='Iron'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Coal_Output'],
                    mode='lines',
                    name='Coal'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Wool_Textile_Output'],
                    mode='lines',
                    name='Wool and Textile'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Leather_Output'],
                    mode='lines',
                    name='Leather'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Foodstuffs_Output'],
                    mode='lines',
                    name='Foodstuffs'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Construction_Output'],
                    mode='lines',
                    name='Construction'))
fig.add_trace(go.Scatter(x=df['Year'], y=df['Printed_Books_Output'],
                    mode='lines',
                    name='Printed Books'))


fig.update_layout(xaxis_type="log", yaxis_type="log")

# plot settings
fig.update_layout( 
    title='England and Great Britain Industrial Production, 1270-1870',
    
    font=dict(
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