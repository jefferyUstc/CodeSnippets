import os
import sys


def find_file(start, name):
    for relpath, dirs, files in os.walk(start):
        """
        os.walk返回一个三元组，包含
        相对于查找目录的相对路径;
        一个该目录下的目录名列表;
        那个目录下面的文件名列表
        """

        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    find_file(sys.argv[1], sys.argv[2])
    """
    类似的还有glob
    """
