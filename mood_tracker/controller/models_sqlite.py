from django.db import models

# Create your models here.
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from django_sorcery.db import databases
from .utils import get_session

db = databases.get('default')

BASE = declarative_base()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(String(36), primary_key=True)
    temperature = db.Column(Integer)
    safety_score = db.Column(Integer)
    mask_proper = db.Column(Boolean)
    age = db.Column(Integer)
    gender = db.Column(String(36))

    def update(self, values):
        for k, v in values.items():
            setattr(self, k, v)

    def save(self, session=None):
        if not session:
            session = get_session()
        with session.begin(subtransactions=True):
            session.add(self)
            session.flush()
