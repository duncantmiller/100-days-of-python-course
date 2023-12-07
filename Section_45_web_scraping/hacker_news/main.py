from bs4 import BeautifulSoup
import requests

response = requests.get("≈")
content = BeautifulSoup(response.text, "html.parser")


