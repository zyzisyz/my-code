import requests
import os
from bs4 import BeautifulSoup
url="http://jasonzou.net/"
root="E://creeper_pictures//"
if not os.path.exists(root):
    os.mkdir(root)

index_re=requests.get(url)
index_re.encoding=index_re.apparent_encoding
index_soup=BeautifulSoup(index_re.text,'html.parser')
for gallery_link in index_soup.find_all('a',class_='mustang-gallery'):
    gallery_url="http://jasonzou.net/"+gallery_link.get('href')
    gallery_re=requests.get(gallery_url)
    gallery_soup=BeautifulSoup(gallery_re.text,'html.parser')
    for pic_link in gallery_soup.find_all('img'):
        photo_url='http://jasonzou.net/'+pic_link.get('src')
        photo_re=requests.get(photo_url)
        path=root+photo_url.split('/')[-1]
        if not os.path.exists(path):
            with open(path,'wb') as f:
                f.write(photo_re.content)
                f.close()
                print(photo_url.split('/')[-1],' is saved')
        else:
            print('the photo has saved already')
