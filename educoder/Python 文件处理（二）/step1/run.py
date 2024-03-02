# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 xlrd 模块读取每个合并单元格的内容并打印
# 这里需要在读取文件的时候添加个参数，将formatting_info参数设置为True，默认是False，否则可能调用merged_cells属性获取到的是空值。
import xlrd
f=input()
data=xlrd.open_workbook(f,formatting_info=True)
sheet1=data.sheet_by_name('Sheet1')
# print(sheet1.merged_cells)
for c in sheet1.merged_cells:
    print(sheet1.cell_value(c[0],c[2]))
########## End ##########