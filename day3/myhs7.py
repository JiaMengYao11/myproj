#传递列表-禁止 函数 修改 列表
def hanshu(name):
    name.append("gunnimade")
    #假的
    print(name)
if __name__ == '__main__':
    name=["aaa","hehe","okok"]
    hanshu(name[:])
    #真的
    print(name)