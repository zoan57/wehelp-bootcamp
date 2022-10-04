def avg(data):
    source = data["employees"]
    employees_length = 0
    sum = 0
    for entry in source:
        if entry["manager"] == False:
            sum += entry["salary"]
            employees_length += 1
    print(sum//employees_length)
    

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
})
