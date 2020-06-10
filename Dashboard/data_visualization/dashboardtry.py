import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import base64

#introducing the dataframes
df_calls = pd.read_csv("data/MergedCalls.csv")
df_fm = pd.read_csv("data/MergedFMSplit.csv")
df_placements = pd.read_csv("data/MergedPlacements.csv")
df_contactid = pd.read_csv("data/MergedContactID+FM.csv")

#loading the images in the variable
icon1 = 'icons/1.png' 
encoded_image1 = base64.b64encode(open(icon1, 'rb').read())
icon2 = 'icons/2.png' 
encoded_image2 = base64.b64encode(open(icon2, 'rb').read())
icon3 = 'icons/3.png'
encoded_image3 = base64.b64encode(open(icon3, 'rb').read())
icon4 = 'icons/4.png' 
encoded_image4 = base64.b64encode(open(icon4, 'rb').read())
icon5 = 'icons/5.png'
encoded_image5 = base64.b64encode(open(icon5, 'rb').read())
icon6 = 'icons/6.png' 
encoded_image6 = base64.b64encode(open(icon6, 'rb').read())


#only the neccisary data
communication = df_calls[["Account Manager", "Date"]].head(3)
salary = df_contactid[['Job Contract Type', 'Start Date', 'End Date', 'Salary per Month']]
supervision = df_fm[["Time", "Day", "Month", "Year"]].head(2)
promotion = df_placements[["Job Description"]].dropna().head(3)
natureofwork = df_placements[['Placement: ID', 'Start Date', 'End Date']].head()

#items for the choice menu in jumbotron
items =[
        dbc.DropdownMenuItem("Professional 1"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Professional 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Professional 3")
    ]


#jumbotron = header
jumbotron = dbc.Jumbotron([
  html.H2("Measuring and monitoring job satisfaction", className="display-4"),
  html.Hr(),
  dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em', 'margin-left':'1em'}),    
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image6.decode()),style={'height':'3%', 'width':'3%', 'margin-right':'1em','margin-left':'1em'}),     
      ],
      justify="center"), 
  html.Hr(),
  dbc.DropdownMenu(
    items, label="Choose professional here", color="light", className="m-1",
    style={"display": "flex", "flexWrap": "wrap"}
  )
],
style={'margin-bottom': '1em', 'margin-left':'0.5em','margin-right':'0.5em'}
)

#info you need for deploying dashbaord
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
server = app.server

