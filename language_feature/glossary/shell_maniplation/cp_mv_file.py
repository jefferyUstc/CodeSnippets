import shutil

src = ''
dst = ''
# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

# 如果你想保留被复制目录中的符号链接，像这样做
shutil.copytree(src, dst, symlinks=True)


def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('.pyc')]


shutil.copytree(src, dst, ignore=ignore_pyc_files)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))

# 使用 copytree() 复制文件夹的一个棘手的问题是对于错误的处理
# 例如，在复制过程中，函数可能会碰到损坏的符号链接，因为权限无法访问文件的问题等等
try:
    shutil.copytree(src, dst, ignore_dangling_symlinks=True)  # 忽略无效符号连接文件
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)


"""
path.split()  == [path.basename(), path.dirname()]
"""
