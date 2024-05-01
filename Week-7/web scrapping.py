# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# import logging

# flipkart_url = "https://www.flipkart.com/search?q=" + "tv"

# flipkart_url

# urlclient = urlopen(flipkart_url)

# flipkart_page = urlclient.read()

# flipkart_html = bs(flipkart_page, 'html.parser')

# # print(flipkart_html)

# boxes = flipkart_html.find_all("div", {"class":"_1AtVbE col-12-12"})

# print(len(boxes))

# del boxes[0:2]

# print(len(boxes))

# # print(boxes[0].div.div.div)

# # print(boxes[0].div.div.div.a)

# # print(boxes[0].div.div.div.a['href'])

# # print("https://www.flipkart.com" + boxes[0].div.div.div.a['href'])

# # for i in boxes:
# #     print("https://www.flipkart.com" + i.div.div.div.a['href'])
# #     print('\n')

# product_link = "https://www.flipkart.com" + boxes[0].div.div.div.a['href']

# print(product_link)

# product_req = requests.get(product_link)
# # print(product_req.text)

# product_html = bs(product_req.text, 'html.parser')
# # print(product_html)

# comment_box = product_html.find_all("div", {"class":"_16PBlm"})
# # print(comment_box)

# print(len(comment_box))

# print(comment_box[0])

# # print(comment_box[0].div.div.find_all("p",{"class":"_2V5EHH"})[0].text)

# # for i in comment_box:
# #     print(i.div.div.find_all("p",{"class":'_2sc7ZR _2V5EHH'})[0].text)

# # stars = comment_box[0].div.div.div.div.text
# #print(stars)

# # for i in comment_box:
# #     stars = i.div.div.div.div.text
# #     print(stars)

# # comment_header = comment_box[0].div.div.div.p.text
# # print(comment_header)

# # for i in comment_box:
# #     comment_header = i.div.div.div.p.text
# #     print(comment_header)


# print(comment_box[0].div.div.find_all("div", {"class":""})[0].text)

# for i in comment_box:
#     print(i.div.div.find_all("div", {"class":""})[0].text)








import requests
from bs4 import BeautifulSoup
import csv

# Define URL of the YouTube channel
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send GET request and store response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all video items
    video_items = soup.find_all('a', href=lambda href: href and href.startswith('/watch?v='))

    # Extract video URLs for the first five videos
    video_urls = []
    for i, video_item in enumerate(video_items):
        if i >= 5:
            break
        video_url = f"https://www.youtube.com{video_item['href']}"
        video_urls.append(video_url)

    # Save video URLs to CSV file
    with open('video_urls.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Video URL'])
        for video_url in video_urls:
            writer.writerow([video_url])

    print(f"Successfully extracted video URLs for the first five videos and saved to video_urls.csv")

else:
    print(f"Error: Failed to retrieve the webpage. Status code: {response.status_code}")

print(video_urls)

