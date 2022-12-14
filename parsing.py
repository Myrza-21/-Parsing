from bs4 import BeautifulSoup # for parcing web sites
import requests
from requests import get
import time # to delay the site
import random # random number generation

url = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&page='
houses = []
count= 1
while count <=7:
    url = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&page=' + str(count)
    print (url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    house_data = html_soup.find_all('div',class_="listing")
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scaled_value = 1 + (value * (9-5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count +=1

print(len(houses))
print(houses[1])
print()
n = int(len(houses)) - 1
count = 0
while count <= 20: #count <= n
    info = houses[int(count)]
    fee = info.find('div',{"class":"price"}).text
    title_ = info.find('p',{"class":"title"}).text
    location = info.find('div',{"class":"address"}).text
    print(title_, ' ',fee,' ',location)
    count +=1




