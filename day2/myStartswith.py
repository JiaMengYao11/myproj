if __name__ == '__main__':
    #Startswith方法的使用
    # 描述
    # Python startswith()
    # 方法用于检查字符串是否是以指定子字符串开头，
    # 如果是则返回
    # True，否则返回
    # False。
    # 如果参数beg和end指定值，则在指定范围内检查。
    #
    # startswith(str, beg=0, end=len(string));
    # 参数
    # str - - 检测的字符串。
    # strbeg - - 可选参数用于设置字符串检测的起始位置。
    # strend - - 可选参数用于设置字符串检测的结束位置。
    # 返回值
    # 如果检测到字符串则返回True，否则返回False。

    #判断字符串首是否“you”
    str = "you is very good!"
    ms=str.startswith("you")
    print(ms)

    # 判断字符串首是否“you”
    #从下标0开始查找
    ms1 = str.startswith("you",0)
    print(ms1)

    # 判断字符串首是否“you”
    # 从下标0开始查找
    #在下标20结束查找
    ms2 = str.startswith("you", 0,20)
    print(ms2)

