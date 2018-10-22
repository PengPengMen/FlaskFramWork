# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 21:51
# @Author  : menpengpeng
# @FileName: UserModeul.py
# @Software: PyCharm
# @email   ：menpp@cityfun.com.cn

from app.model import  db

class UserModule(db.Model):
    __tablename__ = 'userInfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))

    def __repr__(self):
        return '<title %r>' % self.title