# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 20:06
# @Author  : double peng
# @FileName: run.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn

from app import create_app

app = create_app() #引入应用级别的app 对象

if __name__ == '__main__':
    app.run(host=app.config['HOST'],debug=app.config['DEBUG'],port=app.config['PORT'])