#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 下午7:21
# @Author  : Vassago
# @File    : wtfrom.py
# @Software: PyCharm


from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import DataRequired #, Email

class CreateInstanceForm(Form):
    image = StringField(u'Your name', validators=[DataRequired()])
    port = StringField(u'Your favorite password', validators=[DataRequired()])
    volumes = StringField(u'Your email address', validators=[DataRequired()])
    # birthday = DateField(u'Your birthday')
    #
    # a_float = FloatField(u'A floating point number')
    # a_decimal = DecimalField(u'Another floating point number')
    # a_integer = IntegerField(u'An integer')
    #
    # now = DateTimeField(u'Current time',
    #                     description='...for no particular reason')
    # sample_file = FileField(u'Your favorite file')
    # eula = BooleanField(u'I did not read the terms and conditions',
    #                     validators=[Required('You must agree to not agree!')])
    #
    # submit = SubmitField(u'Signup')
