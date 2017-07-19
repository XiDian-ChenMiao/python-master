# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 应用程序入口文件


from flask import Flask, request, make_response, redirect, abort, render_template, url_for, session, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate, MigrateCommand
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import datetime
import os
from threading import Thread

app = Flask(__name__)


def make_shell_context():
    """
    配置shell命令启动时的回调函数，用于将数据库实例以及模型导入
    :return: 导入到上下文中的实例字典
    """
    return dict(app=app, db=db, User=User, Role=Role)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'daqinzhidi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[陈苗]'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
app.config['FLASKY_MAIL_SENDER'] = '大秦之帝 <daqinzhidi@sina.com>'
app.config['MAIL_SERVER'] = 'smtp.sina.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
# 通过环境变量来设置用户名和密码
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
manager = Manager(app)
# 给管理器的shell命令添加回调函数
manager.add_command('shell', Shell(make_context=make_shell_context))
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app, db)
# 给管理器配置数据库迁移的命令
manager.add_command('db', MigrateCommand)


# 异步发送邮件
def send_aync_email(application, mesg):
    with application.app_context():
        mail.send(mesg)


# 发送邮件函数
def send_email(to, subject, template, **kwargs):
    mesg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    mesg.body = render_template(template + '.txt', **kwargs)
    mesg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_aync_email, args=[app, mesg])
    thr.start()
    return thr


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], '注册新用户', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', name=name, user_agent=user_agent, current_time=datetime.datetime.utcnow())


@app.route('/bad')
def bad_request():
    return '<h1>Bad Request</h1>', 400


@app.route('/response')
def response():
    res = make_response('<h1>Response</h1>')
    res.set_cookie('username', 'daqinzhidi')
    return res


@app.route('/baidu')
def baidu():
    return redirect('http://www.baidu.com')


@app.route('/userid/<userid>')
def user_id(userid):
    idstr = str(userid)
    if idstr.isdigit() and int(userid) >= 0:
        return '<h1>User %d </h1>' % int(userid)
    else:
        abort(404)


@app.errorhandler(404)
def not_found(code):
    return render_template('404.html'), 400


@app.errorhandler(500)
def server_error(code):
    return render_template('500.html'), 500


@app.route('/tmpl/user/<username>')
def tmpl_user(username):
    return render_template('user.html', name=username)


class NameForm(FlaskForm):
    """
    登录表单
    """
    name = StringField('姓名', validators=[Required()])
    submit = SubmitField('提交')


class Role(db.Model):
    """
    角色模型
    """
    __tablename__ = 'roles'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 添加到Role模型中的users属性代表这个关系的面向对象视角。
    # 对于一个Role类的实例，其users属性将返回与角色相关联的用户组成的列表
    # db.relationship()中的backref参数向User模型中添加一个role属性，从而定义反向关系
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    """
    用户模型
    """
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # 角色表的主键为用户表的外键
    role_id = db.Column(db.INTEGER, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    manager.run()
