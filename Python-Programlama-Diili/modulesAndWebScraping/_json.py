import json

person_string= '{"name":"ali","languages" :"[python,c#]"}'

#JSON dan dictionary ye çevirme
result = json.loads(person_string)
print(result)
print(result["name"])

#JSON dosyadan veri okuma
with open("person.json") as f:
    data=json.load(f)
    print(data["name"])
    print(data["languages"])
    
#dictionary'den JSON'a çevirme
person_dict = {
    "name": "ali",
    "languages" : ["c#","python"]
}
result = json.dumps(person_dict)
print(result)