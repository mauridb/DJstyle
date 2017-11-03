# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
from authC.models import User


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()




