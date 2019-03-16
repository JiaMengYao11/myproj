if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    s=[]
    for i in klist:
        s.append(i.strip())
    print(s)

    c=set()
    for i in s:
        c.add(i)

    print(c)

    for i in c:
        d=s.count(i)
        print(d)
        x={i:d}
        print(x)

    if __name__ == '__main__':
        klist = [
            "good ", "good ", "study",
            " good ", "good", "study ",
            "good ", " good", " study",
            " good ", "good", " study ",
            "good ", "good ", "study",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
            " day ", "day", " up",
        ]

        s = []
        for i in klist:
            s.append(i.strip())
        print(s)

        c = set()
        for i in s:
            c.add(i)

        print(c)

        for i in c:
            d = s.count(i)
            print(d)
            x = {i: d}
            print(x)