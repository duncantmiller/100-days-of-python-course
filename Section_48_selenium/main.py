from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# driver.find_element(By.LINK_TEXT, "View history").click()

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python")
driver.find_element(By.CLASS_NAME, "cdx-search-input__end-button").click()
