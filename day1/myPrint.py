if __name__ == '__main__':
    #Print函数的使用
    name="xixix"
    password="cici"
    sex="man"

    #默认print的使用方式
    print(name,password,sex)

    #替换行尾的换行，输出不换行，用end参数实现
    print(name,password,sex,end="===")

    #参数之间去掉分隔符（一个空格），使用sep参数实现
    print(name,password,sex,sep=" ")