#文件-open-使用with语句
# 含义
# 使用with语句能够避免忘记关闭已经打开的文件。
# With语句使用一种称为“上下文管理协议的技术”，能够自动判断文件的作用域
# 能够关闭不在使用的却仍处于打开状态的文件描述符。
#With语句的使用方法
if __name__ == '__main__':
    with open(r"C:\Users\ASUS\Desktop\myproj\day4\file\file.txt","r") as f:
        while True:
            mline=f.readline()
            print(type(mline))
            if mline == "":
                break
            print(mline,end="-")