if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9]
    print(arr)
    for i in arr:
        for j in arr:
            print(i,"*",j,"=",i*j,end=" ")
            if i==j:
                print()
                break

    