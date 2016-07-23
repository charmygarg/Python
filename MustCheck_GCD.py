def sample_gcd_list_ed2_(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        result = my_gcd(result, my_list[i])
    return result
  
def my_gcd(a,b):
    while b:
        a, b = b, a%b
    return a
