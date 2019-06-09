import json

# Plotting tools
import plotly 
from IPython.display import Image 
import plotly.plotly as py
import plotly.graph_objs as go

# credentials from json file
with open("plotly_credentials.json", "r") as file:  
    creds = json.load(file)

# API access to plotting tools
plotly.tools.set_credentials_file(username=creds['username'], api_key =creds['password'])

# Plotting bar chart with two groups
def plot2bar(bar1, name1, bar2, name2, x_in, title, xaxis, yaxis, filename_, rgba='rgba(255,128,0,0.9)'):
    trace1 = go.Bar(
        x    = x_in,
        y    = bar1,
        name = name1,
    )

    trace2 = go.Bar(
        x    = x_in,
        y    = bar2,
        name = name2,
        marker = dict(
            color = rgba,
        )
    )
 
    data = [trace1,trace2]
    layout= go.Layout(
        barmode='group',
        title=title,
        xaxis=dict(
            title=xaxis
        ),
        yaxis=dict(
            title=yaxis
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, sharing='public', filename=filename_)

# Plotting bar chart with two groups
def plot3bar(bar1, name1, bar2, name2, bar3, name3, x_in, title, xaxis, yaxis, filename_, rgba='rgba(255,128,0,0.9)'):
    trace1 = go.Bar(
        x    = x_in,
        y    = bar1,
        name = name1,
    )

    trace2 = go.Bar(
        x    = x_in,
        y    = bar2,
        name = name2,
        marker = dict(
            color = 'rgba(255,128,0,0.9)',
        )
    )
 
    trace3 = go.Bar(
        x    = x_in,
        y    = bar3,
        name = name3,
        marker = dict(
            color = 'rgba(0,128,255,0.9)',
        )
    )

    data = [trace1,trace2, trace3]
    layout= go.Layout(
        barmode='group',
        title=title,
        xaxis=dict(
            title=xaxis
        ),
        yaxis=dict(
            title=yaxis
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, sharing='public', filename=filename_)

def plotline(valueList, years):
    data = []

    for item in valueList:
        yy = item

        # Create a trace
        trace = go.Scatter(
            x = years,
            y = yy
        )

        data.append(trace)

    py.iplot(data, filename='basic-line.png')