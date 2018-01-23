from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Regexp
from app.models import User
from flask import session

class RegistForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[DataRequired("请输入昵称!")],
        description='昵称',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[DataRequired("请输入邮箱!"),
                    Email("邮箱格式不正确")],
        description='邮箱',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
            # "required":"required",
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[DataRequired("请输入手机号码!"),
                    Regexp("1[3458]\d{9}", message="手机格式不正确")],
        description='手机号码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机号码！",
            # "required":"required",
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[DataRequired("请输入密码！")],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
            # "required": "required",
        }
    )
    repwd = PasswordField(
        label='确认密码',
        validators=[DataRequired("请输入确认密码！"),
                    EqualTo('pwd', message="两次密码不一致")],
        description='确认密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认密码！",
            # "required": "required",
        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )
    def validate_name(self,filed):
        name = filed.data
        user = User.query.filter_by(name=name).count()
        if user==1:
            raise ValidationError("昵称已经存在")

    def validate_email(self,filed):
        email = filed.data
        user = User.query.filter_by(email=email).count()
        if user==1:
            raise ValidationError("邮箱已经存在")

    def validate_phone(self,filed):
        phone = filed.data
        user = User.query.filter_by(phone=phone).count()
        if user==1:
            raise ValidationError("手机号码已经存在")

class LoginForm(FlaskForm):
    name = StringField(
        label="请输入账号",
        validators=[DataRequired("请输入账号!")],
        description='账号',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[DataRequired("请输入密码！")],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登陆',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )

class UserdatailForm(FlaskForm):
    name = StringField(
        label="昵称",
        validators=[DataRequired("请输入昵称!")],
        description='昵称',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[DataRequired("请输入邮箱!"),
                    Email("邮箱格式不正确")],
        description='邮箱',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
            # "required":"required",
        }
    )
    phone = StringField(
        label="手机号码",
        validators=[DataRequired("请输入手机号码!"),
                    Regexp("1[3458]\d{9}", message="手机格式不正确")],
        description='手机号码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机号码！",
            # "required":"required",
        }
    )
    face = FileField(
        label="头像",
        validators = [DataRequired("请上传头像!"),],
        description='头像',
    )
    info = TextAreaField(
        label="简介",
        validators=[DataRequired("请输入简介!")],
        description='简介',
        render_kw={
            "class": "form-control",
            "row":10
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        }
    )

class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[DataRequired("请输入旧密码！")],
        description='旧密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码!",
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[DataRequired("请输入新密码！")],
        description='新密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码!",
        }
    )
    submit = SubmitField(
        '修改密码',
        render_kw={
            "class": "btn btn-success",
        }
    )
    # def validate_old_pwd(self, filed):
    #     pwd = filed.data
    #     name = session["old_pwd"]
    #     user = User.query.filter_by(name=name).first()
    #     if not user.check_pwd(pwd):
    #         raise ValidationError('旧密码错误!')

class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[DataRequired("请输入内容!")],
        description='内容',
        render_kw={
            "id": "input_content"
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )

