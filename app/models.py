# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from . import db


#   用户角色表roles
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


#   用户表TUserInfo
class User(db.Model):
    __tablename__ = 'TUserInfo'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user_name = db.Column(db.String(64), unique=True, index=True)
    login_time = db.Column(db.DateTime)
    register_time = db.Column(db.DateTime)
    pwd = db.Column(db.String(32))

    def __repr__(self):
        return '<User %r>' % self.username


#   注册码表TRegisterCode
class RegisterCode(db.Model):
    __tablename__ = 'TRegisterCode'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True)
    valid_flag = db.Column(db.Integer)
    expired_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.username
