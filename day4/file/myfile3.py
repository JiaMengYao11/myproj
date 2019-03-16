#File read()
# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
# read(size);
# 参数
# size -- 从文件中读取的字节数。
# 返回值
# 返回从字符串中读取的字节。
if __name__ == '__main__':
    myf = open(r"C:\Users\ASUS\Desktop\myproj\day4\file.c")
    mbol=myf.readable()
    print(mbol)

    #读取全部文件的内容
    sum=myf.read()
    print(sum)

    #读取文件的一行
    rl=myf.readline()
    print(rl)

    #读取文件的所有行
    #返回一个列表
    mlist=myf.readline()
    print(mlist)

    #关闭
    myf.close()



