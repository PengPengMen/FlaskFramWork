# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 21:46
# @Author  : double peng
# @FileName: buleprint.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn

#  抽取出单蓝图的对象

from flask import Blueprint

web = Blueprint('web',__name__) # 声明web为蓝图对象