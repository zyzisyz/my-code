import requests
import os
from bs4 import BeautifulSoup
cont = 0

index_url = 'http://www.iazeros.com'
root = 'E://sea//'
if not os.path.exists(root):
    os.mkdir(root)
index_re = requests.get(index_url)
index_re.encoding = index_re.apparent_encoding
index_soup = BeautifulSoup(index_re.text, 'html.parser')
for index_link in index_soup.find_all('a', onclick="do_click();"):
    gallery_url = index_link.get('href')
    gallery_re = requests.get(gallery_url)
    gallery_soup = BeautifulSoup(gallery_re.text, 'html.parser')
    for gallery_link in gallery_soup.find_all('img'):
        photo_url = gallery_link.get('src')
        photo_re = requests.get(photo_url)
        path = root + str(cont) + '.jpg'
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                cont += 1
                f.write(photo_re.content)
                f.close()
                print('NO.', cont, ' is saved')

        else:
            print('NO.', cont, ' has existed already')

print('\n{0}s pictures are saved.'.format(cont))
