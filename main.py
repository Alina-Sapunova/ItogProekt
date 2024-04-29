import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
import sqlite3
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7197643700:AAGDeHtbql7ZykEzxCIEmLaoBDZAGwdlE-I"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    reply_keyboard = [['/Go', '/No']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Привет, я SurpriseBot, помогу с выбором подарка на праздник! Начнём?",
        reply_markup=markup
    )


async def inline(update, context):
    await update.message.reply_text(
        "Полезные ссылки",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Открытки",
                                  url='https://yandex.ru/images/search?from=tabbar&text=%D0%BF%D0%BE%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BA')],
            [InlineKeyboardButton(text='Поздавления', url='https://pozdravok.com/pozdravleniya/den-rozhdeniya/')],
        ])
    )


async def go_command(update, context):
    if 'Go' in update.message.text:
        reply_keyboard = [["/8march ", "/9may"],
                          ["/23february", "/new_year"],
                          ["/birthday", "/easter"]]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
        await update.message.reply_text(
            """Выберите праздник на который нужен подарок:
            /8march - 8 марта
            /9may - 9 мая
            /23february - 23 Февраля
            /new_year - Новый год
            /birthday - День рождения
            /easter - Пасха""",
            reply_markup=markup
        )


async def help_command(update, context):
    await update.message.reply_text(
        """Команды для общения с SurpriseBot:
        /start - запуск бота
        /help - помощь
        /inline - полезные ссылки
        /Go - начать общение с ботом
        /No - прекратить общение
        /8march - 8 марта
        /9may - 9 мая
        /23february - 23 Февраля
        /new_year - Новый год
        /birthday - День рождения
        /easter - Пасха
        /cancel - сброс команд""")


async def photo_eighth_march(update, context):
    if '8march' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\march.jpg")


async def photo_nine_may(update, context):
    if '9may' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\may.jpg")


async def photo_february(update, context):
    if '23february' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\photo.jpeg")


async def photo_birthday(update, context):
    if 'birthday' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\dr.jpg")


async def photo_new_year(update, context):
    if 'new_year' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\year.jpg")


async def photo_easter(update, context):
    if 'easter' in update.message.text:
        chat_id = update.message.chat.id
        await context.bot.send_photo(chat_id=chat_id, photo="C:\ItogProekt\img\easter.jpg")


async def check(update, context):
    sp = ['/start', '/help', '/inline', '/Go', '/8march', '/9may',
          '/23february', '/new_year', '/birthday', '/easter', '/No']
    if update.message.text not in sp:
        await update.message.reply_text("Команда не понятна, попробуй ещё")


async def no_command(update, context):
    await update.message.reply_text("Пока-пока")


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("inline", inline))
    application.add_handler(CommandHandler("Go", go_command))
    application.add_handler(CommandHandler("8march", photo_eighth_march))
    application.add_handler(CommandHandler("9may", photo_nine_may))
    application.add_handler(CommandHandler("23february", photo_february))
    application.add_handler(CommandHandler("new_year", photo_new_year))
    application.add_handler(CommandHandler("birthday", photo_birthday))
    application.add_handler(CommandHandler("easter", photo_easter))
    application.add_handler(CommandHandler("No", no_command))
    application.run_polling()


if __name__ == '__main__':
    main()
