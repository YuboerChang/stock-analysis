from script.tools import data_source
from script.machain import stock_machain
import time

def analysis_auto():
    all_departments = data_source.get_departments()
    department_names = all_departments['板块名称'].to_list()
    popular_depart = department_names[:3]
    low_position_depart = department_names[-3:]
    stock_machain.analysis_stocks_of_departments(popular_depart,'../data/popular/')
    print("---  进入10秒休眠，防止请求过多！  ---")
    time.sleep(10)
    print("---  休眠结束，程序继续运行！  ---")
    stock_machain.analysis_stocks_of_departments(low_position_depart,'../data/low_position/')

analysis_auto()