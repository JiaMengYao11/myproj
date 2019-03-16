if __name__ == '__main__':
    #Find-基本语法
    # 基本语法
    # str.find(str, beg=0, end=len(string))
    # 方法检测字符串中是否包含子字符串
    # str 。
    # 参数
    # str - - 指定检索的字符串
    # beg - - 开始索引，默认为0。
    # end - - 结束索引，默认为字符串的长度。
    # 返回值
    # 如果包含子字符串返回开始的索引值，否则返回 - 1。

    #Find-使用示例
    str="good good study day day up"
    ms=str.find("up")
    print(ms)

    #指定了从字符串的起始下标1开始查找“good”
    ms1=str.find("good",1)
    print(ms1)

    # 指定了从字符串的起始下标1开始查找“good”
    #指定看到字符串30结束本次查找
    ms2 = str.find("up", 1,30)
    print(ms2)