from datetime import date,timedelta
from pathlib import Path

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

#数据波动次数计算，如果偏离值超过6，则可认为是一次波动
def get_fluctuation_times(list):
    times = 0
    fluc = 0
    for value in list:
        if(abs(fluc) > 6 and (value*fluc) > 0):
            # 峰值同向直接跳过
            continue
        if(abs(fluc) > 6 and (value*fluc) < 0):
            # 峰值反向波动归零
            fluc = 0
        fluc += value
        if(abs(fluc) > 6):
            times+=1
    return times

#文件夹创建处理
def make_directory(folder):
    folder_path = Path(folder)
    try:
        folder_path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"创建文件夹{folder}失败: {e}")