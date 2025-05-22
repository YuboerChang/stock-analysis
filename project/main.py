from script.machain import stock_machain,department_machain

def run():
    # department_machain.analysis_departments_quickly('../data/')

    department_names = ['能源金属','电力行业','电机','半导体','电子元件']
    stock_machain.analysis_stocks_of_departments(department_names, '../data/')

    # concept_names = ['新能源','绿色电力','人形机器人']
    # stock_machain.analysis_stocks_of_concepts(concept_names, '../data/')


run()
print("----                              ----")
print("----  分析完成，请查看data文件夹！  ----")
print("----                              ----")