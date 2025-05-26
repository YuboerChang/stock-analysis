import statistics
from . import utils

#判断股票是否存在较大波动，涨跌幅大于30%
def is_large_fluctuations(stock_data):
    closing_price = stock_data['收盘'].tolist()
    undulant_ratio = utils.get_difference_ratio(closing_price)
    return undulant_ratio > 0.3

#判断是否更靠近低点位置，即与低点的距离，小于与高点距离的1/4
def is_low_point(stock_data):
    closing_price = stock_data['收盘'].tolist()
    position_data = utils.get_point_ratio(closing_price)
    return position_data > 4
    
#判断当前位置是否在中位数以下
def is_lower_than_median(stock_data):
    closing_price = stock_data['收盘'].tolist()
    median = statistics.median(closing_price)
    return closing_price[-1] < median
    
#判断当前位置是否在平均数以下
def is_lower_than_average(stock_data):
    closing_price = stock_data['收盘'].tolist()
    mean = statistics.mean(closing_price)
    return closing_price[-1] < mean

#判断近n天是否属于平稳曲线
def is_stable_line_recently(stock_data, days):
    last_n_days = stock_data.tail(days)
    all_stable_day = (abs(last_n_days['涨跌幅']) < 4).all()
    fall_day = (last_n_days['涨跌幅'] < 0).sum()
    rise_day = (last_n_days['涨跌幅'] > 0).sum()
    range_sum = last_n_days['涨跌幅'].sum()
    return all_stable_day and fall_day <= (days/2*3) and rise_day <= (days/2*3) and abs(range_sum) <= 6

#判断是否为普通A股账户就能购买的沪深股
def is_hu_shen_stock(stock_code):
    # 判断是否为沪市代码 (600/601/603/605开头的主板)
    if stock_code.startswith(('600', '601', '603', '605')):
        return True
    # 判断是否为深市代码 (000开头的主板，002/003/004开头的原中小板)
    if stock_code.startswith(('000', '002', '003', '004')):
        return True
    # 688开头的沪科创板，300/301开头的深创业板，代码以 8 开头的北交所，代码以 400、430、830 开头的新三板，等等
    return False

#最后一天是下跌的
def is_fall_last_day(stock_data):
    last_day = stock_data.tail(1)
    last_day_volatility = last_day['涨跌幅'].tolist()
    return last_day_volatility[0] < 0

#判断是否刚突破20日均线
def is_higher_than_20_average_line_recently(stock_data):
    stock_data['ma_20'] = stock_data['收盘'].rolling(window=20).mean()
    last_7_days = stock_data.tail(7)
    # 近2日收盘价是否在 20 日均线之上
    recent_2_days_above = (last_7_days['收盘'].iloc[-2:] > last_7_days['ma_20'].iloc[-2:]).all()
    # 再往前5日收盘价是否至少有 3 天在 20 日均线之下
    previous_5_days_below_count = (last_7_days['收盘'].iloc[:5] < last_7_days['ma_20'].iloc[:5]).sum()
    previous_5_days_below = previous_5_days_below_count >= 3
    return recent_2_days_above and previous_5_days_below

#判断近几天是否小幅连涨
def is_rise_continuously(stock_data):
    last_5_days = stock_data.tail(5)
    ranges = last_5_days['涨跌幅'].tolist()
    rise_day = sum(0 < i < 5 for i in ranges)
    return rise_day >= 4

#判断近几天是否小幅下跌
def is_rise_continuously(stock_data):
    last_5_days = stock_data.tail(5)
    ranges = last_5_days['涨跌幅'].tolist()
    rise_day = sum(-5 < i < 0 for i in ranges)
    return rise_day >= 4

#判断是否较多波动次数，每月最少两次，3个月则最少6次
def is_many_fluctuations(stock_data):
    ranges = stock_data['涨跌幅'].tolist()
    times = utils.get_fluctuation_times(ranges)
    return times >= 6
