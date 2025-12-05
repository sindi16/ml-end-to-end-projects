import requests
response = requests.get('https://swapi-api.hbtn.io/api/people/1/.')
data = response.json()

print('Name:', data['name'])
print('Height:', data['height'])
print('Films list:', data['films'])


response = requests.get('https://swapi-api.hbtn.io/api/people/20/.')
data = response.json()

#films = data.get('films', []) if i do like this i ll print directly films[0]
print(f'Name: {data['name']}' )
print(f'Skin color: {data['skin_color']}')
print(f'Film Url: {data['films'][0]}')