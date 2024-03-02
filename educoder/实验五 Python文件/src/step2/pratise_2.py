import os
import os.path
# MergeTxt函数实现文件合并功能，filepath是要合并文件文件所在目录
# outfile是合并后生成的新文件的文件名
def MergeTxt(filepath,outfile):
    #请在此添加代码，实现文件合并
    #********** Begin *********#
    out=open(outfile,'w')
    for root,dirs,files in os.walk(filepath):
        for file in files:
            with open(os.path.join(root,file),encoding='utf-8') as f:
                out.write(f.read())
                out.write('\n')
    #********** End *********#

#在main函数中输入要合并文件所在文件夹
#输出合并后的文件内容
def main():
    filepath=input()  #输入要合并文件所在文件夹
    outfile=input()  #输入合并后的文件路径及文件名
    #请在此添加代码，调用函数并输出合并后的文件内容
    #********** Begin *********#
    MergeTxt(filepath,outfile)
    print(open(outfile).readlines())
    #********** End *********#
main()
