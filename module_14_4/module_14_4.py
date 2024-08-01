from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *
api = 'API Key'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
prime_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True)
buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product5', callback_data='product_buying')],
    ]
)
evaluate_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
         InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')]
    ]
)
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    images = [
        'C:\\Users\Алексей\PycharmProjects\pythonProjectModule14\module_14_3\Omega_D3.webp',
        'C:\\Users\Алексей\PycharmProjects\pythonProjectModule14\module_14_3\Collagen.webp',
        'C:\\Users\Алексей\PycharmProjects\pythonProjectModule14\module_14_3\Biotin.webp',
        'C:\\Users\Алексей\PycharmProjects\pythonProjectModule14\module_14_3\Vitamin_K2.webp',
        'C:\\Users\Алексей\PycharmProjects\pythonProjectModule14\module_14_3\Multivit.webp',
    ]
    items = get_all_product()
    for i, k in enumerate(images):
        with open(k, 'rb') as img:
            await message.answer(f'Название: {items[0][i][-1]} | Описание: {items[1][i][-1]} | Цена: {items[2][i][-1]}$')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью', reply_markup=prime_menu)
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=evaluate_menu)
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) + 5')
    await call.answer()
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    res = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {res}')
    await state.finish()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)