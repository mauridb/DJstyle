# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mongoengine import *

# TODO: create models: project, skill


class User(Document): # TODO: mv to application authentication
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Point(Document):
    lat = FloatField()
    lng = FloatField()
    name = StringField(max_length=50)


class Comment(EmbeddedDocument): # TODO: mv to application blog
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