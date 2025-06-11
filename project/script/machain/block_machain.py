from ..tools import data_source, utils, draw

def get_departments_quickly(folder):
    get_top_departments(folder)
    get_top_concepts(folder)
    get_all_departments_and_concepts(folder)
    low_point_folder = folder + 'low_point_block/'
    utils.make_directory(low_point_folder)
    analysis_low_point_departments(low_point_folder)

def get_top_departments(folder):
    all_departments = data_source.get_departments()
    rise_departments = all_departments.iloc[:10]
    rise_departments.to_csv(folder + "行业板块上涨前十.csv", index=False)
    fall_departments = all_departments.tail(10)
    fall_departments = fall_departments[::-1].reset_index(drop=True)
    fall_departments.to_csv(folder + "行业板块下跌前十.csv", index=False)

def get_top_concepts(folder):
    all_concepts = data_source.get_concepts()
    rise_concepts = all_concepts.iloc[:10]
    rise_concepts.to_csv(folder + "概念板块上涨前十.csv", index=False)
    fall_concepts = all_concepts.tail(10)
    fall_concepts = fall_concepts[::-1].reset_index(drop=True)
    fall_concepts.to_csv(folder + "概念板块下跌前十.csv", index=False)

def get_all_departments_and_concepts(folder):
    all_departments = data_source.get_departments()
    all_departments.to_csv(folder + "行业板块全部.csv", index=False)
    all_concepts = data_source.get_concepts()
    all_concepts.to_csv(folder + "概念板块全部.csv", index=False)

#全盘跑数据找低位板块
def analysis_low_point_departments(folder):
    all_departments = data_source.get_departments()
    department_names = all_departments['板块名称'].to_list()
    get_low_point_departments(department_names, folder, True)

#获取低位板块
def get_low_point_departments(department_names, folder, is_draw):
    low_point_list = []
    for department_name in department_names:
        department_daily = data_source.get_department_daily(department_name, 45)
        if(not is_low_point_block(department_daily)):
            continue
        low_point_list.append(department_name)
        if(is_draw):
            draw.draw_stock_daily_picture(department_daily, folder + department_name + '.png')
    return low_point_list

def is_low_point_block(block_daily):
    prices = block_daily['收盘'].tolist()
    if(utils.get_point_ratio(prices) < 1 or utils.get_difference_ratio(prices) < 0.1):
        return False
    #趋于平稳,5天内下跌天数小于4天，总涨跌幅不超过6%
    fluctuations = block_daily['涨跌幅'].tolist()
    last_fluctuations = fluctuations[-5:]
    return (sum(n < 0 for n in last_fluctuations) < 4) and (sum(last_fluctuations) < 6)