if __name__ == '__main__':
    #自定义异常
    #创建一个类，这个类是继承了Exception(所有异常父类
    #这个类扩展了一个方法show()
    class MyExcept(Exception):
        pass
        def show(self):
            print("xixi")

    #创建一个对象！
    me=MyExcept()
    #调用对象方法
    me.show()

    try:
        #手动抛出异常
        raise MyExcept
    except MyExcept as  me:
        print("raise MyExcept")
        #调用了自定义异常的扩展了的方法
        me.show()
