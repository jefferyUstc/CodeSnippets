"""
1、使用 subprocess.check_output() 函数是执行外部命令并获取其返回值的最简单方式
2、subprocess 模块对于依赖TTY的外部命令不合适用
"""

import subprocess

try:
    out_bytes = subprocess.check_output(['ls', '-h'], stderr=subprocess.STDOUT, timeout=5)
    # 如果你想让命令被一个shell执行，传递一个字符串参数
    # out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
except subprocess.CalledProcessError as e:
    """
    If the exit code was non-zero it raises a CalledProcessError
    """
    out_bytes = e.output  # Output generated before error
    code = e.returncode  # Return code
else:
    out_text = out_bytes.decode('utf-8')
    print(out_bytes)

"""
如果你需要对子进程做更复杂的交互，比如给它发送输入，你得采用另外一种方法。 这时候可直接使用 subprocess.Popen 类
"""
# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = None
if stderr is not None:
    err = stderr.decode('utf-8')
print(out, err, sep='\n*\n')
