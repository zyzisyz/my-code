import requests
import os
from bs4 import BeautifulSoup


print('the program starts')
cont = 0
page = 'index.html'
url = 'http://www.lu543.com/art/oumeisetu/' + page
root = "E://pics//"
if not os.path.exists(root):
    os.mkdir(root)
root = "E://pics//" + url.split('/')[-2] + '//'
if not os.path.exists(root):
    os.mkdir(root)


def getHTMLtext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return ''


def getBS(url):
    soup = BeautifulSoup(getHTMLtext(url), 'html.parser')
    return soup


index_soup = getBS(url)
for index_link in index_soup.find_all('a', target="_blank"):
    gallery_url = 'http://www.lu543.com' + index_link.get('href')
    gallery_soup = getBS(gallery_url)
    for gallery_link in gallery_soup.find_all('img'):
        photo_url = gallery_link.get('src')
        path = root + str(cont) + '.jpg'
        cont += 1
        if cont > 200:
            break
        if not os.path.exists(path):
            photo_re = requests.get(photo_url)
            with open(path, 'wb') as f:
                f.write(photo_re.content)
                f.close()
                print('NO.{0} is saved'.format(cont))
        else:
            print('NO.{0} already exists'.format(cont))
