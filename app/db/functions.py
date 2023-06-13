import random
from typing import Union

from tortoise.exceptions import DoesNotExist
from tortoise.expressions import Q
from tortoise.functions import Count

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

    @classmethod
    async def get_totem_count(cls) -> int:
        count = await User.annotate(count=Count('totem', _filter=~Q(totem=''))).values_list("count", flat=True)
        return count[0]

    @classmethod
    async def get_contact_count(cls) -> int:
        count = await User.annotate(count=Count('is_contact', _filter=~Q(is_contact=False))).values_list("count",
                                                                                                         flat=True)
        return count[0]

    @classmethod
    async def user_complete_quiz(cls, telegram_id: int, totem_name: str):
        try:
            await User.filter(telegram_id=telegram_id).update(totem=totem_name)
        except DoesNotExist:
            return False

    @classmethod
    async def user_wants_contact(cls, telegram_id: int, username: str):
        try:
            await User.filter(telegram_id=telegram_id).update(contact=username, is_contact=True)
        except DoesNotExist:
            return False

    @classmethod
    async def user_requests(cls) -> str:
        user_request_list = []

        request_list = await User.filter(is_contact=True).values("telegram_id", "contact", "totem")

        for request in request_list:
            user_request_list.append(
                f'<b> id пользователя: </b> {request.get("telegram_id")}\n'
                f'<b> Имя пользователя: </b> {request.get("contact")}\n'
                f'<b> Тотемное животное: </b> {request.get("totem")}'
            )

        return f"\n{'_' * 32}\n".join(map(str, user_request_list))


class Animals(models.Animals):

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


class ResultDescription(models.ResultDescription):
    @classmethod
    async def get_description(cls):
        try:
            description = await cls.all()
            random_choice = random.choice(description)
            return random_choice
        except DoesNotExist:
            return False
