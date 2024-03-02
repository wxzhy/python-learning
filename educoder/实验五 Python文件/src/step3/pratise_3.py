'''
编写程序，列出某个文件夹及其子文件夹中包含搜索字符串的文件名字

'''
#---------------------------------begin-------------------------------
import os
filename,key=input(),input()
for root,dirs,files in os.walk(filename):
    for file in files:
        if key in file:
            print(os.path.join(root,file))




#---------------------------------end-------------------------------
