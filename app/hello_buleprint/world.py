# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 21:36
# @Author  : double peng
# @FileName: world.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn

from app.hello_buleprint.buleprint import web

@web.route('/world/')
def world():
    return "menpengpeng"