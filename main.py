import os
from PIL import Image

with open('data.txt',encoding='utf-8') as f:
    c = f.readlines()

for i in c:
    print(i)

