if __name__ == '__main__':
    a="123456123456"
    b=set()
    for i in a:
        b.add(i)
        q=a.count(i)
    print(q)
    if q>=2:

            print(b)
