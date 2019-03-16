if __name__ == '__main__':
    a="aaaaaa"
    b=set()
    for i in a:
        b.add(i)
    if a.__len__()-b.__len__()>=2:
        print("重复")