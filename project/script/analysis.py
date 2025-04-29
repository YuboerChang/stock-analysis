import statistics
from . import utils

#判断股票是否存在较大波动，涨跌幅大于30%
def is_large_fluctuations(stock_data):
    closing_price = stock_data['收盘'].tolist()
    undulant_ratio = utils.get_difference_ratio(closing_price)
    return undulant_ratio > 0.3

#判断是否更靠近低点位置，即与低点的距离，小于与高点距离的1/3
def is_low_point(stock_data):
    closing_price = stock_data['收盘'].tolist()
    position_data = utils.get_point_ratio(closing_price)
    return position_data > 3
    
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
    
#判断是否刚突破20日均线
def is_higher_than_20_average_line_recently(stock_data):
    stock_data['ma_20'] = stock_data['收盘'].rolling(window=20).mean()
    last_7_days = stock_data.tail(7)
    # 近三日收盘价是否在 20 日均线之上
    recent_2_days_above = (last_7_days['收盘'].iloc[-2:] > last_7_days['ma_20'].iloc[-2:]).all()
    # 再往前 5 日收盘价是否至少有 2 天在 20 日均线之下
    previous_5_days_below_count = (last_7_days['收盘'].iloc[:5] < last_7_days['ma_20'].iloc[:5]).sum()
    previous_5_days_below = previous_5_days_below_count >= 2
    return recent_2_days_above and previous_5_days_below

#判断近7天是否属于平稳曲线
def is_stable_line_recently(stock_data):
    last_10_days = stock_data.tail(10)
    all_stable_day = (abs(last_10_days['涨跌幅']) < 3).all()
    fall_day = (last_10_days['涨跌幅'] < 0).sum()
    rise_day = (last_10_days['涨跌幅'] > 0).sum()
    range_sum = last_10_days['涨跌幅'].sum()
    return all_stable_day and fall_day <= 7 and rise_day <= 7 and abs(range_sum) <= 5