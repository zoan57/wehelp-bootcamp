def calculate(min, max, step):
    sum = 0
    for i in range(min, max+1, step):
        sum += i
    print(sum)
        
calculate(4, 8, 2)