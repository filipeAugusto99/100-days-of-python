from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)


# Create and Configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


# Navigate to form
driver.get("https://secure-retreat-92358.herokuapp.com/")


# Input forms automatic
form_name = driver.find_element(By.NAME, value="fName")
form_name.send_keys("Filipe")
form_lastname = driver.find_element(By.NAME, value="lName")
form_lastname.send_keys("Augusto")
form_email= driver.find_element(By.NAME, value="email")
form_email.send_keys("filipe123@gmail.com")


# Send form
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()



