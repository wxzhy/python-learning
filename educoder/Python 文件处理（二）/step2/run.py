import usr

if __name__ == "__main__":
    path = input()
    dat = usr.Read(path)
    for s in range(3):#每次评测有三次查询
        name = input()
        if(name in dat.keys()):
            print(dat[name])
        else:
            print("没有%s城市的温度数据" % (name))