#!/usr/bin/env python
# coding=utf-8
import re
import reprlib
import sys


RE_WORD = re.compile('\w+')

class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceYield(object):
    """
    使用yield代替迭代器版本
    """
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'SentenceYield(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


class SentenceIterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    text = sys.argv[1] if len(sys.argv) > 1 else 'XiDian-ChenMiao just do it.'
    s = Sentence(text)
    sy = SentenceYield(text)
    print([word for word in s])
    print([word for word in sy])
