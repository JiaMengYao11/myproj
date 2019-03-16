if __name__ == '__main__':
    # 使用 异常 避免 崩溃 - 使用异常
    print("输入两个数，计算除法")
    print("输入T退出!")

    while True:
        print("进行除数计算")
        num1=input("First num")
        if num1=='t':
            break
        num2=input("Secont num")
        if num2=='t':
            break
    #抓捕异常，如果发升则进入异常的分值代码块
    try:
        sum=int(num1)/int(num2)
    #异常分值代码块
    #在代码中处理异常
    except ZeroDivisionError as  z:
        print("ZeroDivisionError")
    #如果没有发生异常，则执行这段代码
    else:
        print("sum={0}".format(sum))
    finally:
        print("结束，如果最后还有要处理的代码就在这里写！！！")
