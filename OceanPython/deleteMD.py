import os
import re
import time


# 用os.walk函数遍历目录实现文件查找
def findfile2(issueid, rootdir):
    list_dirs = os.walk(rootdir)
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    for root, dirs, files in list_dirs:
        for nowfile in files:
            print(nowfile.startswith(issueid))

            if nowfile.startswith(issueid):
                os.remove(nowfile)

            # if filename.find('*') >= 0:
            #     regularstring = filename
            #
            #     if filename.rfind(r'.') > 0:  # 从右往左查找扩展名点号
            #         regularstring = regularstring.replace(r'.', r'\.')  # 将正则表达式中扩展名的.点号进行转义处理
            #     regularstring = regularstring.replace('*', r'[\w.]*')
            #     if re.match(regularstring, nowfile):
            #         fullname = os.path.join(root, nowfile)
            #         filenames.append(fullname)
            #         print("1"+fullname)
            # else:
            #     if nowfile == filename:
            #         fullname = os.path.join(root, nowfile)
            #         filenames.append(fullname)
            #         print("2"+fullname)


filenames = []


# 递归遍历根目录下的所有目录查找指定文件
def findfile(issueid, rootdir):
    for fileordir in os.scandir(rootdir):
        if fileordir.is_dir():
            findfile(issueid, fileordir.path)
        else:
            if fileordir.name.startswith(issueid):
                print(fileordir.name)
                print(len(list(fileordir.name)))
                if list(fileordir.name) != 0:
                    print(fileordir.name)

                # os.remove(os.path.join(rootdir, fileordir.name))
                # os.remove(os.path.join(rootdir, fileordir.name))


if __name__ == '__main__':
    starttime = time.time()
    filenames = []
    filenames.clear()
    findfile("8_", "./")
    # findfile2("9_", "./")
    endtime = time.time()
    print(f"搜索用时:{endtime - starttime:.3f}")
    # ret = input(f"你确认删除以上{len(filenames)}个文件吗？[y/n]")
    # if ret == 'y':
    #     print("开始删除文件:")
    #     for delfile in filenames:
    #         try:
    #             os.remove(delfile)
    #             print(f"删除文件{delfile}成功！")
    #         except Exception as e:
    #             print(f"删除文件失败：{e}")
