import zipfile
import os
import re
import time
import shutil

def substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr
def ImgSrc(data,src,dest):
    return re.sub(re.escape(src),dest,data)

def n2c(nzip,out,c,tags,date,name,link,toc,math,comments,mermaid,title):
    # print(f"categories : {c}\ntags : {tags}\ndate : {date}\nname : {name}\nlink : {link}\ntoc : {toc}\nmath : {math}\ncomments : {comments}\nmermaid : {mermaid}")
    image=0
    Zip=zipfile.ZipFile(nzip)
    if len(Zip.namelist())>=2:
        filename=substr(Zip.namelist())
        image=1
    else:
        filename=Zip.namelist()[0][:-3]
    Zip.extractall('./')

    zip_path = os.path.realpath(nzip)
    out_path = os.path.realpath(out) 
    replaced_filename = '-'.join(filename.replace(" ","-").lower().split('-')[:-1])
    out_filename=time.strftime('%Y-%m-%d-')+replaced_filename
    
    categories=c.__repr__().replace("'","").replace('"','')
    tags=f"[{tags}]"
    date=date or time.strftime('%Y-%m-%d %H:%M:%S +0900', time.localtime(time.time()))
    
    front=f"""---
title: {title}
categories: {categories}
tags : {tags}
date : {date}
author:
    name: {name}
    link: {link}
toc: {str(toc).lower()}
comments: {str(comments).lower()}
mermaid: {str(mermaid).lower()}
math: {str(math).lower()}
---
"""
    #remove duplicated md
    filelist=os.listdir(out_path+"/_posts/")
    for f in filelist:
        if f.endswith(replaced_filename+".md"):
            os.remove(out_path+"/_posts/"+f)
    imglist=os.listdir(out_path+"/assets/img/")
    for f in imglist:
        if f.endswith(replaced_filename):
            shutil.rmtree(out_path+"/assets/img/"+f)
    #replace img src
    with open(filename+".md","r") as f:
        data=ImgSrc(f.read(),filename.replace(" ","%20"),"/assets/img/"+out_filename)

    #remove duplicated img folder
    # folderlist=os.listdir(out_path+"/assets/img/")
    # print(f"Image folder PREV ",end='')
    # print(folderlist)
    # for f in folderlist:
    #     if f.endswith(replaced_filename):
    #         shutil.rmtree(out_path+"/assets/img/"+f)

    #add md front data
    data=front+'\n'.join(data.split('\n')[1:])

    #remove duplicated img folder and move
    if image:
        if os.path.exists(out_path+"/assets/img/"+out_filename):
            shutil.rmtree(out_path+"/assets/img/"+out_filename)
        os.rename(filename,out_path+"/assets/img/"+out_filename)
    #write md file
    with open(out_path+"/_posts/"+out_filename+".md","w") as f:
        f.write(data)
    folderlist=os.listdir(out_path+"/assets/img/")
    print(f"Image folder ",end='')
    print(folderlist)
    
    folderlist=os.listdir(out_path+"/_posts")
    print(f"Posts folder ",end='')
    print(folderlist)

    print(f"[+] success upload")
    if image:
        print(f"[+] image to {out_path+'/assets/img/'+out_filename}")
    print(f"[+] md to {out_path+'/_posts/'+out_filename+'.md'}")
