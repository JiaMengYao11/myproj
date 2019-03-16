class MyExcept (Exception) :

    def end(self):
        print(" 11 ")

if __name__ == '__main__':
    try:
        print(5/0)

        raise MyExcept #自定义异常的出发条件

    except MyExcept as e:#自定义异常
        print(e)
        e.end()
    except ZeroDivisionError as e :
        print(e)
        print("除数为0异常")
    except Exception as e :
        print(e)
        print("自定义异常继承的父类异常（最大异常）")
    else:
        print("程序完毕")