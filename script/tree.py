#!/usr/bin/env python
# coding=utf-8
import os
import argparse
import sys

def show_dir_tree(file_dir, ignore_file_name=''):
    """
    display a directory like 'tree' command
    :param file_dir: need to display this directory
    :param ignore_file_name: ignore some files joined by ','
    """
    if file_dir is None or isinstance(file_dir, str) is False:
        return
    if os.path.exists(os.path.abspath(file_dir)) is False:
        print('path not exists.')
        return
    abs_path = os.path.abspath(file_dir)
    if ignore_file_name is '':
        ignore_file_names = None
    else:
        ignore_file_names = ignore_file_name.split(',')
    tree_info = dict(directories=0, files=0)
    treeize(abs_path, 0, tree_info, ignore_file_names=ignore_file_names)
    print('\n{directories} directories, {files} files'.format(directories=tree_info['directories'], files=tree_info['files']))

def treeize(dir_abs_path, suffix_separator_cnt, tree_info, suffix='|    ', ignore_file_names=None):
    """
    treeize a directory
    :param dir_abs_path: absolute path of a directory
    :param suffix_separator_cnt: the number of suffix string
    :param suffix: the suffix string
    :param ignore_file_names: file names list which need to ignore
    """
    if not os.path.exists(dir_abs_path):
        return
    basename = os.path.basename(dir_abs_path)
    if ignore_file_names is not None:
        if basename in ignore_file_names:
            return
    print(suffix * suffix_separator_cnt + '|--- ' + basename)
    if os.path.isfile(dir_abs_path):
        tree_info['files'] += 1
        return
    tree_info['directories'] += 1
    for f in os.listdir(dir_abs_path):
        treeize(os.path.join(dir_abs_path, f), suffix_separator_cnt + 1, tree_info, suffix, ignore_file_names)

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='treeize a directory', usage='need a absolute path about directory')
    p.add_argument('path', help='a directory path to treeize', type=str)
    p.add_argument('-I', default='', dest='ignore', help='some file names which you want to ignore', type=str)
    args = p.parse_args()
    show_dir_tree(args.path, ignore_file_name=args.ignore)
