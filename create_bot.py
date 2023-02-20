from aiogram import Bot, Dispatcher


from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='6078433743:AAF5ptZFEJtJ99tzlblrfGGp4jfyRXGXD_g', parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())