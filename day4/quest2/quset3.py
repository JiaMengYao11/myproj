def user():
    while True:
        name = input("请输入您的姓名:")
        if name.__len__()<6:
            print("您输入的姓名不合法，请重新输入")
        else:
            email = input("请输入您的EMAIL号:")
            email1=email.find("@")
            print(email1)
            if email1==-1:
                    print("您输入的email号不合法，请重新输入")
                    user()
        break
    if name.__len__()>=6 and email1!=-1:
        print("您的姓名是：{0}，email号是：{1}".format(name,email))

