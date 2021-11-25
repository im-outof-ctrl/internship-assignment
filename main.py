import bs4
import csv
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

uClient = requests.get('https://www.supremenewyork.com/shop/all').text
shop_page = soup(uClient, 'lxml')
containers = shop_page.findAll("div", {"class" : "inner-article"})
n = len(containers)

file = open('output.csv', 'w')
writer = csv.writer(file)

writer.writerow(['Productname', 'Description', 'Price'])

for x in range(n):
    product_page = 'https://www.supremenewyork.com'+containers[x].a['href']
    source = requests.get(product_page).text
    sub_page = soup(source, 'lxml')
    Product_name = sub_page.title.text
    description = sub_page.findAll("p", {"class" : "description"})
    Product_description = description[0].text
    price = sub_page.findAll("span", {"data-currency" : "JPY"})
    Product_price = price[0].text
    # print(Product_name)
    # print(Product_price)
    # print(Product_description)
    file.write(Product_name + "," + Product_description.replace(",","|") + "," + Product_price.replace(",",".") + "\n")

file.close()