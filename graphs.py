from datetime import date
from plotly import graph_objs as go
import pandas as pd, ta
import dash_bootstrap_components as dbc
from dash import html, dcc
import materialdashboard as md


def Close_EMA(value,value1):
    ticker = pd.read_csv(f'tickers_data\{value}.csv')
    indicator_ema = ta.trend.ema_indicator(ticker["close"], 50).round(0)
    indicator_ichimoku_b = ta.trend.ichimoku_base_line(ticker["high"],ticker["low"], window1=9, window2=26).round(0)
    layout = go.Layout(
        showlegend = True,
        hovermode  = 'x',
        spikedistance =  -1,
        title=f"نمودار سهم {value}",
        titlefont= {"family":"Vazir","size":20,"color":"#000000"},
        font={"family":"Vazir","size":10,"color":"#000000"},

    xaxis=dict(        
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikethickness = 1,
        spikedash = "dash",
        #("solid", "dot", "dash", "longdash", "dashdot", or
                # "longdashdot") or a dash length list in px (eg
                # "5px,10px,2px,2px")
        spikemode  = 'across',
        ticklabelposition = 'outside bottom',
        tickformat = "%Y-%m-%d",
        spikecolor = "rgb(117, 117, 117)",

        # spikesnap = 'cursor',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        # showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikemode  = 'across',
        spikethickness = 1,
        spikedash = "dash",
        spikecolor = "rgb(117, 117, 117)",
        type = "log",
        tickformat = "000",
    ),

    )
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = ticker["close"][-value1::],
    name = "قیمت سهم",
    # hoverinfo= 'y',
    opacity=1,
    mode = 'lines',
        line = dict(
        color = ('rgb(2, 12, 245)'),
        width = 2,
        ), 
    ))
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = indicator_ema[-value1::],
    name = "EMA 50",
    # hoverinfo= 'y',
    opacity=1,
    mode = 'lines',
        line = dict(
        color = ('rgb(117, 117, 117)'),
        width = 2,
        ), 
    ))
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = indicator_ichimoku_b[-value1::],
    name = "Ichimoku Base Line",
    # hoverinfo= 'y',
    opacity=1,
    mode = 'lines',
        line = dict(
        color = ('#a24d4d'),
        width = 2,
        ), 
    ))
    print(value1)
    return fig

def RSI(value,value1):
    ticker = pd.read_csv(f'tickers_data\{value}.csv')
    line_length = ticker["date"]
    indicator = ta.momentum.rsi(ticker["close"], 14).round(0)

    layout = go.Layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        showlegend = True,
        hovermode  = 'x',
        spikedistance =  -1,
        title= {
            'text' : f"{value} RSI شاخص",
            'x':0.5,
            'xanchor': 'center'
        },
        
        titlefont= {"family":"Vazir","size":20,"color":"#000000"},
        font={"family":"Vazir","size":10,"color":"#000000"},

    xaxis=dict(        
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikethickness = 1,
        spikedash = "dash",
        #("solid", "dot", "dash", "longdash", "dashdot", or
                # "longdashdot") or a dash length list in px (eg
                # "5px,10px,2px,2px")
        spikemode  = 'across',
        ticklabelposition = 'outside bottom',
        tickformat = "%Y-%m-%d",
        spikecolor = "rgb(117, 117, 117)"

        # spikesnap = 'cursor',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        # showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikemode  = 'across',
        spikethickness = 1,
        spikedash = "dash",
        spikecolor = "rgb(117, 117, 117)",
        # type = "log",
        # tickformat = "000"
    ),
    )
    fig = go.Figure(layout=layout)
    
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = indicator[-value1::],
    name = "RSI",
    # hoverinfo= 'y',
    opacity=0.9,
    mode = 'lines',
        line = dict(
        color = ('#9c3587'),
        width = 2,
        ), 
    ))

    fig.add_shape(type='line',
    opacity=1,
                x0=list(ticker["date"][-value1::])[0],
                y0=50,
                x1=list(ticker["date"][-value1::])[-1],
                y1=50,
                line=dict(color='#D50000',dash="dash"),
                xref='x',
                yref='y'
    )
    fig.add_shape(type='line',
                x0=list(ticker["date"][-value1::])[0],
                y0=55,
                x1=list(ticker["date"][-value1::])[-1],
                y1=55,
                line=dict(color='#D50000',dash="dash"),
                xref='x',
                yref='y'
    )
    # data= [close,ema]
    # return dict(data=data, layout=layout)
    return fig

