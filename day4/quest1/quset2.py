import random
def suiji():
    a=[]
    for i in range(10):
        a.append(random.choice(range(0,20)))

    b= []
    for i in range(10):
        b.append(random.choice(range(0, 20)))

    print(type(a))

    a1=str(a)
    b1 = str(b)
    c=[a+b]

    print(c)

