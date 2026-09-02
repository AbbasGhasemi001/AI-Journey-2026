from aiogram.fsm.state import State, StatesGroup


class OrderStates(StatesGroup):
    waiting_for_order_details = State()
    waiting_for_confirmation = State()

