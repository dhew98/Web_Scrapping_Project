from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
title = input("URL: ")
h = urlopen(title)
bs = BeautifulSoup(h, 'html.parser')
print("1.All links\n2.Articles\n3.Information")
x = input("Enter your choice : ")
if(int(x) == 1):
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])
elif(int(x) == 2):
    for link in bs.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
elif(int(x) == 3):
    p = bs.table.children
    for child in p:
        print(child.get_text())
