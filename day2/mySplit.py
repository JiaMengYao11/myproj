if __name__ == '__main__':
    #Split函数的使用
    # split(str="", num=string.count(str)).
    # 参数
    # str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # num - - 分割次数。默认为 - 1, 即分隔所有。
    # 返回值
    # 返回分割后的字符串列表。

    #分割
    str = "u can u up , no can no B B"
    #全部分割
    ms=str.split(" ")
    print(ms)

    #只分割一次
    ms1=str.split(" ",1)
    print(ms1)