def Vortex(value,value1):
    ticker = pd.read_csv(f'tickers_data\{value}.csv')
    line_length = ticker["date"]
    vortex_indicator_p = list(ta.trend.vortex_indicator_pos(ticker["high"], ticker["low"], ticker["close"], 24))
    vortex_indicator_n = list(ta.trend.vortex_indicator_neg(ticker["high"], ticker["low"], ticker["close"], 24))


    layout = go.Layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        showlegend = True,
        hovermode  = 'x',
        spikedistance =  -1,
        title= {
            'text' : f"{value} Vortex شاخص",
            'x':0.5,
            'xanchor': 'center'
        },
        
        titlefont= {"family":"Vazir","size":20,"color":"#000000"},
        font={"family":"Vazir","size":10,"color":"#000000"},

    xaxis=dict(        
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikethickness = 1,
        spikedash = "dash",
        #("solid", "dot", "dash", "longdash", "dashdot", or
                # "longdashdot") or a dash length list in px (eg
                # "5px,10px,2px,2px")
        spikemode  = 'across',
        ticklabelposition = 'outside bottom',
        tickformat = "%Y-%m-%d",
        spikecolor = "rgb(117, 117, 117)"

        # spikesnap = 'cursor',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        # showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikemode  = 'across',
        spikethickness = 1,
        spikedash = "dash",
        spikecolor = "rgb(117, 117, 117)",
        # type = "log",
        # tickformat = "000"
    ),
    )
    fig = go.Figure(layout=layout)
    
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = vortex_indicator_p[-value1::],
    name = "VI +",
    # hoverinfo= 'y',
    opacity=0.9,
    mode = 'lines',
        line = dict(
        color = ('#01579B'),
        width = 2,
        ), 
    ))
    fig.add_trace(go.Scatter(
    x = ticker["date"][-value1::],
    y = vortex_indicator_n[-value1::],
    name = "VI -",
    # hoverinfo= 'y',
    opacity=0.9,
    mode = 'lines',
        line = dict(
        color = ('#D50000'),
        width = 2,
        ), 
    ))
    # data= [close,ema]
    # return dict(data=data, layout=layout)
    return fig

