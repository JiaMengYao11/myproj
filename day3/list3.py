if __name__ == '__main__':
    #列表生成式-条件判断

    mlist=[i for i in range(1,11) if i%2==0]
    print(mlist)

    slist=list()
    for i in range(1,11):
        if i%2!=0:
            slist.append(i)
    print(slist)