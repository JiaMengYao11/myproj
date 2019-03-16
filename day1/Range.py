if __name__ == '__main__':
    #Range的使用
    #通过range顺序产生10个数
    #留头不留尾
    list=range(10)
    for i in list:
        print(i,end="ggggg")

    #通过range产生1到10范围内的整数
    #第三个“2”，是步长值
    # 留头不留尾
    list1=range(1,10,2)
    print()
    for i in list1:
        print(i,end="/////")

    #Range的使用-range的使用
    #使用range构造一个列表
    #注意此时的起始位置和结束位置由大到小
    #后面的步长是负值
    print()
    list3=range(10,-2,-1)
    for i in list3:
        print(i,end="--")