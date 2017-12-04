import os
import requests
import bs4
from bs4 import BeautifulSoup

print('the program starts')
cont = 0

root = 'E://fun_pic//'
if not os.path.exists(root):
    os.mkdir(root)


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return ''


def getBS(url):
    try:
        html = getHTMLText(url)
        return BeautifulSoup(html, 'html.parser')
    except BaseException:
        return None


def main():
    cont = 0
    url = "http://jasonzou.net/"
    index_suop = getBS(url)
    for index_link in index_suop.find_all('a', class_='mustang-gallery'):
        gallery_url = "http://jasonzou.net/" + index_link.get('href')
        gallery_soup = getBS(gallery_url)
        for gallery_link in gallery_soup.find_all('img'):
            photo_url = "http://jasonzou.net/" + gallery_link.get('src')
            cont += 1
            path = root + str(cont) + '.jpg'
            photo_re = requests.get(photo_url)
            if not os.path.exists(path):
                with open(path, 'wb') as f:
                    f.write(photo_re.content)
                    f.close()
                    print('NO.{0} pic is saved'.format(cont))
            else:
                print('NO.{0} pic is existed'.format(cont))


main()
