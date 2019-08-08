import sys


def get_version(brief=False):
    if not brief:
        return sys.version_info
    return sys.version_info[0]

