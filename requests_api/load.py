import json
data = {'name': 'Alice', 'age' : 25}
with open('file.json', 'w') as file:
    json.dump(data, file)