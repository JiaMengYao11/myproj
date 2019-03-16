
if __name__ == '__main__':
    # 输入两个人的生日，比较两个人年龄大小（50
    # 分）
    print("请输入两个人的生日")
    a=input()
    b=input()
    a1=a[0:4]#19971123
    b1=b[0:4]
    a2=a[4:6]
    b2=b[4:6]
    a3=a[6:]
    b3=b[6:]
    if int(a1)>int(b1):
        print("第二次输入的年龄大一些")
    elif int(a1)<int(b1):
        print("第一次输入的年龄大一些")
    elif int(a1)==int(b1):
        if int(a2)>int(b2):
            print("先输入的年龄大一些")
        elif int(a2)<int(b2):
            print("后输入的年龄大一些")
        elif int(a2)==int(b2):
            if int(a3)>int(b3):
                print("第一次输入的年龄大一些")
            elif int(a3)<int(b3):
                print("第二次输入的年龄大一些")
            elif int(a3)==int(b3):
                print("两个年龄一样大")