import  random

if __name__ == '__main__':
    a=[]
    for i in range(0,10):
        a.append(random.choice(range(0,10)))
    print(a)
    b=random.choice(range(0,10))
    a1=str(a)
    b1 = str(b)
    print(a1)
    print(b1)
    c=a1.find(b1)
    print(c)
    if c==-1:
        print("没有")