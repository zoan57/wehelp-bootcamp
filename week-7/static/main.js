function serachUser() {
    let username = document.getElementById("searchName").value;
    console.log(username);
    fetch("http://127.0.0.1:3000/api/member?username=" + username).then(function(response) {
        return response.json();
    }).then(function(value) {
        document.getElementById("resultName").innerHTML = value.data.name + "(" + value.data.username + ")";
    }).catch(function(error) {
        document.getElementById("resultName").innerHTML = "User not found!"
    })
}

function updateUser() {
    let name = document.getElementById("updateName").value;
    console.log(name);
    fetch("http://127.0.0.1:3000/api/member", {
            method: "PATCH",
            headers: {
                "Content-type": "application/json",
                "accept": "application/json"
            },
            body: JSON.stringify({
                name: name
            })
        })
        .then(function(response) {
            return response.json();
        }).then(function(value) {
            document.getElementById("updateResult").innerHTML = "更新成功";
        }).catch(function(error) {
            document.getElementById("updateResult").innerHTML = "更新失敗"
        })
}