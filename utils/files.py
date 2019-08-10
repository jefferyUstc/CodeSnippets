from __future__ import print_function

import fnmatch
import re
import shutil
import sys
import tarfile
import zipfile
from os import getcwd, listdir, remove, makedirs, walk, stat
from os.path import join, isdir, isfile, exists

import progressbar


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


def maybe_download_and_extract(filename, working_directory, url_source, extract=False, expected_bytes=None):
    """
    Checks if file exists in working_directory otherwise tries to dowload the file,
    and optionally also tries to extract the file if format is ".zip" or ".tar"

    Parameters
    -----------
    filename : str
        The name of the (to be) dowloaded file.
    working_directory : str
        A folder path to search for the file in and dowload the file to
    url_source : str
        The URL to download the file from
    extract : boolean
        If True, tries to uncompress the dowloaded file is ".tar.gz/.tar.bz2" or ".zip" file, default is False.
    expected_bytes : int or None
        If set tries to verify that the downloaded file is of the specified size, otherwise raises an Exception,
        defaults is None which corresponds to no check being performed.

    Returns
    ----------
    str
        File path of the dowloaded (uncompressed) file.

    Examples
    --------
    >>> down_file = maybe_download_and_extract(filename='ERR166303.vcf.zip',
    ...                                            working_directory='data/',
    ...                                            url_source='http://galaxy.ustc.edu.cn:30803/liunianping/')

    """
    if sys.version_info[0] == 2:
        from urllib import urlretrieve
    else:
        from urllib.request import urlretrieve

    def _download(filename, working_directory, url_source):

        progress_bar = None

        def _dlProgress(block_num, block_size, total_size, pbar=progress_bar):
            nonlocal progress_bar
            if total_size != 0:
                if progress_bar is None:
                    progress_bar = progressbar.ProgressBar(maxval=total_size)
                    progress_bar.start()
                downloaded = block_num * block_size
                if downloaded < total_size:
                    progress_bar.update(downloaded)
                else:
                    progress_bar.finish()
                    progress_bar = None

        filepath = join(working_directory, filename)
        urlretrieve(url_source + filename, filepath, reporthook=_dlProgress)

    exists_or_mkdir(working_directory, verbose=False)
    filepath = join(working_directory, filename)

    if not exists(filepath):
        _download(filename, working_directory, url_source)
        statinfo = stat(filepath)
        print('Succesfully downloaded %s %s bytes.' % (filename, statinfo.st_size))  # , 'bytes.')
        if not (expected_bytes is None) and (expected_bytes != statinfo.st_size):
            raise Exception('Failed to verify ' + filename + '. Can you get to it with a browser?')
    if extract:
        if tarfile.is_tarfile(filepath):
            tarfile.open(filepath, 'r').extractall(working_directory)
        elif zipfile.is_zipfile(filepath):
            with zipfile.ZipFile(filepath) as zf:
                zf.extractall(working_directory)
        else:
            print("Unknown compression_format only .tar.gz/.tar.bz2/.tar and .zip supported")
    return filepath
