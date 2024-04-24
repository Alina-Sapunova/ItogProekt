# 5796309424  чат id
import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram.ext import ApplicationBuilder
import sqlite3
from telegram import ReplyKeyboardMarkup

TOKEN = '7197643700:AAGDeHtbql7ZykEzxCIEmLaoBDZAGwdlE-I'

# proxy_url = "socks5://user:pass@host:port"
#
# app = ApplicationBuilder().token(TOKEN).proxy_url(proxy_url).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    reply_keyboard = [['/Да', '/Нет'],
                      ['/site', '/work_time']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
            reply_markup=markup
        )
    # user = update.effective_user
    # await update.message.reply_html(
    #     rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    # )


async def help_command(update, context):
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def photo_command(update, context):
    conn = sqlite3.connnect('bot.db')
    cur = conn.cursor()
    result = cur.execute("SELECT photo FROM party WHERE id = ?", (1,)).fetchone()[0]


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("photo", photo_command))
    application.run_polling()


if __name__ == '__main__':
    main()
