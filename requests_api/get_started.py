import requests
url = "https://swapi-api.hbtn.io/api/people/1"
response = requests.get(url)

print(f'Status:', {response.status_code})
print('Raw text:', response.text)