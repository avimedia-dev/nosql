import json

# Python <> JSON
# dict      Object
# list      Array
# tuple     Array
# srt       String
# int       Number
# float     Number
# True      true
# False     false
# None      null 

#DUMPLS
d = {
    "first_name": "Christian",
    "is_teacher": True,
    "cars": [
        {"brand": "Audi A2", "registerPlate": "AAA-111"},
        {"brand": "Audi A3", "registerPlate": "AAA-112"},
    ]
}

# convert python object into JSON
d_as_json = json.dumps(d, indent=4, sort_keys=True) # separators= ...
print(d_as_json)
print(type(d))
print(type(d_as_json))

#save json string to json file
with open("chrisu.json", "w", encoding='utf-8') as file:
    file.write(d_as_json)
#DUMP - save to file directly from python object
with open("chrisu2.json", "w") as file:
    json.dump(d, file,indent=4)
