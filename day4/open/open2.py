#文件-open-list
if __name__ == '__main__':
    with open(r"C:\Users\ASUS\Desktop\myproj\day4\file\file.txt","r") as  f:
        mlist=list(f)
        for i in mlist:
            print(i,end="-")