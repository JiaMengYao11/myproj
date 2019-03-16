import  random
if __name__ == '__main__':
    mlist=list()
    print(type(mlist))
    mlist.append("111")
    print(mlist)
    mlist.insert(0,"2222")
    print(mlist)
    mlist.append("高碧云是大沙雕")
    print(mlist)
    mlist.pop(1)
    print(mlist)
    del mlist[0]
    print(mlist)
    mlist.remove("高碧云是大沙雕")
    print(mlist)
    #del mlist
    #由于删除了整个列表，所以不能打印
    # print(mlist)
    mlist.append("111")
    mlist.append("111")
    mlist.append("111")
    mlist.append("111")
    mlist.append("111")
    print(mlist)
    mlist.clear()
    print(mlist)

    llist=[1,2,3,4,5]
    print(type(llist))

    llist[0]=20
    print(llist)
    for i in llist:
       pass

    slist=[2,5,6,8,7]
    #打乱顺序
    random.shuffle(slist)
    print(slist)

    #对列表进行升序排序
    slist.sort(reverse=False)
    print(slist)

    # 对列表进行降序排序
    slist.sort(reverse=True)
    print(slist)

    #默认True降序
    slist.sort()
    print(slist)

    #翻转
    slist.reverse()
    print(slist)

    #临时排序
    bb=sorted(slist,reverse=True)
    print(bb)