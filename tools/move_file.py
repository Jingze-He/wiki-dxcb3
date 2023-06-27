import os
from PIL import Image


def move_tubiao_and_lihui(path, newpath, refpath)

    path = 'C://Users//何竞择//Desktop//wiki//再生者图片//原始图标'
    newpath = 'C://Users//何竞择//Desktop//wiki//命名图标'

    files = os.listdir(path)

    content = {"_1": "普通", "_2": "传说", "_3": "觉醒", "_4": 0, "_5": 1, "_6": 2}

    # 再生者皮肤列表
    with open(refpath,encoding='utf-8') as f:
        c = f.readlines()
    for i in c:
            d = i.replace("\n","").split("\t")
            print(d)
            for j in files:
                if d[2] + "_" in j:
                    for key in content:
                        if key in j and '4' not in key and '5' not in key and '6' not in key:
                            img_size = Image.open(os.path.join(path, j)).convert('RGB').size
                            if img_size[0] < 150 and img_size[1] < 150:
                                os.rename(os.path.join(path, j), os.path.join(path, "图标-" + d[0] + "-" + content[key] + ".png"))
                            else:
                                os.rename(os.path.join(path, j), os.path.join(path, "再生者-立绘-" + d[0] + "-" + content[key] + ".png"))
                        elif key in j:
                            img_size = Image.open(os.path.join(path, j)).convert('RGB').size
                            if img_size[0] < 150 and img_size[1] < 150:
                                os.rename(os.path.join(path, j), os.path.join(path, "图标-" + d[0] + "-" + d[1].split("、")[content[key]] + ".png"))
                            else:
                                os.rename(os.path.join(path, j), os.path.join(path, "再生者-立绘-" + d[0] + "-" + d[1].split("、")[content[key]] + ".png"))
