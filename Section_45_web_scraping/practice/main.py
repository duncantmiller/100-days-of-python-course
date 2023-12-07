from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify())
print(soup.find_all(name="p"))
tags = soup.find_all(name="a")

for tag in tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector="p a")

print(company_url)
