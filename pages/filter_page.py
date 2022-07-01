import dash
from dash import html, dcc
import pandas as pd
import ta
import EVR_Strategy
import dash_bootstrap_components as dbc
# app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


dash.register_page(__name__,path="/b",title="fdgvd",image='bird.jpeg')



button = dbc.Row(children=[
        dbc.RadioItems(
            id="filter-strategy",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "IE استراتژی", "value": 2},
                {"label": "RSI استراتژی", "value": 1},
            ],
            value=1,
            style={"margin-left":"10%","font-family":"Vazir","width":"50%"}
        ),
            html.H4(":تایم فریم",style={"font-family":"Vazir","margin-left":"20%","width":"20%"}),
])


def layout():
	return html.Div(children=[
		button,
		html.Div(id= "dd-output-container6"
		)
		# Cross_RSI_14()
	])

# table_header = [
#     html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
# ]

# row1 = html.Tr([html.Td("Arthur"), html.Td(html.A("GFGHTRH", href="https://www.yahoo.com", target='_blank'),style={'text-color':'#ffffff','text-align':"right"})])
# exec("row2 = html.Tr([html.Td('Ford'), html.Td('Prefect')])")
# row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
# row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])
# table_body = [html.Tbody([row1, row2, row3, row4])]
# dbc.Table(table_header + table_body, bordered=True,
#     dark=True,
#     hover=True,
#     responsive=True,
#     striped=True,)
