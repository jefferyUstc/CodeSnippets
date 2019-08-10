import sys
from psutil import cpu_count, Process
from multiprocessing import cpu_count


def get_version(brief=False):
    if not brief:
        return sys.version_info
    return sys.version_info[0]


def get_cpu_cores(logical=False):
    return cpu_count(logical=logical)


def get_cpu_cores2(logical=False):
    return cpu_count(logical=logical)


def get_process_memory(pid):
    if isinstance(pid, int):
        process = Process(pid)
    else:
        raise TypeError('pid should be int type')
    info = process.memory_info()
    return {
        'vms': info.vms,
        'rss': info.rss
    }
