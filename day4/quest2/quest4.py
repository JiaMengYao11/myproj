def ziFuChuan():
    huiwen=input("请输入一行字符串：")
    print(huiwen)

    huiwen1=[]
    huiwen2=[]
    for i in huiwen:
        huiwen1.append(i)
        huiwen2.append(i)
    huiwen1.reverse()
    print(huiwen1)
    print(huiwen2)
    if huiwen2==huiwen1:
            print("该字符串是回文")
    else:
            print("该字符串不是回文")