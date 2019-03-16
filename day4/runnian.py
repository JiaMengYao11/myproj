if __name__ == '__main__':
    print("请输入年份")
    a=int(input())
    print("请输入月份")
    b=int(input())
    print("请输入天")
    c=int(input())
    num=0
    list={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:31,10:31,11:30,12:31}
    if (a%4==0 and a%100!=0)or a%400==0:
        for k,v in list.items():
            num += v
            if k==b:
                break
        print("这是{0}年的第{1}".format(a,num+c))
    else:
        list[2] = 28
        for k,v in list.items():
            num += v
            if k==b:
                break
        print("这是{0}年的第{1}".format(a, num + c))