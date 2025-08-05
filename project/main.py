from script.machain import block_machain
from script.machain import stock_machain
from script.tools import data_source,analysis,draw,utils

def run_blocks():
    block_folder = '../data/block/'
    utils.make_directory(block_folder)
    block_machain.get_departments_quickly(block_folder)

def run_department_stocks():
    stock_folder = '../data/stock/'
    department_names = ['电网设备','航天航空']
    stock_machain.analysis_stocks_of_departments(department_names, stock_folder)

def run_concept_stocks():
    stock_folder = '../data/stock/'
    concept_names = ['低空经济','固态电池']
    stock_machain.analysis_stocks_of_concepts(concept_names, stock_folder)

def test():
    data_source.get_department_stocks('电力行业')


# run_blocks()
run_department_stocks()
# run_concept_stocks()
# test()

print("----                              ----")
print("----  分析完成，请查看data文件夹！  ----")
print("----                              ----")