import day4.quest1.quest1 as q1
import day4.quest1.quset2 as q2
import day4.quest1.quset3 as q3
import day4.quest1.quest4 as q4
if __name__ == '__main__':

    ldict={
        1:"1.输入用户姓名及性别，然后给出下列的提示",
        2:"2.随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"3.注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"4.从键盘输入一行字符串，判断是否是回文数"
    }
    fdict={
        1:q1.checkSex,
        2:q2.suiji,
        3: q3.user,
        4:q4.ziFuChuan
    }
    while True:
        for i in ldict.values():
            print(i)
        xz=input("请输入您要选择的服务:")
        if int(xz)==1:
            q1.checkSex()
        elif int(xz)==2:
            q2.suiji()
        elif int(xz)==3:
            q3.user()
        elif int(xz)==4:
            q4.ziFuChuan()
