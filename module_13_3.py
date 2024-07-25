from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
api = 'API Key'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
@dp.message_handler(commands=['start'])
async def start_messages(message):
    await bot.send_message(message.from_user.id, 'Привет! Я бот помогающий твоему здоровью')
@dp.message_handler(content_types=["text"])
async def all_massages(message):
    await bot.send_message(message.chat.id, 'Введите команду /start, чтобы начать общение')
executor.start_polling(dp, skip_updates=True)