import akshare as ak
from . import utils

#获取行业板块盘面信息
def get_departments():
    return ak.stock_board_industry_name_em()

#获取行业板块的股票信息
def get_department_stocks(department_name):
    all_department_data = ak.stock_board_industry_name_em()
    department_code = all_department_data[all_department_data['板块名称'] == department_name]['板块代码'].values[0]
    department_stocks = ak.stock_board_industry_cons_em(symbol=department_code)
    return department_stocks

#获取概念板块盘面信息
def get_concepts():
    return ak.stock_board_concept_name_em()

#获取概念板块的股票信息
def get_concept_stocks(concept_name):
    return ak.stock_board_concept_cons_em(symbol=concept_name)

#获取个股信息，代码或名字均可
def get_stock_message(stock):
    stocks = ak.stock_zh_a_spot_em()
    stock_msg = stocks[(stocks['代码'] == stock) | (stocks['名称'] == stock)]
    return stock_msg

#已知股票代码，获取股票名称
def get_stock_name(stock_code):
    stock_name = ''
    try:
        stocks = ak.stock_zh_a_spot_em()
        stock_msg = stocks[stocks['代码'] == stock_code]
        stock_name = stock_msg['名称'].values[0]
    except Exception as e:
        print(stock_code + f" 获取股票名称发生异常: {e}")
    return stock_name

#获取个股历史数据
def get_stock_daily(stock_code, days):
    end_date = utils.get_today_format()
    start_date = utils.get_before_day_format(days)
    stock_daily = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date)
    return stock_daily

#获取行业板块历史数据
def get_department_daily(department_name, days):
    end_date = utils.get_today_format()
    start_date = utils.get_before_day_format(days)
    stock_daily = ak.stock_board_industry_hist_em(symbol=department_name, period="日k", start_date=start_date, end_date=end_date)
    return stock_daily