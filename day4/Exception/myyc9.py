#失败 时 一声不吭
#要 让 程序 在 失败 时 一声不吭， 可 像 通常 那样 编写 try 代码 块，
# 但在 except 代码 块 中 明确 地 告诉 Python 什么 都不 要做。
# Python 有一个 pass 语句， 可在代码 块 中 使用 它来 让 Python 什么 都不 要做；
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

    #有错不处理
    except ZeroDivisionError as  z:
        pass
    #如果没有发生异常，则执行这段代码
    else:
        print("sum={0}".format(sum))
    finally:
        print("结束，如果最后还有要处理的代码就在这里写！！！")