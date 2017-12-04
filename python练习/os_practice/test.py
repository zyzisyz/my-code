import os

url = 'http://www.lu543.com/art/fengrufeitun/'
root = "E://pics//"
if not os.path.exists(root):
    os.mkdir(root)
root = "E://pics//"+url.split('/')[-2]+'//'
if not os.path.exists(root):
    os.mkdir(root)