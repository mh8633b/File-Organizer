import os
import shutil

files = {

    "IMAGES": [".jpg", ".jpeg", ".png", ".gif"],
    "AUDIO":[".mp3",".m4a",".m4b",".m4p",".wma",".wav"],
    "VIDEO":[".mp4",".flv",".wmv",".3gp",".mpg","webm"],
    "TEXT":[".txt",".pdf"],
    "HTML": [".html5", ".html", ".hml", ".xhtml"],
    "ARCHIVES" :[".zip",".rar","xar",".iso",".tar",".gz"],
}

directories = {"images", "audio", "videos", "text", "html", "archives"}

for folders in directories:
    try:
        os.mkdir(folders)
    except:
        pass

filenames = [f for f in os.listdir()]


for i in filenames:
    for extension in files["IMAGES"]:
        if i.endswith(extension):
            shutil.move(i, "images")

    for extension in files["AUDIO"]:
        if i.endswith(extension):
            shutil.move(i, "audio")

    for extension in files["VIDEO"]:
        if i.endswith(extension):
            shutil.move(i, "videos")

    for extension in files["TEXT"]:
        if i.endswith(extension):
            shutil.move(i, "text")

    for extension in files["HTML"]:
        if i.endswith(extension):
            shutil.move(i, "html")

    for extension in files["ARCHIVES"]:
        if i.endswith(extension):
            shutil.move(i, "archives")

for y in directories:
    try:
        os.rmdir(y)
    except:
        pass

