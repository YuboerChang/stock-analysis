from script.machain import stock_machain,department_machain

def run():
    department_names = department_machain.get_target_departmens()
    stock_machain.analysis_stocks_of_departments(department_names)

    # concept_names = department_machain.get_target_concepts()
    # stock_machain.analysis_stocks_of_concepts(concept_names)



run()
print("----  分析完成，请查看data文件夹！  ----")