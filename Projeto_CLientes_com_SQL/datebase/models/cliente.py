from peewee import Model, CharField, DateTimeField
from datebase.datebase import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db