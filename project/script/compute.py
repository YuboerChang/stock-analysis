def get_average(*nums):
    sum = 0
    count = 0
    for num in nums:
        sum+=num
        count+=1
    return round(sum / count, 2)

def get_difference_ratio(list):
    max_value = max(list)
    min_value = min(list)
    return round((max_value - min_value) / min_value, 2)

#尾部位置判断，返回高低差值的比例
def get_point_situation(list):
    max_value = max(list)
    min_value = min(list)
    point_value = list[-1]
    if(min_value == point_value):
        #特殊位置，尾部即低点，规定返回100
        return 10
    return round(abs(max_value - point_value) / abs(min_value - point_value), 2)

