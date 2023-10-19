import json
x={
    "name":"deva",
    "age":23,
    "clg":["tpgit"],
    "loc":("vellore")

}
print(x)
print(x['age'])
print(x['name'])
print(x.values())
print(x.keys())
y=json.dumps(x)
print(y)
print()