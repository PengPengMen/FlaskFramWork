# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 20:05
# @Author  : double peng
# @FileName: __init__.py.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn


from flask import Flask
from app.Config import config
from app.instance import security
#from app.hello_buleprint.hello import web  # 导入蓝图对象
from app.hello_buleprint.buleprint import web  # 导入蓝图对象
from app.model.UserModeul import db
# 应用级别的初始化
def create_app():
    app = Flask(__name__,instance_relative_config=True) #新建flask app对象
    app.config.from_object(config) #引用web服务器配置文件
    app.config.from_object(security) #引用数据库配置文件

    db.init_app(app) #初始化数据库db对象
    db.create_all(app=app) #创建model中所有申明的数据库表模型
    register_blueprint(app) #注册蓝图
    return app# 返回flask app 和SQLAlchemy db对象

# 注册蓝图函数
def register_blueprint(app):
    app.register_blueprint(web) #注册蓝图对象




