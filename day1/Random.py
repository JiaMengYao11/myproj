import random
if __name__ == '__main__':
    #Random的使用-randint
    #导入随机数生成的包
    #包括20
    v=random.randint(1,20)
    print(v)

    #Random的使用-randint
    #choice方法用于已经给定的序列中随机选择一个数
    #不包括尾数
    v1=random.choice(range(10))
    print(v1)


    #Random的使用-进阶使用
    #定义字符串
    str="qwertyuiopasdfghjklzxcvbnm"
    #定义新的字符串
    str1=""
    for i in range(5):
        str1+=random.choice(str)
        print(i,str1)