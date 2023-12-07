from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = BeautifulSoup(response.text, "html.parser")

rows = content.find_all(name="tr", class_="athing")

front_page_links = []
for row in rows:
    title_id = row.get("id")
    title_link = row.select_one("td.title span a")
    points_span = content.select_one(f"span#score_{title_id}")
    if points_span:
        points_value = int(points_span.string.split(" ")[0])
    else:
        points_value = 0
    row_data = {
        "url": title_link.get("href"),
        "title": title_link.string,
        "points": points_value
    }
    front_page_links.append(row_data)

print(front_page_links)
