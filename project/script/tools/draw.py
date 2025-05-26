import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

def ak_data_format(stock_daily):
    if(len(stock_daily) > 20):
        stock_daily['ma_20'] = stock_daily['收盘'].rolling(window=20).mean()
    stock_daily = stock_daily.rename(columns={'日期': 'Date', '开盘': 'Open', '最高': 'High', '最低': 'Low', '收盘': 'Close', '成交量': 'Volume'})
    stock_daily['Date'] = pd.to_datetime(stock_daily['Date'])
    stock_daily.set_index('Date', inplace=True)
    return stock_daily

def draw_stock_chart(format_stock_daily, save_path):
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
    if(len(format_stock_daily) > 20):
        ap = mpf.make_addplot(format_stock_daily['ma_20'])
        mpf.plot(format_stock_daily, type='candle', addplot=ap, volume=True, style=chart_style, savefig=save_path)
    else:
        mpf.plot(format_stock_daily, type='candle', volume=True, style=chart_style, savefig=save_path)


#特定股票走势画图
def draw_stock_daily_picture(stock_daily, path):
    try:
        format_stock_daily = ak_data_format(stock_daily)
        draw_stock_chart(format_stock_daily,path)
    except Exception as e:
        print(path + f" 画图时发生异常: {e}")