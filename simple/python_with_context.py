#!/usr/bin/env python
# coding=utf-8

from contextlib import contextmanager

class ContextIllustration(object):

    def __enter__(self):
        print('entering context')

    def __exit__(self, exc_type, exc_value, traceback):
        print('leaving context')
        if exc_type is None:
            print('with no error')
        else:
            print('with an error (%s)' % (exc_value))


@contextmanager
def context_illustration():
    print('entering context')
    try:
        yield
    except Exception as e:
        print('leaving context, with an error (%s)' % e)
        raise
    else:
        print('leaving context, with no error')


if __name__ == '__main__':
    with ContextIllustration():
        print('something')
        # raise RuntimeError('runtime error')
