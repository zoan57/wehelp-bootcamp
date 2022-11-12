function getData() {
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response) {
        return response.json();
    }).then(function(data) {
        let output = data["result"]["results"];

        function add(number) {
            // ADD IMAGE //
            let newPromotion = document.createElement('img');
            newPromotion.src = "https" + output[number]["file"].split("https")[1];
            console.log(newPromotion);
            document.getElementById('title-' + number).appendChild(newPromotion);

            // ADD TITLES //
            let titleName = output[number]["stitle"];
            let title = document.createElement('span');
            let titleText = document.createTextNode(titleName);
            title.appendChild(titleText);
            document.getElementById('title-' + number).appendChild(title);
        };
        for (let i = 0; i < 10; i++) {
            add(i)
        }



        //以下如果只要取2015年以後的資料。
        //但到底要怎樣才可以只取2015年以後，還能個別放入id裡...
        for (let titles of output) {
            if ((titles["xpostDate"].slice(0, 4)) > 2014) { //要找特定範圍的話要用.slice
                let pictureName = (titles["file"].split("jpg" + "jpg"));
                let placeName = (titles["stitle"]);
            }
        }


    })
}


function toggleMenu() {
    let menu = document.getElementById("menu");
    menu.classList.toggle("show");
    /*if (menu.style.display == "none") {
        menu.style.display = "block"
    } else {
        menu.style.display = "none";
    }
    */
}