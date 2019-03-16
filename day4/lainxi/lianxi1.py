if __name__ == '__main__':
    #a="20180205"
    a=input("请输入年月份")
    a1=a[0:4]
    a2=a[4:6]
    a3=a[6:]
    if int(a2)>=1:
        if int(a3)<=31 and  int(a3) >=1:
            print("这是{0}年的第{1}天".format(a1,int(a3)+31*(int(a2)-1)))

