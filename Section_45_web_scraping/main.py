from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify())
print(soup.find_all(name="p"))