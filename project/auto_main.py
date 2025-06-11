from script.tools import data_source
from script.machain import stock_machain, block_machain

def analysis_auto():
    all_departments = data_source.get_departments()
    department_names = all_departments['板块名称'].to_list()
    popular_depart = department_names[:2]
    fall_most_depart = department_names[-2:]
    # 非最终存放的文件夹，不用创建判断
    stock_machain.analysis_stocks_of_departments(popular_depart, '../data/popular/')
    stock_machain.analysis_stocks_of_departments(fall_most_depart, '../data/fall_most/')
    #取中间十行，有较大概率处于平稳低位
    middle = len(department_names) // 2
    target_depart = department_names[(middle-5) : (middle+5)]
    low_position_depart = block_machain.get_low_point_departments(target_depart,'',False)
    stock_machain.analysis_stocks_of_departments(low_position_depart,'../data/low_position/')

analysis_auto()