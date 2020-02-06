# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd
import numpy as np
import pandas as pd

# Imports from this application
from app import app

pipeline = load('assets/pipeline.joblib')
print(type(pipeline))
print('Hello, World')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
         html.H3('Predictions', className='mb-5'), 
         html.H4('Year'), 
         dcc.Slider(
             id='year', 
             min=1270, 
             max=1870, 
             step=70, 
             value=2020, 
             marks={n: str(n) for n in range(1270,1870,70)}, 
             className='mb-5', 
             ), 
        html.H4('Annual Inflation Rate'),
        dcc.Slider(
            id='inflation', 
            min=-50, 
            max=50, 
            step=10, 
            value=0, 
            marks={n: str(n) for n in range(-50,50,10)}, 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H3('Real Consumption Earnings', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)


layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('year', 'value'), Input('inflation', 'value')],
)
def predict(Year, Annual_inflation_rate):
    df = pd.DataFrame(
        columns=['Year', 'Annual_inflation_rate'], 
        data=[[Year, Annual_inflation_rate]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} Years'
