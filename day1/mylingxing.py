if __name__ == '__main__':
    #arr=input("请输入您要创建的菱形数量")
    arr=[1,2,3,4,5,6,7,8,9]
    for i in arr:
        for j in arr:
            if i<j:
                print(" ",end=" ")
        for k in arr[0:i-1]:
            print("*",end=" ")
        for j in arr:
            print("*",end=" ")
            if j==i:
                print()
                break
    for i in arr:
        for j in arr:
            print(" ",end=" ")
            if i==j :
                break
        for h in arr:
            if i<h:
                print("*",end=" ")
            if i<h-1:
                print("*",end=" ")
        print()