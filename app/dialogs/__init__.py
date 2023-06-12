from aiogram_dialog import DialogRegistry


def register_dialogs(registry: DialogRegistry):
    from . import quiz_dialog

    registry.register(quiz_dialog.ui)
