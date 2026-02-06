import requests
import pandas as pd

url = "https://data.gov.in/api/crime-data"
response = requests.get(url)

new_data = response.json()
df_new = pd.DataFrame(new_data)

df_new.to_csv("latest_crime_data.csv", index=False)
