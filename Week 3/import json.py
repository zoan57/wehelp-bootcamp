import json
from turtle import title
import urllib.request as request
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
     data = json.load(response) 

output = data["result"]["results"]
with open("data.csv", "w" , encoding="utf-8") as file:
    for titles in output:
        if int(titles["xpostDate"][0:4]) >= 2015:
            picture = titles["file"].split("jpg")
            file.write(titles["stitle"]+",")
            file.write(titles["address"][5:8]+",")
            file.write(titles["longitude"]+",")
            file.write(titles["latitude"]+",")
            file.write(picture[0]+"jpg"+"\n")