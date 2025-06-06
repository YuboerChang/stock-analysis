from script.machain import block_machain
from script.machain import stock_machain
from script.tools import data_source,analysis

def run_blocks():
    block_machain.analysis_departments_quickly('../data/')

def run_department_stocks():
    department_names = ['能源金属','电力行业','电机','半导体','电子元件']
    stock_machain.analysis_stocks_of_departments(department_names, '../data/')

def run_concept_stocks():
    concept_names = ['新能源','绿色电力','人形机器人']
    stock_machain.analysis_stocks_of_concepts(concept_names, '../data/')

def test():
    stock = '603728'
    stock_dairy = data_source.get_stock_daily(stock,90)
    analysis.is_many_fluctuations(stock_dairy)
    print('test end!')


# run_blocks()
run_department_stocks()
# run_concept_stocks()
# test()

print("----                              ----")
print("----  分析完成，请查看data文件夹！  ----")
print("----                              ----")