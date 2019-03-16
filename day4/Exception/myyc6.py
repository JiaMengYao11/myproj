#异常处理-示例-加上异常处理
if __name__ == '__main__':
    #将可能会发生的异常的代码放入到这段代码中！
    try:
        # 打开一个不存在的文件。
        # 使用只读方式打开
        # 注意这段代码会发生异常
        # 如果不使用异常进行处理，就会直接结束
        yc = open("baby.text", "r")
        yc.close()
        
    #此处抓捕异常使用了异常 父类exception
    #一般来说应该是先处理子类的异常然后处理父类异常
    except Exception as e:
        print(e)

    #如果try没有发生异常
    #则会在执行完try代码后执行else中的代码
    else:
        print("exception else")

    #当处理完所有的异常后都会执行这段代码
    #不论发生异常与否，都会执行这段代码中的代码！

    finally:
        print("finally")