# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 20:29
# @Author  : double peng
# @FileName: hello.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn


from app.hello_buleprint.buleprint import web


@web.route('/hello/')
def hello():
    return "hello world"
