import requests

url = "https://api.nasa.gov/planetary/apod"
params = {'api_key' : 'DEMO_KEY'}


response = requests.get(url, params=params)
data = response.json()

print('Title:', data['title'])
print('Date:', data['date'])
print('URL:', data['url'])

