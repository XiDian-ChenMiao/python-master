# coding=utf-8

from __future__ import absolute_import, unicode_literals
import os, re
import shutil


class Path:
    '''
    关于路径操作的封装
    '''
    _LINUX_ROOT = '/'
    _LINUX_PATH_SEPARATOR = '/'

    def __init__(self, pathstr: str):
        self._pathstr = pathstr
        self._abspath = os.path.abspath(pathstr)

    def get_parent(self):
        return Path(os.path.dirname(self._abspath))

    def get_childs(self):
        if self.is_file():
            return
        return [Path(c) for c in os.listdir(self._abspath)]

    def is_absolute(self):
        return os.path.isabs(self._pathstr)

    def is_dir(self):
        return os.path.isdir(self._abspath)

    def is_file(self):
        return os.path.isfile(self._abspath)

    def join(self, s):
        return Path(os.path.join(self._abspath, s))

    def get_basename(self):
        return os.path.basename(self._abspath)

    def get_extension(self):
        return os.path.splitext(self._abspath)[1]

    def get_filename(self):
        return os.path.split(self._abspath)[1]

    def is_exists(self):
        return os.path.exists(self._abspath)

    def ends_with(self, ext):
        return self._abspath.endswith(ext)

    def touch(self):
        if self.is_exists():
            return True
        open(self._abspath, mode='r', encoding='utf-8').close()
        return True

    def mkdir(self):
        if self.is_exists():
            return
        os.makedirs(self._abspath)
        return True

    def rm(self):
        if not self.is_exists():
            return
        if self.is_file():
            os.remove(self._abspath)
        if self.is_dir():
            shutil.rmtree(self._abspath)

    def mv(self, dest):
        shutil.move(self._abspath, dest)

    def cp(self, dest):
        if self.is_file():
            shutil.copyfile(self._abspath, dest)
        if self.is_dir():
            shutil.copytree(self._abspath, dest)

    @classmethod
    def is_two_linux_path_contains(cls, path_a, path_b):
        if path_a == cls._LINUX_ROOT or path_b == cls._LINUX_ROOT:
            return True
        path_a_split = path_a.split(cls._LINUX_PATH_SEPARATOR)
        path_b_split = path_b.split(cls._LINUX_PATH_SEPARATOR)
        for item_1, item_2 in zip(path_a_split, path_b_split):
            if item_1 != item_2:
                return False
        return True

    def is_valid_linux_path(self):
        if not self._pathstr:
            return False
        LINUX_PATH_REGEX = r'^(/[^/ ]*)+/?$'
        return self.is_valid_pattern(LINUX_PATH_REGEX)

    def is_valid_pattern(self, regex):
        REGEX = re.compile(regex, re.UNICODE)
        m = REGEX.match(self._abspath)
        return True if m else False

    def is_valid_windows_path(self):
        WINDOWS_PATH_REGEX = r'^[a-zA-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$'
        return self.is_valid_pattern(WINDOWS_PATH_REGEX)

    def is_valid_path(self):
        return self.is_valid_windows_path() or self.is_valid_linux_path()


class File(object):
    '''
    关于文件操作的方法封装
    '''
    def __init__(self, filestr: str):
        if not os.path.isfile(filestr):
            raise ValueError('must be a real file, now is %s' % filestr)
        self._filestr = os.path.abspath(filestr)
        self._statresult = os.stat(self._filestr)

    def get_size(self):
        return self._statresult.st_size

    def get_create_time(self):
        return self._statresult.st_ctime


if __name__ == '__main__':
    f = File('/home/daqinzhidi/programs/python-master/util/path.py')
    p = Path('/home/daqinzhidi/programs/python-master/util/path.py')
    print('file size:', f.get_size())
    print('create time:', f.get_create_time())
    print('get_parent:', p.get_parent())
    print('get_childs:', p.get_childs())
    print('is_absolute:', p.is_absolute())
    print('is_dir:', p.is_dir())
    print('is_file:', p.is_file())
    print('get_basename:', p.get_basename())
    print('get_extension:', p.get_extension())
    print('get_filename:', p.get_filename())
    print('is_exists', p.is_exists())
    print('ends_with:', p.ends_with('.py'))
    print('is_two_linux_path_contains:', Path.is_two_linux_path_contains('/home/daqinzhidi', '/home/daqinzhidi/programs'))
    print('is_valid_linux_path:', p.is_valid_linux_path())
    print('is_valid_windows_path:', p.is_valid_windows_path())
