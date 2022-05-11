import os#首先导入os模块，进行文件的查找，修改，删除等操作一般都要事先导入os模块

def del_files(path):
    for root,dirs,files in os.walk(path):#（使用 os.walk ,这个方法返回的是一个三元tupple(dirpath(string), dirnames(list), filenames(list)), 其中第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.）

            for name in files:
                if '.md' in name:#判断某一字符串是否具有某一字串，可以使用in语句
                 os.remove(os.path.join(root,name))##os.move语句为删除文件语句
                 print('Delete files:',os.path.join(root,name))
if __name__=='__main__':
    path=r"04-JavaScript基础"#此为需要删除的路径
    del_files(path)#调用函数
