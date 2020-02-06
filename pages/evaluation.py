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

# import dataframe
df = pd.read_csv('https://raw.githubusercontent.com/andronikmk/uk-data-dash-app/master/data/uk_data_v7.csv')

# plot 1 and 2
fig1 = go.Figure()

# plot 1
fig1 = px.scatter(df, x = 'Year', y='Annual_inflation_rate')

# plot settings
fig1.update_layout(
    title=" England and Great Britain Annual Inflation Rate, 1270-1870",
    xaxis_title="Year",
    yaxis_title="Percent",
    font=dict(
        size=10,
        color="#7f7f7f"
    )
)


fig2 = go.Figure()

# plot 2
fig2 = px.scatter(df, x = 'Year', y='Real_consumption_earnings_Growth_GB')

# plot settings
fig2.update_layout(
    title="England and Great Britain Real Consumption Earnings, 1270-1870",
    xaxis_title="Year",
    yaxis_title="Percent",
    font=dict(
        size=10,
        color="#7f7f7f"
    ),
)
# Add trace with large marker
fig2.update_traces(marker=dict(size=7,color='palegoldenrod',
                              line=dict(width=1,
                                        color='black')),
                  selector=dict(mode='markers'))


# Add trace with large marker
fig1.update_traces(marker=dict(size=7,
                              line=dict(width=1,
                                        color='black')),
                  selector=dict(mode='markers'))



column1 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
    ],
    md=6,
)

column2 = dbc.Col(
    [
         dcc.Graph(figure=fig2),
    ],md=6
)

layout = dbc.Row([column1, column2])