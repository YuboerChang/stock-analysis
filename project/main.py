from script import machain,data_source

def run():
    # data = data_source.get_departments()
    # data.to_csv("../data/板块.csv")
    # department_names = ['能源金属','电力行业']
    # machain.analysis_stocks_of_departments(department_names)


    # data = data_source.get_concepts()
    # data.to_csv("../data/概念.csv")
    concept_names = ['新能源','绿色电力']
    machain.analysis_stocks_of_concepts(concept_names)


run()
print("----  分析完成，请查看data文件夹！  ----")