import json
#инициализация json объекта
tickets_info = {
    "ticket num": [],
    "departure data": [],
    "departure time": [],
    "destination airport": [],
    "price": [],
    "travel time": []
}
with open("data.json", "w") as outfile:
    json.dump(tickets_info, outfile)