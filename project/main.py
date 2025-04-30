from script import machain,data_source

def test():
    # print(data_source.get_stock_daily('900938',60))
    # print(data_source.get_stock_message('900938'))
    data = data_source.get_today_department('电子元件')
    data.to_csv("../data/test.csv")

def run():
    # department_names = ['半导体','电子元件','能源金属','电力行业','互联网服务','光学光电子','通用设备' ]
    department_names = ['电力行业']
    machain.analysis_low_point_stock(department_names)
    print("----  分析完成，请查看data文件夹！  ----")


# test()
run()