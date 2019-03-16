if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    llist=[]
    for i in klist:
        llist.append(i.strip())
    print(llist)
    qlist=set()
    for i in llist:
        qlist.add(i)
    print(qlist)
    for i in qlist:
        elist=llist.count(i)
        if elist>=2:
            print("有重复")

    a="aaaaaa"
    b=set()
    for i in a:
        b.add(i)
    print(a.__len__()-b.__len__())
    if a.__len__()-b.__len__()>=2:
        print("有重复")

    a1="asdfghjklasdfghjkl"
    b1=set()
    for i in a1:
        b1.add(i)
    print(a1.__len__()-b1.__len__())
    if a1.__len__()-b1.__len__()>=2:
        print("重复")

    a2="asdfghjklzzxcbnaaa"
    b2=set()
    for i in a2:
        b2.add(i)
    print(b2)
    for i in b2:
        c1=a2.count(i)
    print(c1)
    print("222222")
    if c1>=2:
        print("55555")
        print("重复的为{0}".format(i))

    s=["good","good","study"]
    for i in s:
        e=s.count(i)

        if e>=2:
            print(i)



