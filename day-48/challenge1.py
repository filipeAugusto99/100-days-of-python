from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")


date_list = [date.text for date in dates]
names_events_list = [name.text for name in names_events]


events = {}


for i in range(len(date_list)):
    events[i] = {
        "time": date_list[i],
        "name": names_events_list[i]
    }


print(events)


driver.quit()

