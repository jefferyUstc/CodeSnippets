import fileinput

with fileinput.input(inplace=False,
                     backup='.bak',
                     bufsize=0,  # 请忽略改参数，其实没啥用
                     mode='r',
                     openhook=fileinput.hook_encoded('utf-8')) as f:
                    # fileinput.hook_compressed()
    for line in f:
        if not f.filename() == '2  .txt':
            print(f.filename(),  # 当前文件文件名
                  f.lineno(),  # 当前已读总行数
                  f.filelineno(),  # 当前文件行号
                  f.fileno(),  # 文件number, 0表示stdin,3代表命令行参数传入的文件，4代表函数参数传入的文件
                  f.isfirstline(),  # 是否为首行
                  f.isstdin(),  # 是否为标准输入
                  line  # 当前行的内容
                  )
            # f.readline()  # 读取一行内容，并将指针向下一行移动
        else:
            f.nextfile()  # 跳到下一个文件


# 使用方法
# ls | fileinput_module.py
# fileinput_module.py 1.txt 2.txt 3.txt




