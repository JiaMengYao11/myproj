import time
if __name__ == '__main__':
    #文件-open-read-示例3
    with open(r"C:\Users\ASUS\Desktop\myproj\day4\file\file.txt","r") as f:
        pass
        while True:
            #每次只读文件中的一个字符
            c=f.read()
            if c=="":
                break
            print(c,end="////")
            time.sleep(10)#延迟十秒