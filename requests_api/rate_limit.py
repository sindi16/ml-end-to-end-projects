import requests
import time
def safe_get(url):
    response = requests.get(url)
    if response.status_code == 429:
        print('Rate limit hit, waiting 60s')
        time.sleep(60)
        response = requests.get(url)

    return response.json()

print(safe_get())