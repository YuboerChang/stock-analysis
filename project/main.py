from script import machain

def analysis_bug_stock():
    # department_names = ['半导体','电子元件','能源金属','电力行业','互联网服务','光学光电子','通用设备' ]
    department_names = ['半导体']
    for department in department_names:
        department_stocks = machain.get_today_department(department)
        stock_codes = department_stocks['代码'].tolist()
        for stock_code in stock_codes:
            stock_daily = machain.get_stock_daily(stock_code,30)
            if(machain.get_undulant_situation(stock_daily) and machain.get_low_point_situation(stock_daily)):
                stock_msg = department_stocks[department_stocks['代码'] == stock_code]
                machain.draw_stock_daily_picture(stock_daily,'../data/'+ stock_code + '_' + stock_msg['名称'].values[0] +'.png')

analysis_bug_stock()
print("----  分析完成，请查看data文件夹！  ----")