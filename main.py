import aiogram
import re
from create_bot import dp, bot
from aiogram.dispatcher.filters.builtin import CommandStart
import pdfkit
from io import BytesIO
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import create_bdx, add_userx, get_userx, update_money, add_wait, get_money, get_wait, delete_wait, check_for_wait, get_user_balance_and_id
from selenium import webdriver
import datetime
import re
from aiogram.dispatcher.filters import Text
import time
import asyncio
import random
from aiogram.types import ReplyKeyboardMarkup
import time
from bs4 import BeautifulSoup

from aiogram.utils.exceptions import Throttled
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from proxy_auth_data import *

from reportlab.pdfgen import canvas
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pickle

async def anti_flood(*args, **kwargs):
    m = args[0]
    #тут будет то, что нужно при флуде.
    await m.answer("🔸Пожалуйста, не флудите")

# Создание PDF-файла
pdf_file = canvas.Canvas("example.pdf")

options = webdriver.ChromeOptions()
options.binary_location = r"/usr/bin/google-chrome"
chrome_driver_binary = r"/usr/local/bin/chromedriver"

options.add_argument(r"C:\Users\yyurc\AppData\Local\Google\Chrome\User Data")
options.add_argument('--headless')
options.add_argument('--no-sandbox')

browser = webdriver.Chrome(service=Service(chrome_driver_binary), options=options)





browser.get("https://naurok.com.ua/login")

time.sleep(3)

for cookie in pickle.load(open(f"{vk_phone}_cookies", "rb")):
        browser.add_cookie(cookie)

time.sleep(5)
browser.refresh()




 # cookies
pickle.dump(browser.get_cookies(), open(f"{vk_phone}_cookies", "wb"))

import html.entities
from aiogram import types

import os

regex = r'^(https?:\/\/)?(www\.)?naurok\.com\.ua\/.*\.html$'
str = "https://naurok.com.ua"

from selenium.common.exceptions import NoSuchElementException

class History(StatesGroup):
    texts = State()

from aiogram.utils import exceptions

current_url = browser.current_url

print(current_url)

@dp.message_handler(CommandStart(), state="*") # не более 2 сообщений за 10 секунд
@dp.throttled(anti_flood, rate=1)
async def bot_start(message: aiogram.types.Message):
    get_user_id = get_userx(user_id=message.from_user.id)
    if len(get_user_id) == 0:
        add_userx(message.from_user.id, 30)
        await message.answer("🔸<b>ВАМ ВЫДАНО 30 ГРИВЕН</b>")

    await message.answer("<b>🔔 Пополнить баланс</b>\n\n"
                        "🔸Нажимаете в боте кнопочку <b>📱ПРОФИЛЬ</b>\n"
                        "🔸Копируйте свой номер аккаунта\n"
                        "🔸Пересылайте - @kilopok\n"
                        " ", reply_markup=check_user_out_func())
    await message.answer("<b>🔔 Получить ответы </b>\n\n"
                        "🔸Пополняете баланс\n"
                        "🔸Присылаете ссылку\n"
                        "🔸Получаете ответы\n"
                        "🔸Видео: https://youtu.be/LMmXc8gusG8", reply_markup=check_user_out_func())

def check_user_out_func():
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("📱 Профиль")
    menu_default.row("🎁 Пополнить")
    return menu_default

@dp.message_handler(text="📱 Профиль", state="*")
@dp.throttled(anti_flood, rate=1)
async def bot_start(message: types.Message, state: FSMContext):
    get_user_id = get_user_balance_and_id(message.from_user.id)[0]
    if len(get_user_id) != 0:
        await message.answer("<b>📱 Ваш профиль</b>\n\n"
                            f"🔸<b>Номер:</b> <code>{get_user_id[1]}</code> <i>(КОПИРУЕТСЯ)</i>\n"
                            f"🔸<b>Баланс:</b> <code>{get_user_id[2]}</code>\n")
    else:
        await message.answer('🔸Пройдите регистрацию, используя команду /start')

