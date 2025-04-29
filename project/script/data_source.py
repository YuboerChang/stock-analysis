import akshare as ak
from . import utils

#获取近日盘面板块信息
def get_today_all():
    return ak.stock_board_industry_name_em()

#获取当日板块股票信息
def get_today_department(department_name):
    all_department_data = ak.stock_board_industry_name_em()
    department_code = all_department_data[all_department_data['板块名称'] == department_name]['板块代码'].values[0]
    department_stocks = ak.stock_board_industry_cons_em(symbol=department_code)
    return department_stocks

#获取个股信息，代码或名字均可
def get_stock_message(stock):
    stocks = ak.stock_zh_a_spot_em()
    stock_msg = stocks[(stocks['代码'] == stock) | (stocks['名称'] == stock)]
    return stock_msg

#已知股票代码，获取股票名称
def get_stock_name(stock_code):
    stocks = ak.stock_zh_a_spot_em()
    stock_msg = stocks[stocks['代码'] == stock_code]
    return stock_msg['名称'].values[0]

#获取近日个股走势信息
def get_stock_daily(stock_code,days):
    end_date = utils.get_today_format()
    start_date = utils.get_before_day_format(days)
    stock_daily = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date)
    return stock_daily