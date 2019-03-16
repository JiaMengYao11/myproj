def aaa(a,b,c=""):
    if c:
        user={"a":a,"b":b,"c":c}
    else:
        user={"a":a,"b":b}
    return user

if __name__ == '__main__':
    #返回字典

    u=aaa("a","b","ddd")
    print(u)