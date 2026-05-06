from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


qtd_articles = driver.find_elements(By.CSS_SELECTOR, value="#articlecount li a")

article_list = [article.text for article in qtd_articles]
print(article_list)