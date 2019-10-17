#! /usr/bin/python
# _*_ coding: utf-8 _*_


class OpenTextFile(object):
    """
    实现打开一个文件使用with,这里仅仅是个例子
    因为 open()本身就可以实现 with context
    """
    def __init__(self, file_path):
        self.file = file_path

    def __enter__(self):
        self.f = open(self.file, 'r', encoding='utf-8')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with OpenTextFile('./with_context.py') as f:
    print(f.readlines())