@dp.message_handler(text="🎁 Пополнить", state="*")
@dp.throttled(anti_flood, rate=1)
async def bot_start(message: types.Message, state: FSMContext):
    get_user_id = get_user_balance_and_id(message.from_user.id)[0]
    if len(get_user_id) != 0:
        await message.answer("<b>🎁 Пополнить баланс</b>\n\n"
                        "🔸Нажимаете в боте кнопочку <b>📱ПРОФИЛЬ</b>\n"
                        "🔸Копируйте свой номер аккаунта\n"
                        "🔸Пересылайте - @kilopok\n"
                        f"🔸<b>Баланс:</b> <code>{get_user_id[2]}</code>\n"
                        "🔸Видео: https://youtu.be/LMmXc8gusG8", reply_markup=check_user_out_func())
    else:
        await message.answer('🔸Пройдите регистрацию, используя команду /start')

@dp.message_handler(Command("add"))
async def my_command_handler(message: types.Message):
    if message.chat.id ==5367742577:
        match = re.match(r"/add (\d{4,}) (\d{1,4})", message.text)
        if match:
            first_number = int(match.group(1))
            second_number = int(match.group(2))
            if second_number > 9999:
                await message.answer("ЧЕЛ ТЫ ЧЁ ДОЛБАЁБ ТЫ ТИПУ НАХУЙ ЩА ДААШ  10000 ГРИВЕН УЕББАН ОСТАНОВИСЬ")
            else:
                money_current = get_money(first_number)[0][0]
                all_money = int(money_current) + int(second_number)
                update_money(first_number, all_money)
                await bot.send_message(chat_id=first_number, text="🔸Поздравляем! \n"
                                     f"🔸Начислено: <code>{second_number}</code>\n"
                                     f"🔸Баланс: <code>{all_money}</code>")
                pass
        else:
            await message.answer("Invalid command format!")

@dp.message_handler(Command("del"))
async def my_command_handler(message: types.Message):
    if message.chat.id ==5367742577:
        match = re.match(r"/del (\d{4,}) (\d{1,4})", message.text)
        if match:
            first_number = int(match.group(1))
            second_number = int(match.group(2))
            if second_number > 9999:
                await message.answer("Second number is too large!")
            else:
                money_current = get_money(first_number)[0][0]
                all_money = int(money_current) - int(second_number)
                update_money(first_number, all_money)
                pass
        else:
            await message.answer("Invalid command format!")

@dp.message_handler(Text(contains="https"))
@dp.throttled(anti_flood, rate=1)
async def bot_start(message: aiogram.types.Message, state: FSMContext):
    wait_info = get_wait(message.from_user.id)
    if len(wait_info) == 0:
        get_user_id = get_userx(user_id=message.from_user.id)[0]
        if len(get_user_id) != 0:
            if re.search(regex, message.text):
                del_msg = await message.answer("🔸Ссылка принята")
                if not get_user_id[0] < 20:
                    money_finish = int(get_user_id[0]) - 20
                    status_money = update_money(message.from_user.id, money_finish)
                    if status_money == True:
                        link = re.sub(r'\.html$', '', message.text) + '/set'
                        wait_succes = add_wait(datetime.datetime.now(), message.from_user.id, link)
                        await message.answer(f'🔸Вы успешно записались в очередь\nВаше место: <b>{wait_succes[0][0]}</b>')

                        if wait_succes[0][0] == 1:
                            await get_syte(message.from_user.id, link)
                        else:
                            await message.answer(f'🔸Ожидайте')
                    else:
                        await message.answer("🔸Проблема с оплатой. Обратитесь в техническую поддержку")
                else:
                    await message.answer("🔸Пожалуйста, пополните баланс. Требуется 20 гривен за один тест")
            else:
                await message.answer("🔸Строка не является ссылкой требуемого формата \n Пример: naurok.com.ua/test/matematichna-logika-2031033.html")

        else:
                await message.answer('🔸Пройдите регистрацию, используя команду /start')
    else:
        await message.answer('🔸Вы уже записались в очередь.')

async def check_wait_user():
    #await asyncio.sleep(5)
    wait_all = check_for_wait()
    print(wait_all)
    if len(wait_all) != 0:
        await get_syte(wait_all[0][1], wait_all[0][2])
    else:
        print('zakonchili')

