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

    ldict=[]
    print(type(klist))
    #print(ldict)
    c=set()
    for i in klist:
        ldict.append(i.strip())

    #print(ldict)

    for i in ldict:
        c.add(i)
    #print(c)
    for i in c:
        c1 = ldict.count(i)
        d={i:c1}
        #print(d)
        # print("重复的次数是{0},重复的内容为{1}".format(c1,i))

    d={i:i for i in c}
    print(d)

    for i in c:
        d[i]=i
    print(d)


