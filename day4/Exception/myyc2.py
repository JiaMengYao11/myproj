if __name__ == '__main__':

    #异常-处理 ZeroDivisionError 异常
    try:
        print(100/0)
    except ZeroDivisionError as  z:
        pass

        print("ZeroDivisionError")
        print(z)
    print("除数不能为0")