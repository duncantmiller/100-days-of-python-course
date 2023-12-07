from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.com/Barleans-Supplement-Softgels-Health-Flavored/dp/B002VLZ8AI")

price_element = driver.find_element(By.XPATH, value='//*[@id="sns-base-price"]/div/span[1]/span[2]')
print(price_element.text)
