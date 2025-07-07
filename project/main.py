from script.machain import block_machain
from script.machain import stock_machain
from script.tools import data_source, analysis,draw

def run_blocks():
    block_machain.get_departments_quickly('../data/')

def run_department_stocks():
    department_names = ['电网设备','电力行业']
    stock_machain.analysis_stocks_of_departments(department_names, '../data/')

def run_concept_stocks():
    concept_names = ['新能源','绿色电力','人形机器人']
    stock_machain.analysis_stocks_of_concepts(concept_names, '../data/')

def test():
        department_stocks = data_source.get_department_stocks('电力行业')
        stock_codes = department_stocks['代码'].tolist()
        for stock_code in stock_codes:
            stock_daily = data_source.get_stock_daily(stock_code, 90)
            analysis.is_ten_last(stock_daily,stock_code)
            draw.draw_stock_daily_picture(stock_daily, '../data/' + stock_code +'.png')


run_blocks()
# run_department_stocks()
# run_concept_stocks()
# test()

print("----                              ----")
print("----  分析完成，请查看data文件夹！  ----")
print("----                              ----")