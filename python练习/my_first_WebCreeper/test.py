import requests
from bs4 import BeautifulSoup
import os
cont = 0
url = 'http://jasonzou.net/'
root = "://pics//"
if not os.path.exists(root):
    os.mkdir(root)
# 创建目录

index_re = requests.get(url)
index_soup = BeautifulSoup(index_re.text, 'html.parser')

for link in index_soup.find_all('a', class_='mustang-gallery'):
    # 找到class=mustang-gallery的a标签
    gallery_url = 'http://jasonzou.net/' + link.get('href')
    print(gallery_url)
    gallery_re = requests.get(gallery_url)
    gallery_soup = BeautifulSoup(gallery_re.text, 'html.parser')
    for pic in gallery_soup.find_all('img'):
        # 找到所有img标签
        pic_url = 'http://jasonzou.net/' + pic.get('src')
        path = root + pic_url.split('/')[-1]
        if not os.path.exists(path):
            photo = requests.get(pic_url)
            with open(path, 'wb') as f:
                f.write(photo.content)
                f.cloCse()
                print(pic_url.split('/')[-1], ' is saved')
                cont += 1
        else:
            print(pic_url.split('/')[-1], ' has existed already')

print('\n', cont, 'pictures is saved')
