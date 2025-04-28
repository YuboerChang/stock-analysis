import akshare as ak
from . import date,compute,draw

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
    end_date = date.get_today()
    start_date = date.get_before_day(days)
    stock_daily = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date)
    return stock_daily

#判断股票是否存在较大波动，涨跌幅大于20%
def get_undulant_situation(stock_data):
    closing_price = stock_data['收盘'].tolist()
    undulant_ratio = compute.get_difference_ratio(closing_price)
    if(undulant_ratio > 0.3):
        return True
    else:
        return False

#判断是否更靠近低点位置，即与低点的距离，小于与高点距离的1/3
def get_low_point_situation(stock_data):
    closing_price = stock_data['收盘'].tolist()
    position_data = compute.get_point_situation(closing_price)
    if(position_data > 4):
        return True
    else:
        return False
    
#特定股票走势画图
def draw_stock_daily_picture(stock_daily, path):
    format_stock_daily = draw.ak_data_format(stock_daily)
    draw.draw_stock_chart(format_stock_daily,path)