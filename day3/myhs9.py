#传递 任意 数量 的 实 参
#可将 函数 编写 成 能够 接受 任意 数量 的 键— 值对。
#函数前面有一个特殊符号**双星
#该参数的类型是字典
def hanshu(**name):
    print(type(name))
    for i in name.items():
        print(i)
if __name__ == '__main__':
    hanshu(a="dddd",s="qqqq")