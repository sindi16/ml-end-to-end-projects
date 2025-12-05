import requests

url = 'https://swapi-api.hbtn.io/api/people/'
params = {'search' : 'Luke'}

response = requests.get(url, params=params)
data = response.json()


count = data.get('count')

print('Count:', count)
# or print(data['count'])
print('First:', data['results'][0]['name'])


url = 'https://swapi-api.hbtn.io/api/people/'
params = {'search' : 'R2'}

response = requests.get(url)
data = response.json()

print('Count:', data['count'])

results = data.get('results', [])
for person in results:
    print(person['name'])