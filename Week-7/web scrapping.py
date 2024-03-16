import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging

flipkart_url = "https://www.flipkart.com/search?q=" + "tv"

flipkart_url

urlclient = urlopen(flipkart_url)

flipkart_page = urlclient.read()

flipkart_html = bs(flipkart_page, 'html.parser')

# print(flipkart_html)

boxes = flipkart_html.find_all("div", {"class":"_1AtVbE col-12-12"})

print(len(boxes))

del boxes[0:2]

print(len(boxes))

# print(boxes[0].div.div.div)

# print(boxes[0].div.div.div.a)

# print(boxes[0].div.div.div.a['href'])

# print("https://www.flipkart.com" + boxes[0].div.div.div.a['href'])

# for i in boxes:
#     print("https://www.flipkart.com" + i.div.div.div.a['href'])
#     print('\n')

product_link = "https://www.flipkart.com" + boxes[0].div.div.div.a['href']

print(product_link)

product_req = requests.get(product_link)
# print(product_req.text)

product_html = bs(product_req.text, 'html.parser')
# print(product_html)

comment_box = product_html.find_all("div", {"class":"_16PBlm"})
# print(comment_box)

print(len(comment_box))

print(comment_box[0])

# print(comment_box[0].div.div.find_all("p",{"class":"_2V5EHH"})[0].text)

# for i in comment_box:
#     print(i.div.div.find_all("p",{"class":'_2sc7ZR _2V5EHH'})[0].text)

# stars = comment_box[0].div.div.div.div.text
#print(stars)

# for i in comment_box:
#     stars = i.div.div.div.div.text
#     print(stars)

# comment_header = comment_box[0].div.div.div.p.text
# print(comment_header)

# for i in comment_box:
#     comment_header = i.div.div.div.p.text
#     print(comment_header)


print(comment_box[0].div.div.find_all("div", {"class":""})[0].text)

for i in comment_box:
    print(i.div.div.find_all("div", {"class":""})[0].text)



