n = int(input("Please enter a positive integer: "))
if n > 1:
    print (n*"*")
    for x in range(n-1, 1, -1):
        print("*"+ (x-2)*" "+"*") 
    print("*") 
elif n == 1:
    print("*")