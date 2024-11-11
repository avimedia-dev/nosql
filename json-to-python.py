import json

json_string = '{"hasChildren":false,"employees":null}'

d = json.loads(json_string)

print(d)
print(type(d))

#LOAD

with open('chrisu.json', 'r') as file:
    chrisu_as_python = json.load(file)

print(type(chrisu_as_python))
print(chrisu_as_python)