import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

def ak_data_format(stock_daily):
    stock_daily = stock_daily.rename(columns={'日期': 'Date', '开盘': 'Open', '最高': 'High', '最低': 'Low', '收盘': 'Close', '成交量': 'Volume'})
    stock_daily['Date'] = pd.to_datetime(stock_daily['Date'])
    stock_daily.set_index('Date', inplace=True)
    return stock_daily

def draw_stock_chart(format_stock_daily,save_path):
    color = mpf.make_marketcolors(
        up='red', down='green',  # K 线颜色，上涨为绿色，下跌为红色
        edge={'up': 'red', 'down': 'green'},  # K 线边框颜色
        wick={'up': 'red', 'down': 'green'},  # 上下影线颜色
        volume='in',  # 成交量颜色跟随 K 线颜色
        ohlc='i'
    )
    chart_style = mpf.make_mpf_style(marketcolors=color)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    mpf.plot(format_stock_daily, type='candle', volume=True, style=chart_style, savefig=save_path)