import mplfinance as mpf
import pandas as pd

def ak_data_format(stock_daily):
    stock_daily = stock_daily.rename(columns={'日期': 'Date', '开盘': 'Open', '最高': 'High', '最低': 'Low', '收盘': 'Close', '成交量': 'Volume'})
    stock_daily['Date'] = pd.to_datetime(stock_daily['Date'])
    stock_daily.set_index('Date', inplace=True)
    return stock_daily

def draw_stock_chart(stock_daily,save_path):
    mpf.plot(stock_daily, type='candle', volume=True, title='K-line', ylabel='Price', ylabel_lower='Volume',savefig=save_path)
