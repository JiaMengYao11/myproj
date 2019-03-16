if __name__ == '__main__':

    #while循环
    while True :
        hehe = input("hehe")

            #if判断
        if hehe == "q":
            break
    print(hehe)
    hehe=input("are you sure")
    if hehe=='yes':
        print("退出")
        print(hehe)

    #else判断
    else:
         print("退出")

    #字符串切片
    str = "good good study , day day up"
    str1 = "12121212121212"
    print(str[::-1])#翻转
    print(str[::-2])#回退2位
    print(str1[::2])
    print(str1[1:10:-1])#空
    print(str1[1:10:1])#翻转
    #for(i=str.length();i>=0;i+=-1)=str[::-1]
    #for(i=0;i<=str.length();i+=2)=str[::2]
    print(str.title())#首字母大写
    print(type(str))#显示变量类型

    print("hehe",end=" ")#end=“ ” 不换行加空格“ ”
    print("hehe")

    name="hehe"
    password="hehe"
    sex="hehe"
    #默认print的使用方式
    print(name,password,sex)

    #替换行尾的换行，输出不换行，用end参数实现
    print(name,password,sex,end=" ")

    #参数之间去掉分隔符（一个空格/l），使用sep参数实现
    print("---------")
    print(name,password,sex,sep=" ")

    #九九乘法表
    arr=[1,2,3,4,5,6,7,8,9]

    for i in arr:
        for j in arr :
            print(i,"*",j,"=",i*j,end=" ")
            if(i==j):
                print()
                break

    #Print格式化输出
    name=input("your name")
    print("my name is:{0}".format(name))

    print("my name is {0} , age is {1}".format("高碧云","27"))
