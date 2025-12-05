import pandas as pd
import requests

url = "https://api.openbrewerydb.org/v1/breweries"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
print(df[['name', 'state', 'city']].head())