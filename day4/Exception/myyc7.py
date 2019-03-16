if __name__ == '__main__':
    #自定义一个异常类
    class MyException(ValueError):
        pass
    try:
        print("异常在前")
        #手动跑出异常，注意！抛出的是自定义异常
        raise MyException
        print("异常在后")

    #抓捕自定义异常
    except MyException as me:
        print("catch MyExctption")

    #抓捕自定义异常的父类
    except ValueError as ve:
        print("catch ValueError")

    #抓捕所有异常的父类
    except Exception as e:
        print("exception")
        print(e)

        # 如果try没有发生异常
        # 则会在执行完try代码后执行else中的代码
    else:
        print("exception else")

        # 当处理完所有的异常后都会执行这段代码
        # 不论发生异常与否，都会执行这段代码中的代码！

    finally:
        print("finally")