if __name__ == '__main__':
    a="aaa"
    q=set()
    for i in a:
        q.add(i)
    print(a.__len__()-q.__len__())

    b="aaaaaaaaaaa"
    c=set()
    for i in b:
        c.add(i)
    for i in c:
           num = b.count(i)
    if num >= 2:
        print("重复的是{0},重复的次数为：{1}".format(i, num))

    d="asdasdasd"
    w=set()
    for i in d:
      w.add(i)

    print(d.__len__()-w.__len__())






