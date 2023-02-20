import sqlite3
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# create a connection to the SQLite database
conn = sqlite3.connect('user_queue.db')
cur = conn.cursor()

# create a table to store user information
cur.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, queue_position INTEGER, balance INTEGER)')

# create the bot and dispatcher objects
bot = Bot('6078433743:AAF5ptZFEJtJ99tzlblrfGGp4jfyRXGXD_g')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# define the states for the conversation
class QueueStates(StatesGroup):
    in_queue = State()
    not_in_queue = State()
    

# define the handler for when a user requests to join the queue
@dp.message_handler(commands=['join'])
async def join_queue(message: types.Message, state: FSMContext):
    # get the user's ID
    user_id = message.from_user.id
    
    # check if the user has enough balance to join the queue
    cur.execute('SELECT balance FROM users WHERE user_id=?', (user_id,))
    row = cur.fetchone()
    if not row or row[0] < 20:
        await message.reply("You do not have enough balance to join the queue.")
        return
    
    # withdraw 20 points from the user's balance
    cur.execute('UPDATE users SET balance=balance-20 WHERE user_id=?', (user_id,))
    conn.commit()
    
    # add the user to the queue
    cur.execute('SELECT COUNT(*) FROM users')
    row = cur.fetchone()
    queue_position = row[0] + 1
    cur.execute('INSERT INTO users (user_id, queue_position, balance) VALUES (?, ?, ?)', (user_id, queue_position, row[0]))
    conn.commit()
    
    # set the user's state to "in_queue"
    await state.set_state(QueueStates.in_queue)
    
    # notify the user that they have been added to the queue
    await message.reply("You have been added to the queue. Your position is {0}.".format(queue_position))
    
# define the handler for when a user checks their position in the queue
@dp.message_handler(commands=['queue'])
async def check_queue(message: types.Message, state: FSMContext):
    # get the user's ID
    user_id = message.from_user.id
    
    # check if the user is in the queue
    cur.execute('SELECT queue_position FROM users WHERE user_id=?', (user_id,))
    row = cur.fetchone()
    if not row:
        await message.reply("Вы не в очереди")
        await state.set_state(QueueStates.not_in_queue)
        return
    
    # get the user's queue position
    queue_position = row[0]
    
    # notify the user of their queue position
    await message.reply("Your position in the queue is {0}.".format(queue_position))
    
# define the handler for when a user's turn in the queue comes up
@dp.message_handler(commands=['answer'], state=QueueStates.in_queue)
async def answer_user(message: types.Message, state: FSMContext):
    # get the user's ID
    user_id = message.from_user.id
    
    # get the user's queue position
    cur.execute('SELECT queue_position FROM users WHERE user_id=?', (user_id,))
    row = cur.fetchone()
    queue_position = row[0]
    
    # check if the user is next in the queue
    cur.execute('SELECT user_id FROM users WHERE queue_position=?', (queue_position,))
    row = cur.fetchone()
    if row[0] != user_id:
        await message.reply("It is not your turn yet.")
        return

    # remove the user from the queue
    cur.execute('DELETE FROM users WHERE user_id=?', (user_id,))
    conn.commit()

    # set the user's state to "not_in_queue"
    await state.set_state(QueueStates.not_in_queue)

    # send the user their answer
    answer = "Your answer is: ..."
    await bot.send_message(chat_id=user_id, text=answer, parse_mode=ParseMode.HTML)

    # notify the next user in the queue
    cur.execute('SELECT user_id FROM users WHERE queue_position=1')
    row = cur.fetchone()
    if row:
        next_user_id = row[0]
        await bot.send_message(chat_id=next_user_id, text="It is now your turn in the queue.")

    # close the database connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)