import random

if __name__ == '__main__':
    a=[]
    for i in range(0,10):
        a.append(random.choice(range(0,10)))
    print(a)
    a.sort()
    print(a)

    print('\n'.join([''.join([('Love'[(x - y) % len('Love')]
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
            for x in range(-30, 30)]) for y in range(30, -30, -1)]))

