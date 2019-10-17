"""
创建或解压常见格式的归档文件（比如.tar, .tgz或.zip）
"""
import shutil

print(shutil.get_archive_formats())  # 所有支持的格式
"""
[('bztar', "bzip2'ed tar-file"),
('gztar', "gzip'ed tar-file"),
('tar', 'uncompressed tar file'),
('xztar', "xz'ed tar-file"),
('zip', 'ZIP file')]
"""
shutil.unpack_archive(filename=None, extract_dir=None, format=None)
shutil.make_archive(base_name=None, format=None, root_dir=None, base_dir=None, verbose=0,
                    dry_run=0, owner=None, group=None, logger=None)
