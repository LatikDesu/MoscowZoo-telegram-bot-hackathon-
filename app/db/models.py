from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    totem = fields.CharField(max_length=100, null=True)
    contact = fields.CharField(max_length=100, null=True)
    is_contact = fields.BooleanField(default=False)


class Animals(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=100)
    url = fields.CharField(max_length=100)
    image = fields.CharField(max_length=100)
    code = fields.IntField()


class Questions(Model):
    id = fields.BigIntField(pk=True)
    tier = fields.IntField()
    question = fields.TextField()
    answers = fields.TextField()
    answers_code = fields.CharField(max_length=10)


class ResultDescription(Model):
    id = fields.BigIntField(pk=True)
    description = fields.TextField()
    code = fields.IntField(null=True)
