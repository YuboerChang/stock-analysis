def get_average(*nums):
    sum = 0
    count = 0
    for num in nums:
        sum+=num
        count+=1
    return round(sum / count, 2)


