if __name__ == '__main__':
    #使用 异常 避免 崩溃-未使用异常
    #创建 一个 只 执行 除法 运算 的 简单 计算器：

    print("输入两个数，计算除法！！")
    print("输入t退出")

    while True:
        print("\t")#空格
        num1=input("First num")
        if num1=='q':
            break
        num2=input("second num")
        if num2=='q':
            break
        sum=int(num1)/int(num2)
        print(sum)