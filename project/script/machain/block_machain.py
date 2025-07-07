from ..tools import data_source, utils, draw

def get_departments_quickly(folder):
    get_top_departments(folder)
    # get_top_concepts(folder)
    get_all_departments_and_concepts(folder)
    analysis_noteworthy_departments(folder, [], True)

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
    # all_concepts = data_source.get_concepts()
    # all_concepts.to_csv(folder + "概念板块全部.csv", index=False)

#全盘跑数据找低位板块
def analysis_noteworthy_departments(folder, department_names, is_draw):
    low_point_folder = folder + 'low_point_block/'
    utils.make_directory(low_point_folder)
    hot_folder = folder + 'hot_block/'
    utils.make_directory(hot_folder)
    # 空数组则自动获取获取全部板块
    if(department_names is None or not department_names):
        all_departments = data_source.get_departments()
        department_names = all_departments['板块名称'].to_list()

    noteworthy_list = []
    for department_name in department_names:
        department_daily = data_source.get_department_daily(department_name, 45)
        if(is_low_point_block(department_daily)):
            noteworthy_list.append(department_name)
            if(is_draw):
                draw.draw_stock_daily_picture(department_daily, low_point_folder + department_name + '.png')
            continue
        if(is_hot_block(department_daily)):
            noteworthy_list.append(department_name)
            if(is_draw):
                draw.draw_stock_daily_picture(department_daily, hot_folder + department_name + '.png')
    return noteworthy_list

def is_low_point_block(block_daily):
    prices = block_daily['收盘'].tolist()
    if(utils.get_point_ratio(prices) < 1 or utils.get_difference_ratio(prices) < 0.1):
        return False
    #趋于平稳,5天内下跌天数小于3天
    fluctuations = block_daily['涨跌幅'].tolist()
    last_fluctuations = fluctuations[-5:]
    return sum(n < 0 for n in last_fluctuations) < 3

def is_hot_block(block_daily):
    fluctuations = block_daily['涨跌幅'].tolist()
    last_3_fluctuations = fluctuations[-3:]
    is_continuous_rise = all(n > 0 for n in last_3_fluctuations)
    last_5_fluctuations = fluctuations[-5:]
    rise_days = sum(n> 0 for n in last_5_fluctuations)
    return is_continuous_rise and rise_days < 5