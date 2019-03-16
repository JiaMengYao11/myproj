if __name__ == '__main__':
    #Endswith的使用-示例
    str=" u can u up , no can no B B"
    #查看字符串是否以B结尾
    #实现该函数的返回值是布尔值
    mbool =str.endswith("B")
    print(mbool)
    #该方法指定了查找的范围！！
    mbool1=str.endswith("B",10,str.__len__())
    print(mbool1)