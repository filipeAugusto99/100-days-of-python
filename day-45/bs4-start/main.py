from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_pag = response.text

soup = BeautifulSoup(yc_web_pag, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvote)









# with open("website.html") as file:
#     contents = file.read()
# 
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup)
# # print(soup.p)
# 
# 
# # Finding and Selecting Particular Elements with Beautiful Soup
# # all_anchor_tags = soup.find_all(name="a")
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText)
# #     print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
# 
# company_url = soup.select_one(selector="p a")
# print(company_url)
# 
# name = soup.select_one(selector="#name")
# print(name)
# 
# headings = soup.select(".heading")
# print(headings)