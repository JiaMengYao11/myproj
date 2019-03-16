#文件-open-seek
if __name__ == '__main__':
    # seek(offset: int, whence: int = 0)：
    # 参数
    # Offset：指定偏移位置。
    # whence：指定偏移的策略。
    # 0：从文件的开头位置开始偏移。
    # 1：从文件的当前的位置开始偏移。
    # 2：从文件的末尾开始偏移。

    with open(r"C:\Users\ASUS\Desktop\myproj\day4\file\file.txt","r") as f:
        pass
        #查出所有字符的数量
        mf=f.seek(0,2)

        print(mf)