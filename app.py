# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import datetime
from click import style
from dash import Dash, html, dcc, Output, Input, dash_table, page_registry, page_container
from plotly import graph_objs as go
import pandas as pd
import dash_bootstrap_components as dbc
import pages_plugin,ta,graphs,EVR_Strategy

app = Dash(__name__,plugins=[pages_plugin],external_stylesheets=[dbc.themes.BOOTSTRAP])

def update_tickers_data():
    df = pd.read_csv(fr'check_time.csv', sep=',')
    csv_date = str(list(df["UpdateTime"])[-1])
    # csv_day = int(list(df["WeekDay"])[-1])
    csv_date = datetime.datetime.strptime(csv_date,"%Y-%m-%d %H")
    now_d = str(datetime.datetime.now().strftime("%Y-%m-%d %H"))
    now = (datetime.datetime.strptime(now_d,"%Y-%m-%d %H"))
    # now_w = str(datetime.datetime.now().weekday())
    c = (now-csv_date).total_seconds()
    if c >= 86400:
        t = csv_date + datetime.timedelta(days=int(c / 86400))
        t = t.strftime("%Y-%m-%d %H")
        EVR_Strategy.download_tickers()
        with open("check_time.csv", "w") as file:
            file.write("UpdateTime\n")
            file.write(f"{t}")
            file.close()
    else:
         pass
app.layout = html.Div([
    update_tickers_data(),
    html.H1("داشبورد کمک تریدر",style={"text-align":"center","font-family":"Vazir","margin-top":"10px"}),
	pages_plugin.page_container
])


@app.callback(
    Output('dd-output-container1', 'figure'),
    Input('demo-dropdown', 'value'),
    Input('radios', 'value'),

)
def update_output(value,value1):
    return graphs.Close_EMA(value,value1)

@app.callback(
    Output('dd-output-container2', 'figure'),
    Input('demo-dropdown', 'value'),
    Input('radios', 'value'),
)
def update_output2(value,value1):
    return graphs.RSI(value,value1)

@app.callback(
    Output('dd-output-container3', 'figure'),
    Input('demo-dropdown', 'value'),
    Input('radios', 'value'),
)
def update_output3(value,value1):
    return graphs.Vortex(value,value1)

@app.callback(
    Output('dd-output-container4', 'figure'),
    Input('demo-dropdown', 'value'),
    Input('radios', 'value'),
)
def update_output4(value,value1):
    return graphs.SP(value,value1)

@app.callback(
    Output('dd-output-container5', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output5(value):
    t = dbc.Row(children=[
        dbc.RadioItems(
            id="radios",
            className="btn-group",
            inputClassName="btn-check",

            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "همه", "value": 9999},
                {"label": "یک سال", "value": 365},
                {"label": "شش ماه", "value": 180},
                {"label": "سه ماه", "value": 90},
                {"label": "یک ماه", "value": 30},
                {"label": "یک هفته", "value": 7},
            ],
            value=9999,
            style={"margin-left":"10%","font-family":"Vazir","width":"50%"}
        ),
            html.H4(":تایم فریم",style={"font-family":"Vazir","margin-left":"20%","width":"20%"}),
])
    return t


@app.callback(
    Output('dd-output-container6', 'children'),
    Input('filter-strategy', 'value')
)
def filter_time_frame(value):
    buy = []
    buy_v = []
    buy_d = []
    for symbol in EVR_Strategy.all_tickers:
        df = pd.read_csv(fr'tickers_data/{symbol}.csv', sep=',')
        if value == 1:
            try:
                close = df["close"]
                indicator_rsi = ta.momentum.rsi(df["close"], 14)
                rsi_1 = list(indicator_rsi)[-1]
                rsi_2 = list(indicator_rsi)[-2]
                close_1 = list(close)[-1]
                close_2 = list(close)[-2]
                if rsi_2 <= 55:
                    if rsi_1 > 55:
                        buy.append(symbol)
                        n =(int(list(df["volume"])[-1]))
                        buy_v.append("{:,}".format(n))
                        buy_d.append((list(df["jdate"])[-1]))
            except:
                pass
        if value == 2:
            try:
                close = df["close"]
                indicator_ema = ta.trend.ema_indicator(df["close"], 50)
                ema_1 = list(indicator_ema)[-1]
                ema_2 = list(indicator_ema)[-2]
                close_1 = list(close)[-1]
                close_2 = list(close)[-2]
                if ema_2 >= close_2:
                    if ema_1 <= close_1:
                        buy.append(symbol)
                        n =(int(list(df["volume"])[-1]))
                        buy_v.append("{:,}".format(n))
                        buy_d.append((list(df["jdate"])[-1]))
            except:
                pass
            
    
    df = pd.DataFrame({
	"حجم": buy_v,
	"سهم": buy,
    "تاریخ": buy_d,
	})
    table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True,style={"text-align":"right"})
    print("finish")
    return table

# @app.callback(
#     Output('dd-output-container3', 'children'),
#     Input('demo-dropdown', 'value')
# )
# def update_output3(value):
#     return graphs.time_frame(value)

    #################################################################################################
    # fig = make_subplots(rows=2, cols=1)




if __name__ == '__main__':
    app.run_server(debug=True)
