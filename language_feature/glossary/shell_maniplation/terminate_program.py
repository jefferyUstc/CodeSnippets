import sys

# 方式1
sys.stderr.write('It failed!\n')
raise SystemExit(1)

# 方式2
raise SystemExit('It failed!\n')

# sys.exit(n) 退出程序引发SystemExit异常, 可以捕获异常执行些清理工作. n默认值为0, 表示正常退出. 其他都是非正常退出. 还可以sys.exit("sorry, goodbye!"); 一般主程序中使用此退出.
# os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出
# exit()/quit(), 抛出SystemExit异常. 一般在交互式shell中退出时使用
