import ctypes
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
lib = ctypes.cdll.LoadLibrary(os.path.join(dir_path, 'gcache.so'))


gget = lib.cache_get
gget.restype = ctypes.c_char_p
gget.argtypes = [ctypes.c_char_p]


def get(key):
    return gget(ctypes.c_char_p(key.encode('utf8')))


gset = lib.cache_set
gset.restype = ctypes.c_char_p
gset.argtypes = [ctypes.c_char_p, ctypes.c_char_p]


def set(key, value):
    if not isinstance(value, bytes):
        value = value.encode('utf-8')

    return gset(
        ctypes.c_char_p(key.encode('utf8')),
        ctypes.c_char_p(value))


gsetup = lib.setup
gsetup.argtypes = [ctypes.c_char_p]


def setup(addr):
    gsetup(ctypes.c_char_p(addr.encode('utf8')))
