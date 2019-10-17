from glob import glob, glob0, glob1

from os import walk

"""
walk(top='',  # 所要遍历的目录路径
     topdown=True,  # 为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)
     onerror=None,  # 可选，需要一个 callable 对象，当 walk 需要异常时，会调用
     followlinks=False  # 为 True，则会遍历目录下的symbolic link实际所指的目录(默认关闭)
     )
"""
for root, dirs, files in walk('./'):
    print('root:', root, '\n***\n')  # 当前root路径
    print('files:', files, '\n***\n')  # 当前root文件夹下面的文件
    print('dirs:', dirs, '\n***\n')  # 当前root文件夹下的目录


"""
glob(pathname='', recursive=False)
"""
file_list = glob('./*/*.py')
print(file_list)

