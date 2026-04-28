from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.br/MSI-GeForce-RTX-3050-Ventus/dp/B0CSPNYB42/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24FXOTCIF3611&dib=eyJ2IjoiMSJ9.221D2eE2H2uj50b6bt_VsNlPoyE8b7Xh5IJLzWVNbkuCXTvFzUnej2Bf7Xxim8Zd7xcGh-HTTStU1a1VkFe207GxeK6Bt_heuXxlkJBB6iu8LTbPNK7Gjs6Oyeq4mlp2UO5pJDE5k7tmmoAhfFBf52BfuMXKOgcnS8VjBLOKy8poQ7wnL25pFHBM2EoaURjXndYGZdjxQSCgrjzb-5g1EG9nrrDEFPhrmsl0gZy6pC-M3Cp1xr2luAO9tAwG1a5Gn6H2B4Yb0TAx9JRXXMWS1rqbonRLSWbAmHOSWp-Yu30.IR64MJw_1PUtK5fWEYZKvUvwScV2xcBDBEbYiW1T9xI&dib_tag=se&keywords=placa%2Bde%2Bv%C3%ADdeo%2Bgtx%2B3050&qid=1777378532&sprefix=placa%2Bde%2Bvideo%2Bgtx%2B3050%2Caps%2C220&sr=8-6&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# print(f"The price is {price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar.get_attribute("placeholder"))
#driver.close()
driver.quit()