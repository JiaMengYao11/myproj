import random

if __name__ == '__main__':
    a=[]
    for i in range(0,20):
        a.append(random.choice(range(1,10)))

    b=random.choice(range(0,2))
    print(b)
    print(a)
    c=str(a)
    e = str(b)
    print(type(c))
    d=c.find(e)
    if d==-1:

        print("no")

    else:
        print("yes")

