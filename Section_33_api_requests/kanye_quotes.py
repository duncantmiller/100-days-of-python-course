import requests

response = requests.get(url="https://api.kanye.rest")

response.raise_for_status()

quote = response.json()["quote"]
print(quote)
