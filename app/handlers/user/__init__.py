from aiogram import Router


def get_user_router() -> Router:
    from . import info, pic_of_day, quiz, result_dialog, start, start_dialog

    router = Router()
    router.include_router(start.router)
    router.include_router(start_dialog.router)

    router.include_router(quiz.router)
    router.include_router(result_dialog.router)

    router.include_router(info.router)

    router.include_router(pic_of_day.router)

    return router
