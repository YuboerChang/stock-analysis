from ..tools import data_source

def analysis_top_departments(folder):
    all_departments = data_source.get_departments()
    rise_departments = all_departments.iloc[:10]
    rise_departments.to_csv(folder + "板块上涨前十.csv", index=False)
    fall_departments = all_departments.tail(10)
    fall_departments = fall_departments[::-1].reset_index(drop=True)
    fall_departments.to_csv(folder + "板块下跌前十.csv", index=False)

def analysis_top_concepts(folder):
    all_concepts = data_source.get_concepts()
    rise_concepts = all_concepts.iloc[:10]
    rise_concepts.to_csv(folder + "概念板块上涨前十.csv", index=False)
    fall_concepts = all_concepts.tail(10)
    fall_concepts = fall_concepts[::-1].reset_index(drop=True)
    fall_concepts.to_csv(folder + "概念板块下跌前十.csv", index=False)

def analysis_all_departments_and_concepts(folder):
    all_departments = data_source.get_departments()
    all_departments.to_csv(folder + "板块全部.csv", index=False)
    all_concepts.to_csv(folder + "概念板块全部.csv", index=False)
    all_concepts = data_source.get_concepts()

def get_target_departmens():
    departments = ['能源金属','电力行业']
    return departments

def get_target_concepts():
    concepts = ['新能源','绿色电力']
    return concepts