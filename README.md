# lt的第一个项目
## 框架
使用了flask框架和sqlalchemy，wtform，flask_login，flask_migrate和flask_bootstrap等模块
内容主要参考了**Flask Web开发：基于Python的Web应用开发实战第2版**这本书
以及此书在B站上的讲解视频 *视频地址（https://www.bilibili.com/video/BV1vK4y177nP?p=25&vd_source=8214e9c408e413c7326ad075c3894515）* 

## 功能说明
### 前端页面
除了index主页之外都使用了jianjia2模版来渲染页面，页面通过{% extends "bootstrap/base.html" %}来继承bootstrap的base.html，其他页面也用到了jianjia2来标记语句和变量
### 登陆和注册
登陆和注册界面后端功能通过flask_wtform模块来实现，在form.py中创建了RegistForm和loginForm两个表单类来处理收到的表单数据，通过validator函数来对数据进行验证，主要验证密码不为空和密码长度
在注册表单中除了多了一个EqualTo验证之外还自定义了一个validate_username验证器，用来验证用户名是否存在，如果用户名存在就无法注册
### ORM model
在models.py创建了User和Course两个类，除了常规设置属性外，主要有三个亮点：
User类中定义了三个方法来增加安全性，通过werkzeug.security模块实现了将用户输入密码哈希加密，并且在数据库中不存储明文密码，只存储哈希加密过的哈希密码
使用flask_login模块来进行登陆管理，User类继承了UserMixin来实现登陆管理，该部分在router.py中用来认证和授权相关的功能
Course类中定义find_by_course_model来实现通过模块名返回模块课程
### 数据库迁移
通过flask_migrate来实现数据库迁移的功能，使得对数据库模型进行变更和升级变得更加方便和可控。通过使用 Flask_migrate使得数据库结构的升级和降级变得可控和可重复。
 
## 总结
该项目完成了后端部分大部分内容，而且因为使用多种模块和对象类，使得代码很简洁，可维护性高，避免了重复造轮子
但前端设计较为简陋，计划接下来重点改善前端页面

   
