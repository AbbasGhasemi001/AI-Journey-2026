from aiogram.fsm.state import State, StatesGroup

class SupportStates(StatesGroup):
    waiting_for_support_message = State()