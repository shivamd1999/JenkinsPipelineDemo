import json
with open('file.json','r') as persondata:
          employee=json.load(persondata)
print(employee)
