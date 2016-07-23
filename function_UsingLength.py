def my_sum(sample_list):
    sum = 0
    n = len(sample_list)
    for i in sample_list:
        sum = sum + i
        avg = sum / n 
    return avg