def checkSex(**cdict):
    name=input("请输入您的名字:")
    sex = input("请输入您的性别:")
    sdict={
        "男":"false",
        "men":"false",
        "女": "true",
        "girl": "true"
    }
    for k,v in sdict.items():
        if k=="false":
            print("{0}{1}你好".format(name,"男"))
            break
        else:
            print("{0}{1}你好".format(name, "女"))
            break