def SP(value,value1):
    ticker = pd.read_csv(f'tickers_data\{value}.csv',nrows=value1)
    ticker=ticker[ticker['volume']!=0]
    ticker.reset_index(drop=True, inplace=True)
    ticker.isna().sum()
    # ticker = ticker.tail(900)
    # print(ticker)
    def support(df1, l, n1, n2): #n1 n2 before and after candle l
        for i in range(l-n1+1, l+1):
            if(df1.low[i]>df1.low[i-1]):
                return 0
        for i in range(l+1,l+n2+1):
            if(df1.low[i]<df1.low[i-1]):
                return 0
        return 1
    def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
        for i in range(l-n1+1, l+1):
            if(df1.high[i]<df1.high[i-1]):
                return 0
        for i in range(l+1,l+n2+1):
            if(df1.high[i]>df1.high[i-1]):
                return 0
        return 1
    
    sr = []
    n1=3
    n2=2
    for row in range(3, len(list(ticker.index))-n2): #len(df)-n2
        if support(ticker, row, n1, n2):
            sr.append((row,ticker.low[row],1))
        if resistance(ticker, row, n1, n2):
            sr.append((row,ticker.high[row],2))
    plotlist1 = [x[1] for x in sr if x[2]==1]
    plotlist2 = [x[1] for x in sr if x[2]==2]
    plotlist1.sort()
    plotlist2.sort()
    for i in range(1,len(plotlist1)):
        if(i>=len(plotlist1)):
            break
        if abs(plotlist1[i]-plotlist1[i-1])<=0.005:
            plotlist1.pop(i)

    for i in range(1,len(plotlist2)):
        if(i>=len(plotlist2)):
            break
        if abs(plotlist2[i]-plotlist2[i-1])<=0.005:
            plotlist2.pop(i)

    dfpl = ticker

    layout = go.Layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        showlegend = True,
        hovermode  = 'x',
        spikedistance =  -1,
        title= {
            'text' : f"{value} حمایت و مقاومت سهم",
            'x':0.5,
            'xanchor': 'center'
        },
        
        titlefont= {"family":"Vazir","size":20,"color":"#000000"},
        font={"family":"Vazir","size":10,"color":"#000000"},

    xaxis=dict(        
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikethickness = 1,
        spikedash = "dash",
        #("solid", "dot", "dash", "longdash", "dashdot", or
                # "longdashdot") or a dash length list in px (eg
                # "5px,10px,2px,2px")
        spikemode  = 'across',
        ticklabelposition = 'outside bottom',
        tickformat = "%Y-%m-%d",
        spikecolor = "rgb(117, 117, 117)"

        # spikesnap = 'cursor',
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        # showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=0,
        mirror=True,
        showspikes = True,
        spikemode  = 'across',
        spikethickness = 1,
        spikedash = "dash",
        spikecolor = "rgb(117, 117, 117)",
        # type = "log",
        # tickformat = "000"
    ),
    )


    fig = go.Figure(layout=layout)
    c=0
    while (1):
        if(c>len(plotlist1)-1 ):#or sr[c][0]>e
            break
        fig.add_shape(type='line', x0=list(dfpl["date"])[0], y0=plotlist1[c],
                    x1=list(dfpl["date"])[-1],
                    y1=plotlist1[c],
                    line=dict(color="MediumPurple",width=3),
                    )
        c+=1

    c=0
    while (1):
        if(c>len(plotlist2)-1 ):#or sr[c][0]>e
            break
        fig.add_shape(type='line', x0=list(dfpl["date"])[0], y0=plotlist2[c],
                    x1=list(dfpl["date"])[-1],
                    y1=plotlist2[c],
                    line=dict(color="RoyalBlue",width=1),
                    )
        c+=1

    fig.add_trace(go.Candlestick(x=dfpl["date"],
                    open=dfpl['open'],
                    high=dfpl['high'],
                    low=dfpl['low'],
                    close=dfpl['close'],
                    name = "Price"))
    # fig.add_trace(go.Scatter(
    # x = dfpl['date'],
    # y = dfpl["close"],
    # name = "قیمت سهم",
    # # hoverinfo= 'y',
    # opacity=1,
    # mode = 'lines',
    #     line = dict(
    #     color = ('rgb(2, 12, 245)'),
    #     width = 2,
    #     ), 
    # ))
    fig.update_layout(
    xaxis2=dict(rangeslider=dict(visible=False)),
    xaxis1=dict(rangeslider=dict(visible=False))
    )

    # line_length = ticker["date"]
    # vortex_indicator_p = list(ta.trend.vortex_indicator_pos(ticker["high"], ticker["low"], ticker["close"], 24))
    # vortex_indicator_n = list(ta.trend.vortex_indicator_neg(ticker["high"], ticker["low"], ticker["close"], 24))


    # layout = go.Layout(
    #     paper_bgcolor='#ffffff',
    #     plot_bgcolor='#ffffff',
    #     showlegend = True,
    #     hovermode  = 'x',
    #     spikedistance =  -1,
    #     title= {
    #         'text' : f"{value} Vortex شاخص",
    #         'x':0.5,
    #         'xanchor': 'center'
    #     },
        
    #     titlefont= {"family":"Vazir","size":20,"color":"#000000"},
    #     font={"family":"Vazir","size":10,"color":"#000000"},

    # xaxis=dict(        
    #     showline=True,
    #     showgrid=True,
    #     showticklabels=True,
    #     linecolor='rgb(204, 204, 204)',
    #     linewidth=0,
    #     mirror=True,
    #     showspikes = True,
    #     spikethickness = 1,
    #     spikedash = "dash",
    #     #("solid", "dot", "dash", "longdash", "dashdot", or
    #             # "longdashdot") or a dash length list in px (eg
    #             # "5px,10px,2px,2px")
    #     spikemode  = 'across',
    #     ticklabelposition = 'outside bottom',
    #     tickformat = "%Y-%m-%d",
    #     spikecolor = "rgb(117, 117, 117)"

    #     # spikesnap = 'cursor',
    # ),
    # yaxis=dict(
    #     showline=True,
    #     showgrid=True,
    #     # showticklabels=True,
    #     linecolor='rgb(204, 204, 204)',
    #     linewidth=0,
    #     mirror=True,
    #     showspikes = True,
    #     spikemode  = 'across',
    #     spikethickness = 1,
    #     spikedash = "dash",
    #     spikecolor = "rgb(117, 117, 117)",
    #     # type = "log",
    #     # tickformat = "000"
    # ),
    # )
    # fig = go.Figure(layout=layout)
    
    # fig.add_trace(go.Scatter(
    # x = ticker["date"][-value1::],
    # y = vortex_indicator_p[-value1::],
    # name = "VI +",
    # # hoverinfo= 'y',
    # opacity=0.9,
    # mode = 'lines',
    #     line = dict(
    #     color = ('#01579B'),
    #     width = 2,
    #     ), 
    # ))
    # fig.add_trace(go.Scatter(
    # x = ticker["date"][-value1::],
    # y = vortex_indicator_n[-value1::],
    # name = "VI -",
    # # hoverinfo= 'y',
    # opacity=0.9,
    # mode = 'lines',
    #     line = dict(
    #     color = ('#D50000'),
    #     width = 2,
    #     ), 
    # ))
    # data= [close,ema]
    # return dict(data=data, layout=layout)
    return fig

