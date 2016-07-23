# Type your code here
def pattern_sum(a, b):
    sum = 0
    for i in range(1,b+1) :
        sum = sum + a
        a  = (a*(10^i))+a
    return a