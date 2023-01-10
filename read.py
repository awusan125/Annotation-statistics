import os
 
def fn(path, tail2,f):
    for i in os.listdir(path):
        sub_path = os.path.join(path, i)
        if os.path.isdir(sub_path):  # 递归遍历子目录下文件及目录
            fn(sub_path, tail2,f)
        elif os.path.isfile(sub_path):  # 读取目录下文件
            tail1 = i.split('.')[-1]  # 取出后缀
            # 读取后缀为py的目标文件内容
            if tail1 == tail2:
                f.write(sub_path+'\n')
                
if __name__ == '__main__':
    path_from='/home/wzd/notebook/pycode/highStarCode/'
    path_out= "/home/wzd/notebook/pycode/test.txt"
    f= open(path_out,"w")
    key = fn(path_from, "py",f)
    f.close()
