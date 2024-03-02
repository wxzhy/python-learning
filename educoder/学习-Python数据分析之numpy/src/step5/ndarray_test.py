import numpy as np

# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 input 获取一个字典，完成 ROI 提取
d=eval(input())
arr=np.array(d['image'])
x,y,w,h=d['x'],d['y'],d['w'],d['h']
roi=arr[x:x+h,y:y+w]
print(roi)


########## End ##########
