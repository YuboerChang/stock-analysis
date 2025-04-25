from datetime import date,timedelta

def get_today():
    return date.today().strftime("%Y%m%d")

def get_before_day(before_days):
    before_day = date.today() - timedelta(days=before_days)
    return before_day.strftime("%Y%m%d")