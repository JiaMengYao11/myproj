if __name__ == '__main__':
    #Index函数
    # str.index(str, beg=0, end=len(string))
    # 参数
    # str - - 指定检索的字符串
    # beg - - 开始索引，默认为0。
    # end - - 结束索引，默认为字符串的长度。
    # 返回值
    # 如果包含子字符串返回开始的索引值，否则抛出异常。

    #Index-示例
    str="u can u up , no can no B B"
    #查找up字符串
    ms=str.index("up")
    print(ms)

    #从下标1开始查找字符串“no”
    ms1=str.index("no",1)
    print(ms1)

    # 从下标1开始查找字符串“no”
    #在下标20结束查找
    ms2 = str.index("B", 1,30)
    print(ms2)