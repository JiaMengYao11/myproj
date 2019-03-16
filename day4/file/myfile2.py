#File write()
#文件对象方法
#file.read()
# file.readlines()
# f.tell()
# f.seek()
# f.close()

if __name__ == '__main__':
    mlist=["ok","you","can","fine"]
    myf= open(r"C:\Users\ASUS\Desktop\myproj\day4\file.c","w")
    #w=写

    #判断文件是否具有可写权限
    mbool=myf.writable()
    print(mbool)
    #向文件写入一串字符串
    #返回值为写入多少个的字符
    zifi=myf.write("okokok")
    print("zifu={zifu}".format(zifu=zifi))

    #向文件写入多行
    #返回值为none

    myf.writelines(mlist)
    myf.close()