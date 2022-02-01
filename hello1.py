import json
with open('person.json','r') as persondata:
          employee=json.load(persondata)
print(employee)