async def get_syte(id_user, link):
    try:
        try:
            await bot.send_message(chat_id=id_user, text='🔸 Начал работу по вашему запросу')

            browser.get(link)
            await asyncio.sleep(5)
            wright_answer = browser.find_element(by=By.ID, value="homework-show_answer")
            wright_answer.click()
            await asyncio.sleep(2)
            option_element = browser.find_element(by=By.CSS_SELECTOR, value='option[value="2023-03-17"]')
            option_element.click()
            #await asyncio.sleep(5)
            button = browser.find_element(By.CLASS_NAME, "btn-orange")
            button.click()
            await asyncio.sleep(2)
            current_url = browser.current_url
            if 'https://naurok.com.ua/test/homework/' in current_url:
                text = browser.page_source
                sentences_list = re.findall(r'value="(.*?)"', text)
                print(sentences_list[1])
                link=sentences_list[1]
                browser.get(link)
                name_answer = browser.find_element(by=By.ID, value="joinform-name")
                name_answer.send_keys("Олег Тинькоф")
                button = browser.find_element(By.CLASS_NAME, "btn-orange")
                button.click()
                await asyncio.sleep(3)
                test_quition = browser.find_element(By.CLASS_NAME, 'test-option')
                test_quition.click()
                end = browser.find_element(by=By.CLASS_NAME, value="endSessionButton")
                end.click()
                await asyncio.sleep(5)
                random_number = random.randint(1, 100000000)
                html = browser.page_source
                soup = BeautifulSoup(html, "html.parser")
                questions = soup.find_all("div", class_="homework-stat-question-line")
                output_string = ""
                for question in questions:
                    question_text = question.find("p").text.strip()
                    answer = question.find("span", class_=["correct quiz", "incorect quiz"])
                    if answer is not None:
                        answer_value = answer.text.strip()
                        answer_text = answer.find_next("p").text.strip()
                    else:
                        correct_options = question.find_all("div", class_="homework-stat-option-value correct")
                        if correct_options:
                            answer_values = []
                            answer_texts = []
                            for option in correct_options:
                                answer_values.append(option.find("span").text.strip())
                                answer_texts.append(option.find("p").text.strip())
                            answer_value = answer_values
                            answer_text = answer_texts
                        else:
                            answer_value = "не выбран"
                            answer_text = "ответ не выбран"

                    output_string += f"<b>{question_text}</b>\n"
                    if isinstance(answer_value, list):
                        for i, value in enumerate(answer_value):
                            output_string += f"🔸<b>Ответ {i+1}:</b> <code>{answer_text[i]}</code>\n"
                    else:
                        output_string += f"🔸<b>Ответ:</b> <code>{answer_text}</code>\n"
                    output_string += "-----\n"


                if len(output_string) < 3000:
                    await bot.send_message(id_user, output_string)
                else:
                    html_string = ""
                    for question in questions:
                        question_text = question.find("p").text.strip()
                        answer = question.find("span", class_=["correct quiz", "incorect quiz"])
                        if answer is not None:
                            answer_value = answer.text.strip()
                            answer_text = answer.find_next("p").text.strip()
                        else:
                            answer_value = "не выбран"
                            answer_text = "ответ не выбран"

                        html_string += f"{question_text}\n"
                        html_string += f"🔸Ответ: {answer_text}\n"
                        html_string += f"-----\n"

                    await send_txt_file(html_string, id_user)
                delete_wait(id_user)
                await check_wait_user()
            else:
                await return_cash(id_user)
        except NoSuchElementException as e:
            print(e)
            await return_cash(id_user)
    except BaseException as e:
        print(e)
        await return_cash(id_user)

async def return_cash(id_user):
    delete_wait(id_user)
    get_user_id = get_userx(user_id=id_user)[0]
    if len(get_user_id) != 0:
        if not get_user_id[0] < 0:
            money_finish = int(get_user_id[0]) + 20
            update_money(id_user, money_finish)
            await bot.send_message(chat_id=id_user, text='🔸 Произошёл сбой в системе взлома\n🔸Пожалуйста, попробуйте ещё раз\n🔸<b>Деньги возвращены</b>')
    wait_all = check_for_wait()
    if len(wait_all) != 0:
        await get_syte(wait_all[0][1], wait_all[0][2])
    else:
        print('zakonchili')


def rate_limit(limit: int, key=None):
    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator


async def send_txt_file(text: str, chat_id: int):
    bio = BytesIO(text.encode('utf-8'))
    bio.seek(0)
    file = types.InputFile(bio, filename='file.txt') # создаем объект Document для отправки файла в чат
    await bot.send_document(chat_id, file)

if __name__ == "__main__":
    create_bdx()
    aiogram.executor.start_polling(dp, skip_updates=True)
