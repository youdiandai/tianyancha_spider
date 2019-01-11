#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2019/1/10'
"""
import pyExcelerator
import json
import sys

COLUMN = [('name', u'公司名称'), ('created', u'创建时间'), ('financing', u'融资情况'), ('local', u'所在地'), ('desc', u'简介')]


def create_excel(j_name, e_name=None):
    e_name = e_name if e_name else j_name.split('.')[0] + '.xls'
    # 防止名字格式错误
    e_name = e_name.split('.')[0] + '.xls'
    w = pyExcelerator.Workbook()
    ws = w.add_sheet('sheet1')
    with open(j_name, 'rb') as f:
        a = f.read()
    companies = json.loads(a)

    for x in range(len(COLUMN)):
        ws.write(0, x, COLUMN[x][1])

    for x in range(len(companies)):
        for y in range(len(COLUMN)):
            ws.write(x + 1, y, companies[x][COLUMN[y][0]])
    w.save(e_name)


if __name__ == '__main__':
    json_name = sys.argv[1]
    excel_name = sys.argv[2] if len(sys.argv) > 2 else json_name.split('.')[0] + '.xls'
    # 防止名字格式错误
    excel_name = excel_name.split('.')[0] + '.xls'
    print("Start creating an excel file {} from the json file {}".format(excel_name, json_name))
    create_excel(json_name, excel_name)
    print("end")
