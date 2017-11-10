# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import *


class Project(EmbeddedDocument):
    name = StringField()


class Skill(EmbeddedDocument):
    name = StringField()


class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email = StringField(required=True)
    password = StringField()
    role = StringField(max_length=50)
    projects = ListField(EmbeddedDocumentField(Project))
    skills = ListField(EmbeddedDocumentField(Skill))
    meta = {'allow_inheritance': True}
