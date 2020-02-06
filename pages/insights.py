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


# import dataframe
df = pd.read_csv('https://raw.githubusercontent.com/andronikmk/uk-data-dash-app/master/data/uk_data_v7.csv')

# plot 1 and 2
fig1 = go.Figure()
fig2 = go.Figure()

fig1.add_trace(go.Scatter(x=df['Year'], y=df['Beef_Million_Lbs'],
                    mode='lines',
                    name='Beef'))
fig1.add_trace(go.Scatter(x=df['Year'], y=df['Veal_Million_Lbs'],
                    mode='lines',
                    name='Veal'))
fig1.add_trace(go.Scatter(x=df['Year'], y=df['Mutton_Million_Lbs'],
                    mode='lines',
                    name='Mutton'))
fig1.add_trace(go.Scatter(x=df['Year'], y=df['Pork_Million_Lbs'],
                    mode='lines',
                    name='Pork'))
fig1.add_trace(go.Scatter(x=df['Year'], y=df['Wool_Million_Lbs'],
                    mode='lines',
                    name='Wool'))
fig1.add_trace(go.Scatter(x=df['Year'], y=df['Hides_Million_Lbs'],
                    mode='lines',
                    name='Hides'))
fig1.update_layout(xaxis_type="log", yaxis_type="log")

# plot settings
fig1.update_layout(
    title="England and Great Britain Total Output of Livestock Products, 1270-1870",
    xaxis_title="Year",
    yaxis=dict(
        title='Millions of Pounds',
        zeroline=False,
        showticklabels=False,
       ),
    font=dict(
        color="#7f7f7f"
    )
)

# adding subplots
fig2.add_trace(go.Scatter(x=df['Year'], y=df['Wheat_Million_Bushels'],
                    mode='lines',
                    name='Wheat'))
fig2.add_trace(go.Scatter(x=df['Year'], y=df['Rye_Million_Bushels'],
                    mode='lines',
                    name='Rye'))
fig2.add_trace(go.Scatter(x=df['Year'], y=df['Barley_Million_Bushels'],
                    mode='lines',
                    name='Barley'))
fig2.add_trace(go.Scatter(x=df['Year'], y=df['Oats_Million_Bushels'],
                    mode='lines',
                    name='Oats'))
fig2.add_trace(go.Scatter(x=df['Year'], y=df['Pulses_Million_Bushels'],
                    mode='lines',
                    name='Legume'))

# plot settings
fig2.update_layout(
    title="England and Great Britain Agricultural Production, 1270-1870",
    xaxis_title="Year",
    yaxis_title="Millions of Bushels",
    font=dict(
        color="#7f7f7f"
    )
)

fig3 = go.Figure()
# Add traces
fig3.add_trace(go.Scatter(x=df['Year'], y=df['Cattle_Million'],
                    mode='lines',
                    name='Chattle'))
fig3.add_trace(go.Scatter(x=df['Year'], y=df['Sheep_Million'],
                    mode='lines',
                    name='Sheep'))
fig3.add_trace(go.Scatter(x=df['Year'], y=df['Pigs_Million'],
                    mode='lines',
                    name='Pig'))

# x-axis range
# fig3.update_xaxes(range=[1550, 1870])


fig3.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 200,
        dtick = 100
    )
)

# plot settings
fig3.update_layout(
    title="England and Great Britain Livestock, 1270-1870",
    xaxis_title="Year",
    yaxis_title="Number of Animals (Millions)",
    font=dict(
        color="#7f7f7f"
    )
)

fig4 = px.bar(df, x='Year', y='Total_Arable_and_Sown_Acreage', color='Year',color_continuous_scale='Bluered_r')

# plot settings
fig4.update_layout(
    title="Total Arable and Sown Acreage, 1270-1870",
    xaxis_title="Year",
    yaxis_title="Millions of Acres",
    font=dict(
        color="#7f7f7f"
    )
)

column1 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig3)
    ]
)



layout = dbc.Row([column1])