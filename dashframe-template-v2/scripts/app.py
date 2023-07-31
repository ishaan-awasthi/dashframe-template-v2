'''------IMPORTS------'''
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import plotly.io as io
io.templates.default = 'plotly_dark'

'''------INCORPORATING DATA------'''
heart = pd.read_csv('../data/heart.csv') #target csv file
spo2 = pd.read_csv('../data/spo2.csv')
sleep = pd.read_csv('../data/sleep.csv')
steps = pd.read_csv('../data/steps.csv')
app = Dash(__name__) #dash constructor to initialize site


'''------INITIALIZING PLOTS------'''
line = px.line(heart, x='Time', y='Rate') #HEART
bar = px.bar(steps, x='Day', y='Steps', color='Day') #STEPS
polar = px.bar_polar(sleep, r='Hours', theta='Day', color='Day')#, color='Time') #SLEEP
scatter = px.scatter(spo2, x='Time', y='Rate', color='Rate') #SPO2


'''------GRAPHING PLOTS------'''
app.layout = html.Div([ #create layout of site
    #html.Meta(httpEquiv="refresh", content="10"),
    html.Div(dcc.Graph(figure=bar), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=line), style={'display': 'inline-block'},),
    html.Div(html.P('COMPANY NAME'), style={'textAlign': 'center', 'color':'lightpink', 'fontSize': '30px'},),
    html.Div(dcc.Graph(figure=polar), style={'display': 'inline-block'},),
    html.Div(dcc.Graph(figure=scatter), style={'display': 'inline-block'},),
], style={'textAlign': 'center', 'backgroundColor':'black', 'margin-top':'0px', 'margin-left':'0px', 'margin-right':'0px', 'margin-bottom':'0px'})


'''------RUN SITE------'''
if __name__ == '__main__': #runs site if script is called directly through command-line
    app.run_server(debug=True)
    print
# Export to localhost http://127.0.0.1:8050/
# Run 'python app.py'