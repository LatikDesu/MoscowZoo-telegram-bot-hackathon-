from aiogram_dialog import DialogRegistry


def register_dialogs(registry: DialogRegistry):
    from . import quiz_dialog, start_dialog

    registry.register(start_dialog.ui)
    registry.register(quiz_dialog.ui)
