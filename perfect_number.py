sum = 0
def perfect_number(x):
    for y in range(1,x):
        z = x % y
        sum = sum + z
        if z == 0 && sum == x:
            return True
        else:
            return False