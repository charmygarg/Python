# Type your code here
def find_integer_with_most_divisors(input_list):
    d =0 
    max =0
    output_list = []
    for x in input_list:
        for i in range(1,x+1):
            if x%i == 0:
                list1.append(i)
         d = len(list1) 
         output_list.append(d)
     length = len(output_list)
     max = output_list[0]
     for y in range(1,length-1):
         if max < output_list[y]:
             max = output_list[y]
     return max