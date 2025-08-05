from ..tools import data_source, utils, draw

def get_departments_quickly(folder):
    get_all_departments_and_concepts(folder)
    analysis_noteworthy_departments(folder, [], True)
    analysis_noteworthy_concepts(folder, [], True)

def get_all_departments_and_concepts(folder):
    all_departments = data_source.get_departments()
    all_departments.to_csv(folder + "行业板块全部.csv", index=False)
    all_concepts = data_source.get_concepts()
    all_concepts.to_csv(folder + "概念板块全部.csv", index=False)

#找低位行业板块
def analysis_noteworthy_departments(folder, department_names, is_draw):
    depart_folder = folder + 'department/'
    make_folder(depart_folder)
    # 空数组则自动获取获取全部板块
    if(department_names is None or not department_names):
        all_departments = data_source.get_departments()
        department_names = all_departments['板块名称'].to_list()
    noteworthy_list = []
    for department_name in department_names:
        department_daily = data_source.get_department_daily(department_name, 45)
        noteworthy_list = block_data_analysis(depart_folder, department_name, department_daily, is_draw, noteworthy_list)
    return noteworthy_list

#找低位概念板块
def analysis_noteworthy_concepts(folder, concept_names, is_draw):
    depart_folder = folder + 'concept/'
    make_folder(depart_folder)
    # 空数组则自动获取获取全部板块
    if(concept_names is None or not concept_names):
        all_concepts = data_source.get_concepts()
        concept_names = all_concepts['板块名称'].to_list()
    noteworthy_list = []
    cnt = 1
    for concept_name in concept_names:
        concept_daily = data_source.get_concept_daily(concept_name, 45)
        noteworthy_list = block_data_analysis(depart_folder, concept_name, concept_daily, is_draw, noteworthy_list)
        # 概念板块数量太多，限制一下数量
        if(cnt >= 30):
            break
        cnt+=1
    return noteworthy_list

#文件目录处理
def make_folder(folder):
    low_point_folder = folder + 'low_point_block/'
    utils.make_directory(low_point_folder)
    hot_folder = folder + 'hot_block/'
    utils.make_directory(hot_folder)

# 板块、概念数据分析
def block_data_analysis(folder, name, daily, is_draw, noteworthy_list):
    if(is_low_point_block(daily)):
        noteworthy_list.append(name)
        if(is_draw):
            draw.draw_stock_daily_picture(daily, folder + 'low_point_block/' + name + '.png')
    if(is_hot_block(daily)):
        noteworthy_list.append(name)
        if(is_draw):
            draw.draw_stock_daily_picture(daily, folder + 'hot_block/' + name + '.png')
    return noteworthy_list

def is_low_point_block(block_daily):
    prices = block_daily['收盘'].tolist()
    if(utils.get_point_ratio(prices) < 1 or utils.get_difference_ratio(prices) < 0.1):
        return False
    #趋于平稳,5天内下跌天数小于3天
    fluctuations = block_daily['涨跌幅'].tolist()
    last_fluctuations = fluctuations[-5:]
    return sum(n < 0 for n in last_fluctuations) < 3

#刚刚开涨，尾部2天上涨，但5天内上涨天数小于4天
def is_hot_block(block_daily):
    fluctuations = block_daily['涨跌幅'].tolist()
    last_3_fluctuations = fluctuations[-2:]
    is_continuous_rise = all(n > 0 for n in last_3_fluctuations)
    last_5_fluctuations = fluctuations[-5:]
    rise_days = sum(n> 0 for n in last_5_fluctuations)
    return is_continuous_rise and rise_days < 4