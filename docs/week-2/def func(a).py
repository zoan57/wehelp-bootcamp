def func(a):
    def add(c,d):
        result = c*d
        result += a
        print (result)
    return add


func(-3)(2,9)