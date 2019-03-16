#传递 任意 数量 的 实 参
# 有时候， 你 预先 不知道 函数 需要 接受 多少 个 实 参，
# 好在 Python 允许 函数 从 调用 语句 中 收集 任意 数量 的 实 参。
# 形 参 名前加一个 * （ 星号）是 让 Python 创建 一个  空 元 组，
# 并将 收到 的 所有 值 都 封装 到 这个 元 组 中。
# 注意， Python 将 实 参 封装 到 一个 元 组 中，
# 即便 函数 只 收到 一个 值 也 如此.
def hanshu( *name):
    print(type(name))
    for i in name:
        print(i)
if __name__ == '__main__':
    hanshu("ni","shi","sha","diao")
