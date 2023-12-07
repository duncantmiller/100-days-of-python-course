from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = BeautifulSoup(response.text, "html.parser")

rows = content.find_all(name="tr", class_="athing")

print(rows)
