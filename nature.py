from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
h = urlopen('https://www.nature.com/')
bs = BeautifulSoup(h, 'html.parser')
print("1.Latest Journal\n2.NEWS/ARTICLES\n3.Nature Research")
x = input("Enter your choice : ")
if(int(x) == 1):
    link = bs.find('div', class_='c-hero__copy')
    print(link.h2.a.get_text())
    print(link.h2.a.attrs['href'])
elif(int(x) == 2):
    for link in bs.find("body", {"class": "home-page on-nature-150-page"}).findAll("a", href=re.compile("^(/nature/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
elif(int(x) == 3):
    print("1.Our Journlas\n2.Subjects")
    i = input("Enter ur choice:")
    if(int(i) == 2):
        a = []
        l = bs.find(
            "div", {"class": "app-header-tray__container"}).find_all("h4")
        for item in l:
            if(item.get_text() == "Subjects"):
                a_list = item.parent.find_all("a")
                for link in a_list:
                    if "href" in link.attrs:
                        a.append(link.attrs["href"])
                        print(link.attrs["href"])
        print("1.Biological Sciences\n2.Scientific Community & Society\n3.Earth & Environmental Sciences\n4.Health Sciences\n5.Physical Sciences")
        k = input("Enter ur option : ")
        if(int(k) == 1):
            html = urlopen('https://www.nature.com'+a[0])
            s = BeautifulSoup(html, 'html.parser')
            f = s.find(
                "div", {"class": "content mb30 mq1200-padded position-relative"}).find_all("a")
            for n in f:
                print(n.attrs["href"])
                print(n.get_text())
        elif(int(k) == 2):
            html = urlopen('https://www.nature.com'+a[1])
            s = BeautifulSoup(html, 'html.parser')
            f = s.find(
                "div", {"class": "content mb30 mq1200-padded position-relative"}).find_all("a")
            for n in f:
                print(n.attrs["href"])
                print(n.get_text())
        elif(int(k) == 3):
            html = urlopen('https://www.nature.com'+a[2])
            s = BeautifulSoup(html, 'html.parser')
            f = s.find(
                "div", {"class": "content mb30 mq1200-padded position-relative"}).find_all("a")
            for n in f:
                print(n.attrs["href"])
                print(n.get_text())
        elif(int(k) == 4):
            html = urlopen('https://www.nature.com'+a[3])
            s = BeautifulSoup(html, 'html.parser')
            f = s.find(
                "div", {"class": "content mb30 mq1200-padded position-relative"}).find_all("a")
            for n in f:
                print(n.attrs["href"])
                print(n.get_text())
        elif(int(k) == 5):
            html = urlopen('https://www.nature.com'+a[4])
            s = BeautifulSoup(html, 'html.parser')
            f = s.find(
                "div", {"class": "content mb30 mq1200-padded position-relative"}).find_all("a")
            for n in f:
                print(n.attrs["href"])
                print(n.get_text())
    elif(int(i) == 1):
        J = bs.find(
            "div", {"class": "app-header-tray__container"}).find_all("h4")
        for item in J:
            if(item.get_text() == "Our Journals"):
                a_list = item.parent.find_all("a")
                for link in a_list:
                    if "href" in link.attrs:
                        print(link.attrs["href"])
