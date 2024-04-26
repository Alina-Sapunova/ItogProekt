# 5796309424  чат id
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram.ext import ApplicationBuilder
import sqlite3
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7197643700:AAGDeHtbql7ZykEzxCIEmLaoBDZAGwdlE-I'

# proxy_url = "socks5://user:pass@host:port"
#
# app = ApplicationBuilder().token(TOKEN).proxy_url(proxy_url).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    reply_keyboard = [['Начнём!', 'Нет']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Привет, я SurpriseBot, помогу с выбором подарка на праздник! Начнём? ",
        reply_markup=markup
    )

    # user = update.effective_user
    # await update.message.reply_html(
    #     rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    # )


async def inline(update, context):
    await update.message.reply_text(
        'Полезные ссылки',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Открытки',
                                  url='https://yandex.ru/images/search?from=tabbar&text=%D0%BF%D0%BE%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BA')],
            [InlineKeyboardButton(text='Поздавления', url='https://pozdravok.com/pozdravleniya/den-rozhdeniya/')],
        ])
    )


# async def go_command(update, context):
#     if 'Начать' in update.message.text:
#         await update.message.reply_text("Выберите праздник на который нужен подарок")


# async def party(update, context):
#     reply_keyboard = [['Начнём!', 'Нет']]
#     markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
#     await update.message.reply_text(
#         "Привет, я SurpriseBot, помогу с выбором подарка на праздник! Начнём? ",
#         reply_markup=markup
#     )


async def help_command(update, context):
    await update.message.reply_text("fgfg")


async def photo_command(update, context):
    chat_id = update.message.chat.id
    await context.bot.send_photo(chat_id=chat_id, photo='C:\ItogProekt\img\др.jpg', caption="Как Вам этот вариант?")


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("photo", photo_command))
    application.add_handler(CommandHandler("inline", inline))
    application.add_handler(CommandHandler("Начать", go_command))
    application.run_polling()


if __name__ == '__main__':
    main()
