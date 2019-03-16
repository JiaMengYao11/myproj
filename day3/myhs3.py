def aaa(name,age,hh="xixi"):
    print("name={0}".format(name),end="@")
    print("age={0}".format(age),end="@")
    print("hh={0}".format(hh))
#让 实 参变 成 可选 的
if __name__ == '__main__':
    aaa(name="aaa",age="ass")
    aaa(name="aaa", age="ass",hh="hhh")