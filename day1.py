import requests
import pandas as pd

# Weather API for Nanded - no key needed
url = "https://api.open-meteo.com/v1/forecast?latitude=19.87&longitude=75.34&current_weather=true"
response = requests.get(url)
data = response.json()

print("Current temp in Nanded:", data['current_weather']['temperature'], "°C")

# Save to CSV
df = pd.DataFrame([data['current_weather']])
df.to_csv('weather.csv', index=False)
print("Saved to weather.csv")