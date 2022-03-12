from queue import Queue
from telegram.bot import Bot
from telegram.ext import Dispatcher, Defaults, MessageHandler, Filters
from threading import Thread

from bot.config import TOKEN, DUDIN_ID, TYSOVKA_ID, VIDEONOTESCHANNEL_ID


def forward_video_note(update, context):
    bot = context.bot
    chat = update.effective_chat
    chat_id = chat['id']
    user = update.effective_user
    user_id = user['id']
    message = update.effective_message
    message_id = message['message_id']
    if user_id == DUDIN_ID and chat_id == TYSOVKA_ID:
        bot.forward_message(chat_id=VIDEONOTESCHANNEL_ID, from_chat_id=TYSOVKA_ID, message_id=message_id)


bot = Bot(TOKEN)
update_queue = Queue()

dispatcher = Dispatcher(bot=bot, update_queue=update_queue)

dispatcher.add_handler(MessageHandler(Filters.video_note, forward_video_note))

thread = Thread(target=dispatcher.start, name='dispatcher')
thread.start()
