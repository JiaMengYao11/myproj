if __name__ == '__main__':
    #Count函数
    # count(sub, start=0, end=len(string))
    # 参数
    # sub - - 搜索的子字符串
    # start - - 字符串开始搜索的位置。默认为第一个字符, 第一个字符索引值为0。
    # end - - 字符串中结束搜索的位置。字符中第一个字符的索引为
    # 0。默认为字符串的最后一个位置。
    # 返回值
    # 该方法返回子字符串在字符串中出现的次数。

    str = "u can u up , no can no B B"
    mcount=str.count("up") # 该方法返回子字符串在字符串中出现的次数。
    print(mcount)

    #字符串开始搜索的位置
    mcount1 = str.count("can",1)
    if mcount1>=1:
        print("重复",mcount1,"次","重复的内容为“can”")
    print(mcount1)

    mcount2 = str.count("no", 1,30)
    print(mcount2)