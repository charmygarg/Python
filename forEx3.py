n = int(input("Enter any number:"))
number = 1
power = 0
for number in range(1,n+1):
    power =power + (n ** 2)
    n = n - 1
print(power)