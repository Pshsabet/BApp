#---------------------------------------- REVIEW Packages ----------------------------------------#
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import materialdashboard as md
import EVR_Strategy
#---------------------------------------- REVIEW Layout ----------------------------------------#
#################################################################################################


#################################################################################################
dropdown = html.Div(style={"width":"80%","text-alignment":"center","margin-left":"10%","font-family":"Vazir"},children=[dcc.Dropdown(EVR_Strategy.all_tickers, placeholder= "سهم مورد نظر خود را انتخاب نمایید" , id='demo-dropdown',style={'textAlign':"right", 'direction':'rtl', "margin-bottom":"15px","margin-top":"5%"},clearable=False)])
# md.Stack(
#     direction="row",
#     style={"justify-content": "space-around","width":"100%"},
#     children=[


        # html.H4(":تایم فریم",style={"font-family":"Vazir","margin-left":"0%"})
#################################################################################################

card = md.Stack(
    
    spacing=2,
    children=[
    md.Card(children=[
    md.Typography(children=["dfgdg"],variant="h1"),
    html.H4("P/E: 10.25"),
    html.H4("EPS: 24.25"),
    html.H4("volume: 10.25"),
],
    style={"width":"500px","margin-top":"10px"},
    ),
    html.Div([md.Card(children=[
    md.Typography(children=["dfgdg"],variant="h1"),
    html.H4("P/E: 10.25"),
    html.H4("EPS: 24.25"),
    html.H4("volume: 10.25"),
],
    style={"width":"500px","margin-top":"10px","text-align":"right"},
    )],style={"alignment":"right"})
    ],
    direction="column")

card2 = md.Stack(
    
    spacing=2,
    children=[
    md.Card(children=[
    md.Typography(children=["dfgdg"],variant="h1"),
    html.H4("P/E: 10.25"),
    html.H4("EPS: 24.25"),
    html.H4("volume: 10.25"),
],
    style={"width":"500px","margin-top":"10px"},
    ),
    html.Div([md.Card(children=[
    md.Typography(children=["dfgdg"],variant="h1"),
    html.H4("P/E: 10.25"),
    html.H4("EPS: 24.25"),
    html.H4("volume: 10.25"),
],
    style={"width":"500px","margin-top":"10px","text-align":"right"},
    )],style={"alignment":"right"})
    ],
    direction="column")

cards = md.Stack(children=[card,card2],direction="row")






#---------------------------------------- REVIEW Dash App ----------------------------------------#
dash.register_page(__name__,
    path='/',
	name='Analytic Apps',
	description='Welcome to my app',
    image='bird.jpeg',
	redirect_from=['/old-home-page', '/v2'],
	extra_template_stuff='yup')

def layout():
	return html.Div(children=[
        dropdown,
              html.Div(
        id='dd-output-container5',
    ),
        html.Div(dcc.Graph(
        id='dd-output-container1',
    )),
        html.Div(dcc.Graph(
        id='dd-output-container2',
    )),
        html.Div(dcc.Graph(
        id='dd-output-container3',
    )),
        html.Div(dcc.Graph(
        id='dd-output-container4',
    )),
    ],style={"background-color":"#ffffff"})
# a_csv = pd.read_csv('a.csv')
# download_tickers()
# cr = Cross_RSI_14()

# fig = px.line(df, x="قیمت", y="نام سهم")
# fig.add_trace(go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[1,3,6,11,16,20,17,11,6,1], name="stDev"))

    # columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'نام سهم' else {'id': x, 'name': x} for x in df.columns],
    # style_data={
    #     'color': '#616161',
    #     'backgroundColor': 'white',
    #     'whiteSpace': 'normal',
    #     'height': 'auto',
    #     'textAlign': 'center',
    #     # 'width':'100%'
    # },
    # fill_width=True,
    # style_data_conditional=[
    #     {
    #         'if': {'row_index': 'odd'},
    #         'backgroundColor': '#f8f7ff',
    #         'textAlign': "right",

    #     }
    # ],
    # style_header={
    #     'textAlign': "right",
    #     'backgroundColor': '#6d7ae0',
    #     'color': 'white',
    #     'fontWeight': 'bold',
    # },
    # style_as_list_view=True,

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),
#     html.Div(children='''
#         Dash: A web application framework for your data.
#     ''',style={"color":"#ffffff"}),
#     dcc.Dropdown(['اخابر', 'خودرو', 'ذوب'], placeholder= "سهم مورد نظر خود را انتخاب نمایید" , id='demo-dropdown',style={'textAlign':"right", 'direction':'rtl'}),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     ),
#     daq.Gauge(
#         color={"gradient":True,"ranges":{"green":[0,60],"yellow":[60,120],"red":[120,220]}},
#         id='my-gauge-1',
#         label="Default",
#         scale={'start': 0, 'interval': 1, 'labelInterval': 20},
#         min = 0,
#         max = 220,
#         showCurrentValue=True,
#         units="KM/h",
#     ),
#     dcc.Slider(
#         id='my-gauge-slider-1',
#         min=0,
#         max=220,
#         value=0
#     ),  
# ])



# @app.callback(Output('my-gauge-1', 'value'), Input('my-gauge-slider-1', 'value'))
# def update_output(value):
#     return value

