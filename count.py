import os
import shutil

dirs = os.listdir()

folders = {}
for dir in dirs:
    if dir == "count.py":
        continue
    folders[dir] = len(os.listdir(dir))

top25 = sorted(folders.items(), key=lambda item: item[1], reverse=True)[0:25]

for item in top25:
    print(item[0])
    shutil.copytree(os.path.join("D:/Unisinos/Inteligência Artificial/Birds Dataset/valid/", item[0]), os.path.join("D:/Unisinos/Inteligência Artificial/Birds Dataset/valid25/", item[0]))