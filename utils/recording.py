import psutil
import time
from multiprocessing import Process
import os


def monitor_memory(log_file=None, inter_val=0.5):
    """
    current just for single process recording, and can not get return value
    :param log_file: the directory or file path to save log
    :param inter_val: duration secs
    :return:
    """

    def wrapper(func):
        def log_memory_info(p: psutil.Process):
            nonlocal log_file, inter_val
            if log_file is None:
                log_file = './monitor_memory.log'
            elif os.path.isdir(log_file):
                log_file = os.path.join(log_file, 'monitor_memory.log')
            with open(log_file, 'a') as f:
                f.write('rss\tvms\n')
                while True:
                    try:
                        info = p.memory_info()
                    except:
                        os._exit(0)
                    f.write('{0}\t{0}\n'.format(str(info.rss / (1024 * 1024.)), str(info.vms / (1024 * 1024.))))  # vms
                    f.flush()
                    time.sleep(inter_val)

        def core_wrapper(*args, **kwargs):
            if func.__code__.co_argcount == 0:
                p: Process = Process(target=func)
            else:
                p: Process = Process(target=func, args=(args, *kwargs))
            p.start()
            _p = psutil.Process(p.pid)
            _process = Process(target=log_memory_info, args=(_p,))
            _process.start()
            _process.join()
            p.join()

        return core_wrapper
    return wrapper
