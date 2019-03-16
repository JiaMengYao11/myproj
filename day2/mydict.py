if __name__ == '__main__':

    print("创建字典方法一")
    mdict={"qq":1,"ww":2,"ee":3}
    print("create not null way-> type=",mdict)

    print("创建字典方法二")
    sdict=({"qq":1,"www":2,"rrr":33})
    print("create not null way-> type=", sdict)

    print("创建字典方法三")
    adict=dict(qq=1,ss=2,dd=9)
    print("create not null way-> type=", adict)

    print("创建字典方法四")
    qdict=dict([("qq",1),("ww",3),("dd",5)])
    print("create not null way-> type=", qdict)
