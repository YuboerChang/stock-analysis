from ..tools import analysis, data_source
from ..tools import draw

def analysis_stocks_of_departments(department_names, file_path):
    for department in department_names:
        department_stocks = data_source.get_department_stocks(department)
        stock_codes = department_stocks['代码'].tolist()
        analysis_low_point_stocks(stock_codes, file_path)

def analysis_stocks_of_concepts(concept_names, file_path):
    for concept in concept_names:
        concept_stocks = data_source.get_concept_stocks(concept)
        stock_codes = concept_stocks['代码'].tolist()
        analysis_low_point_stocks(stock_codes, file_path)

def analysis_low_point_stocks(stock_codes, file_path):
    for stock_code in stock_codes:
        if(not analysis.is_hu_shen_stock(stock_code)):
            continue
        stock_daily = data_source.get_stock_daily(stock_code, 90)
        if(not is_low_point_stock(stock_daily)):
            continue
        score = calculate_score(stock_daily)
        stock_name = data_source.get_stock_name(stock_code)
        draw.draw_stock_daily_picture(stock_daily, file_path + str(score) + '_' + stock_code + '_' + stock_name +'.png')

#低点位置分析
def is_low_point_stock(stock_daily):
    is_ok = True
    try:
        if(not analysis.is_large_fluctuations(stock_daily)):
            is_ok = False
        if(not analysis.is_low_point(stock_daily)):
            is_ok = False
        if(not analysis.is_lower_than_median(stock_daily) and not analysis.is_lower_than_average(stock_daily)):
            is_ok = False
        if(not analysis.is_stable_line_recently(stock_daily, 3)):
            is_ok = False
    except Exception as e:
        print(stock_daily['股票代码'].values[0] + f" 分析时发生异常: {e}")
        is_ok = False
    finally:
        return is_ok
        
def calculate_score(stock_daily):
    score = 0
    if(analysis.is_higher_than_20_average_line_recently(stock_daily)):
        score+=1
    if(analysis.is_fall_last_day(stock_daily)):
        score+=1
    if(analysis.is_many_fluctuations(stock_daily)):
        score+=1
    return score