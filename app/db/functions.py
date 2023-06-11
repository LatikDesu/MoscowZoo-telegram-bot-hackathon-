import random
from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


class User(models.User):
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, telegram_id):
        await User(telegram_id=telegram_id).save()

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()


class Animals(models.Animals):
    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def get_totem_animal(cls, code: int):
        if await cls.filter(code=code):
            try:
                target_animals = await cls.filter(code=code)
                random_choice = random.choice(target_animals)
                return random_choice
            except DoesNotExist:
                return False
        else:
            try:
                target_animals = await cls.all()
                random_choice = random.choice(target_animals)
                return random_choice
            except DoesNotExist:
                return False

    @classmethod
    async def get_random_animal(cls):
        try:
            target_animals = await cls.all()
            random_choice = random.choice(target_animals)
            return random_choice
        except DoesNotExist:
            return False


class Questions(models.Questions):
    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def get_question(cls, tier: int):
        try:
            target_question = await cls.filter(tier=tier)
            random_choice = random.choice(target_question)
            return random_choice
        except DoesNotExist:
            return False

    @classmethod
    async def create_question(cls, tier, question, answers, answers_code):
        await Questions(tier=tier,
                        question=question,
                        answers=answers,
                        answers_code=answers_code).save()


class ResultDescription(models.ResultDescription):
    @classmethod
    async def get_description(cls):
        try:
            description = await cls.all()
            random_choice = random.choice(description)
            return random_choice
        except DoesNotExist:
            return False
