#传递列表-在函数中修改列表
def hanshu(name):
    name.append("gun")
    name.append("wulijie")
    name.append("gougou")
def hanshu2(name1):
    name1.append("jiamengyao")
    name1.append("wangjingwen")
    name1.append("gaoshijing")
if __name__ == '__main__':
    name=["sss","lll"]
    hanshu(name)
    print(name)
    name1=["eee","dddd"]
    hanshu2(name1)
    print(name1)