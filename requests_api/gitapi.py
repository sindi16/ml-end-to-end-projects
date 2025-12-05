import requests 

url = "https://api.github.com/users/torvalds"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['name'])
    print(data['public_repos'])

