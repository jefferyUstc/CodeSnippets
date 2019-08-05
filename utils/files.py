import re
import shutil
import fnmatch
from os import getcwd, listdir, remove, makedirs, walk
from os.path import join, isdir, isfile, exists


def load_file_list(path=None, regx=r'\.csv', printable=True):
    """Return a file list in a folder by given a path and regular expression.
    Parameters
    ----------
    path : a string or None
        A folder path.
    regx : a string
        The regx of file name.
    printable : boolean, whether to print the files infomation.
    """
    if not path:
        path = getcwd()
    file_list = listdir(path)
    return_list = []
    for f in file_list:
        if re.search(regx, f):
            return_list.append(join(path, f))
    if printable:
        print('Match file example = %s' % (str(return_list[0])))
        print('Number of files = %d in path: %s' % (len(return_list), path))
    return return_list


def load_folder_list(path=""):
    """Return a folder list in a folder by given a folder path.

    Parameters
    ----------
    path : str
        A folder path.

    """
    return [join(path, o) for o in listdir(path) if isdir(path.join(path, o))]


def file_exists(file_path):
    """Check whether a file exists by given file path."""
    return isfile(file_path)


def folder_exists(folder_path):
    """Check whether a folder exists by given folder path."""
    return isdir(folder_path)


def del_file(file_path):
    """Delete a file by given file path."""
    remove(file_path)


def del_folder(folder_path):
    """Delete a folder by given folder path."""
    shutil.rmtree(folder_path)


def exists_or_mkdir(path, verbose=True):
    """Check a folder by given name, if not exist, create the folder and return False,
    if directory exists, return True.

    Parameters
    ----------
    path : str
        A folder path.
    verbose : boolean
        If True (default), prints results.

    Returns
    --------
    boolean
        True if folder already exist, otherwise, returns False and create the folder.

    """
    if not exists(path):
        if verbose:
            print("[*] creates %s ..." % path)
        makedirs(path)
        return False
    else:
        if verbose:
            print("[!] %s exists ..." % path)
        return True


def find_file_generator(pattern, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    """
    for path, dir_list, file_list in walk(top):
        for name in fnmatch.filter(file_list, pattern):
            yield join(path, name)
