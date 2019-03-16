



if __name__ == '__main__':
    # 定义一个函数
    # 如果参数是0
    #   则手动跑出异常
    def mfun(v):
        if v == 0:
            raise Exception("ok")
            pass
    try:
        #抓捕异常并打印异常信息
        mfun(0)
    except Exception as e:
        print("excetp->{0}".format(e))


    #查看异常处理之后会否影响后续程序的运行