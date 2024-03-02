text = ''' abcdef 姓名：张三
年龄：39
性别男
职业  学生
籍贯：  地球 '''


###begin
text=text.strip()
text=text.replace(' ','')
text=text.replace('abcdef','')
text=text.replace('性别','性别：')
text=text.replace('职业','职业：')
print(text)

###end