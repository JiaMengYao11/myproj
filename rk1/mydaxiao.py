
import random
if __name__ == '__main__':
    one=input("输入一个整数")
    two=random.randint(1,10)
    if one>two:
        print("第一个数大于第二个数")
    else:
        print("第二个数大于第一个数")