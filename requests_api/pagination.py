import requests
def fetch_all_people():
    results = []
    url = "https://swapi-api.hbtn.io/api/people/"

    while url:
        response = requests.get(url)
        data = response.json()

        results.extend(data['results'])
        url = data['next']

    return results
people = fetch_all_people()
print('Total:', len(people))