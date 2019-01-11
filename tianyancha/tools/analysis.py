#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2019/1/11'
"""
import jieba
from collections import Counter


def list_participle(tags):
    return reduce(lambda a, b: a + b, [jieba.lcut(x, cut_all=False) for x in tags])


def count_tag(tags):
    """
    计算tags和desc中，各个词的出现频次
    :param tags:
    :return:
    """
    return Counter(list_participle(tags))


def str_in_tags(tags, *string):
    """
    判断输入的字符串是不是都在tags中出现了
    :param tags:
    :param string:
    :return:
    """
    _p = list_participle(tags)
    for x in string:
        if x not in _p:
            return False
    return True
