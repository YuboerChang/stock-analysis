from script.machain import block_machain
from script.machain import stock_machain
from script.tools import data_source, utils

def run_blocks():
    block_machain.get_departments_quickly('../data/')

def run_department_stocks():
    department_names = ['能源金属','电力行业','电机','半导体','电子元件']
    stock_machain.analysis_stocks_of_departments(department_names, '../data/')

def run_concept_stocks():
    concept_names = ['新能源','绿色电力','人形机器人']
    stock_machain.analysis_stocks_of_concepts(concept_names, '../data/')

def test():
    all_departments = data_source.get_departments()
    department_names = all_departments['板块名称'].to_list()
    middle = len(department_names) // 2
    target_depart = department_names[(middle-5) : (middle+5)]
    print(target_depart)


run_blocks()
# run_department_stocks()
# run_concept_stocks()
# test()

print("----                              ----")
print("----  分析完成，请查看data文件夹！  ----")
print("----                              ----")