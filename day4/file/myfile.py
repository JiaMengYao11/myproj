if __name__ == '__main__':
    #文件-open
    try:
        myf=open(r"C:\Users\ASUS\Desktop\myproj\day4\file.c")

    except OSError:
        print("oserror")
    except Exception:
        print("Execption")
    else:
        #退出
        myf.close()