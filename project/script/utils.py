from datetime import date,timedelta

def get_today_format():
    return date.today().strftime("%Y%m%d")

def get_before_day_format(before_days):
    before_day = date.today() - timedelta(days=before_days)
    return before_day.strftime("%Y%m%d")

#获取最大差异比例
def get_difference_ratio(list):
    max_value = max(list)
    min_value = min(list)
    return round((max_value - min_value) / min_value, 2)

#尾部位置判断，返回高低差值的比例
def get_point_ratio(list):
    max_value = max(list)
    min_value = min(list)
    point_value = list[-1]
    if(min_value == point_value):
        #特殊位置，尾部即低点，规定返回100
        return 10
    return round(abs(max_value - point_value) / abs(min_value - point_value), 2)

