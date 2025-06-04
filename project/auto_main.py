from script.tools import utils,data_source
from script.machain import stock_machain

def analysis_auto():
    all_departments = data_source.get_departments()
    department_names = all_departments['板块名称'].to_list()
    popular_depart = department_names[:5]
    low_position_depart = department_names[-5:]
    stock_machain.analysis_stocks_of_departments(popular_depart,'../data/popular/')
    stock_machain.analysis_stocks_of_departments(low_position_depart,'../data/low_position/')

analysis_auto()