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
    sset=set()
    for i in llist:
        sset.add(i)
    print(sset)
    for i in sset:
        count=llist.count(i)
        print("{0},{1}".format(i,count))
        d={i:i}
        print(d)