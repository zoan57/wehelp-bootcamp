function avg(data) {
    let source = data["employees"];
    let sourceLength = source.length
    let employeesLength = 0
    let sum = 0;
    for (let i = 0; i < sourceLength; i++) {
        if (source[i].manager == false) {
            sum += source[i].salary
            employeesLength++
        }
    }
    console.log(sum / employeesLength)

}
avg({
    "employees": [{
            "name": "John",
            "salary": 30000,
            "manager": false
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": true
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": false
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": false
        }
    ]
})