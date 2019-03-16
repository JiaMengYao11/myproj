if __name__ == '__main__':
    #字典-内置函数
    #Len（）：求字典的长度。
    print("#字典-内置函数")
    print("#Len（）：求字典的长度。")
    mdict = {"qq": "qq", "ee": "ee"}
    ms=mdict.__len__()
    print(ms)
    ms2=len(mdict)
    print(ms2)

    #Str（）：将字典转换成一个字符串。
    ms1=mdict.__str__()
    print(ms1)
    ms3=str(mdict)
    print(ms3)

    #Type（）：显示字典的类型。
    print(type(ms1))