# def time_frame(value):
#     ticker = pd.read_csv(f'tickers_data\{value}.csv')
#     date = len(list(ticker.index))
#     options=[]
#     if date >= 3650:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "سال 5", "value": 1825},
#                 {"label": "سال 3", "value": 1095},
#                 {"label": "1 سال", "value": 365},
#                 {"label": "6 ماه", "value": 180},
#                 {"label": "3 ماه", "value": 90},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 3649 >= date >= 1825:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "سال 5", "value": 1825},
#                 {"label": "سال 3", "value": 1095},
#                 {"label": "1 سال", "value": 365},
#                 {"label": "6 ماه", "value": 180},
#                 {"label": "3 ماه", "value": 90},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 1824 >= date >= 365:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "سال 3", "value": 1095},
#                 {"label": "1 سال", "value": 365},
#                 {"label": "6 ماه", "value": 180},
#                 {"label": "3 ماه", "value": 90},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 364 >= date >= 210:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "6 ماه", "value": 180},
#                 {"label": "3 ماه", "value": 90},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 209 >= date >= 120:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "3 ماه", "value": 90},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 119 >= date >= 30:
#         options=[
#                 {"label": "همه", "value": date},
#                 {"label": "1 ماه", "value": 30},
#                 {"label": "1 هفته", "value": 7},
#             ]
#     if 29 >= date >= 0:
#         options=[
#                 {"label": "همه", "value": date},
#         ]
#     t = md.Stack(
#     direction="row",
#     style={"justify-content": "space-around","width":"100%"},
#     children=[
#         dbc.RadioItems(
#             id="radios",
#             className="btn-group",
#             inputClassName="btn-check",

#             labelClassName="btn btn-outline-primary",
#             labelCheckedClassName="active",
#             options=options=[
#                 {"label": "همه", "value": date},
#                 {"label": "یک سال", "value": 365},
#                 {"label": "شش ماه", "value": 180},
#                 {"label": "سه ماه", "value": 90},
#                 {"label": "یک ماه", "value": 30},
#                 {"label": "یک هفته", "value": 30},
#             ],
#             value=date,
#             style={"margin-left":"0%","justify-content": "flex-start","font-family":"Vazir"}
#         ),
#         html.H4(":تایم فریم",style={"font-family":"Vazir","margin-left":"0%"}),
#         ]
# )
#     return t