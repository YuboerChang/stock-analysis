from . import analysis, data_source, draw

def analysis_bug_stock(department_names):
    for department in department_names:
        department_stocks = data_source.get_today_department(department)
        stock_codes = department_stocks['代码'].tolist()
        for stock_code in stock_codes:
            stock_daily = data_source.get_stock_daily(stock_code, 90)
            if(not analysis.is_large_fluctuations(stock_daily)):
                continue
            if(not analysis.is_low_point(stock_daily)):
                continue
            if(not analysis.is_lower_than_median(stock_daily) and not analysis.is_lower_than_average(stock_daily)):
                #长期来看，股价较高，才有投资意义
                continue
            # if(not analysis.is_higher_than_20_average_line_recently(stock_daily)):
            #     continue
            if(not analysis.is_stable_line_recently(stock_daily)):
                continue
            stock_msg = department_stocks[department_stocks['代码'] == stock_code]
            draw.draw_stock_daily_picture(stock_daily,'../data/'+ stock_code + '_' + stock_msg['名称'].values[0] +'.png')