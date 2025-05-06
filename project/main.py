from script import machain,data_source

def test():
    # data = data_source.get_concepts()
    # data.to_csv("../data/概念.csv")
    # data = data_source.get_ddepartments()
    # data.to_csv("../data/板块.csv")
    data = data_source.get_stock_daily('002738',90)
    data.to_csv("../data/板块.csv")

def run():
    # department_names = ['半导体','电子元件','能源金属','电力行业','互联网服务','光学光电子','通用设备' ]
    department_names = ['能源金属','电力行业']
    machain.analysis_stocks_of_departments(department_names)

    # concept_names = ['算力概念']
    # machain.analysis_stocks_of_concepts(concept_names)
    print("----  分析完成，请查看data文件夹！  ----")


# test()
run()