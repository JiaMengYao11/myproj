if __name__ == '__main__':
    mlist=[1,2,3,5,6,7,8]
    print(type(mlist))
    for i in mlist:
        print("mlist[{0}]={1}".format(i.__index__(),1),end="**")
    print()

    #内建结构-列表-改变列表中的值
    slist=['s',5,8,5,6,5,5,9]
    #更改下标为1的值
    slist[1]=200
    for i in slist:
        print(i,end="//")

    #内建结构-列表-操作列表（访问）
    xlist=[1,5,8,4,6,2,5]
    print()
    for i in xlist:
        print(i,end="-")
    print()
    #访问下标为2的元素的值
    print("xlist[{0}]={1}".format(xlist[2].__index__(),xlist[2]))