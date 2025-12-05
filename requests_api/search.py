import requests
url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId' : 1}

response = requests.get(url)
data = response.json()

for element in data:
    print(data['title'])
    