#the dashboard
dashboard = html.Div([
  dbc.Row([
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Communication", className="card-title"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      ("The last calls executed were: "),
      dbc.Table.from_dataframe(communication, striped=True, bordered=True, hover=True, dark=True)
    ]))])),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Supervision", className="card-title"),
      html.Hr(),
      html.H6("Supervision at Linden-IT:"),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),
       html.Hr(),
      html.H6("Supervision at customer:"),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),    
      html.Hr(),
      ("The FM history is: "),
      dbc.Table.from_dataframe(supervision, striped=True, bordered=True, hover=True, dark=True)
    ]))])),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Coworkers", className="card-title"),
      html.Hr(),
      html.H6("Coworkers at Linden-IT:"),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      html.H6("Coworkers at customer:"),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      html.H6("The next work activity: "),
      dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt(2020, 7, 3),
        first_day_of_week=1,
        display_format='DD-MM-Y',
      )
    ]))])),
     dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Salary", className="card-title"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      ("Information about the contract: "),
      dbc.Table.from_dataframe(salary, striped=True, bordered=True, dark=True)
    ]))])),
  ],
    justify="center",
    style={'margin-bottom': '1em', 'margin-left':'0.5em','margin-right':'0.5em'}
  ),

  dbc.Row([
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Nature of work", className="card-title"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      ("Last placements were at: "),
      html.H6("*Another nice visual here*")
      #visual here
    ]))])),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([ 
      html.H5("Fringe benefits", className="card-title"),
      dbc.Button("More info", id="alert-toggle-auto", color="light", size="sm", className="mr-1"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      dbc.Alert(
        "Examples of fringe benefits are: medical insurance, vacation pay, company car, or meals.",
        id="alert-auto",
        is_open=False,
        duration=4000,
        dismissable=True,
        color="primary"
        ),
      ("The professional makes use of: "),
      dbc.FormGroup([
        dbc.Label(""),
        dbc.Checklist(
          options=[
            {"label": "Company car", "value": 1},
            {"label": "CBTnuggets", "value": 2},
            {"label": "Talentpool", "value": 3}
          ],
          id="switches-input",
          inline=True,
          switch=True,
          value=[2]
        ),
      ])
    ]))])),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
    html.H5("Contingent rewards", className="card-title"),
    dbc.Button("More info", id="alert-toggle-no-fade", className="mb-1", color="light", size="sm"),
    html.Hr(),
    dbc.Row([
      html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
      html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
      html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
    dbc.Alert(
       "Contingent rewards systems are motivation-based systems that are used to reward those that meet their identified goals.",
      id="alert-no-fade",
      dismissable=True,
      duration=4000,
      fade=False,
      is_open=False,
      color="primary"
      ),
    ("The professional feels: "),
    html.H6("*Another nice visual here*")
    #visual here
    ]))])),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Promotion", className="card-title"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      ("the historical placements are: "),
      dbc.Table.from_dataframe(promotion, striped=True, bordered=True, hover=True, dark=True)
    ]))])),
  ],
    justify="center",
    style={'margin-bottom': '1em', 'margin-left':'0.5em','margin-right':'0.5em'}
  ),

  dbc.Row([
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Operating conditions", className="card-title"),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center"),  
      html.Hr(),
      ("The last call was made on: "),
      html.H6("Another nice visual here")
      #visual here
    ]))]),
    width=3
    ),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("SwLS", className="card-title"),
      ("Life satisfaction: "),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em','margin-left':'1em'}),      
        html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),style={'height':'15%', 'width':'15%', 'margin-right':'1em', 'margin-left':'1em'})    
      ],
      justify="center")
    ]))]),
    width=3
    ),
    dbc.Col(html.Div([dbc.Card(dbc.CardBody([
      html.H5("Overall Satisfaction Score", className="card-title"),
      dbc.Button("Explanation", id="open-centered", color="light", size="sm", className="mr-1"),
      dbc.Modal(
          [
            dbc.ModalHeader("How was the score composed?"),
            dbc.ModalBody("The overall score is based on all the facets seen in this dashboard"),
            dbc.ModalFooter(
              dbc.Button(
                "Close", id="close-centered", className="ml-auto", color="primary"
                )
              ),
          ],
            id="modal-centered",
            centered=True
        ),
      html.Hr(),
      dbc.Row([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),style={'height':'20%', 'width':'20%', 'margin-right':'1em', 'margin-left':'1em'}),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),style={'height':'20%', 'width':'20%', 'margin-right':'1em', 'margin-left':'1em'})
      ],
      justify="center"),  
      html.Hr(),
      html.H6("Average score: 3.9")
      #visual here
    ]))])),
  ],
    justify="center",
    style={'margin-bottom': '1em', 'margin-left':'0.5em','margin-right':'0.5em'}
  ),
])

#for the 'More info' button for fringe benefits
@app.callback(
    Output("alert-auto", "is_open"),
    [Input("alert-toggle-auto", "n_clicks")],
    [State("alert-auto", "is_open")]
)

#for the 'More info' button for Fringe benefits
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open

#for the 'More info' button for Contingent rewards
@app.callback(
    Output("alert-no-fade", "is_open"),
    [Input("alert-toggle-no-fade", "n_clicks")],
    [State("alert-no-fade", "is_open")],
)

#for the 'More info' button for Contingent rewards
def toggle_alert_no_fade(n, is_open):
    if n:
        return not is_open
    return is_open

#for the 'More info' button for Overall happiness
@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")]
)

#for the 'More info' button for Overall happiness
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#show the made layout
app.layout = html.Div([jumbotron, dashboard])

#command to run on the server
if __name__ == "__main__":
  app.run_server(debug=True)
  