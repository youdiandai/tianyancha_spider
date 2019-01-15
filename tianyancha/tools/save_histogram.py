#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'save histogram png'
__author__ = 'changxin'
__mtime__ = '2019/1/14'
"""
import json
from collections import Counter
from matplotlib import pyplot as plt


def get_companies(json_file=None):
    json_file = json_file if json_file else 'scraped_data.json'
    with open('scraped_data.json', 'rb') as f:
        return json.loads(f.read())


def sorted_data(companies_dict):
    company_list = [x['local'] for x in companies_dict]
    for x in range(len(company_list)):
        if u'/' in company_list[x]:
            company_list[x] = company_list[x].split(u'/')[-1]
    t = list(Counter(company_list).items())
    t.sort(key=lambda x: x[1], reverse=True)
    return t


def show_histogram(data):
    name_list = [x[0] for x in data]
    data_list = [x[1] for x in data]
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.bar(range(len(data_list)), data_list, color='rgb', tick_label=name_list)
    plt.savefig('histogram.png')
    plt.show()


if __name__ == '__main__':
    show_histogram(sorted_data(get_companies()))
