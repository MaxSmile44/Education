import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse


def reply(chat_id, question):
    message_id = bot.send_message(chat_id, "Запускаю таймер")
    message_id_bar = bot.send_message(chat_id, render_progressbar(parse(question), 0))
    bot.create_countdown(parse(question), notify_progress, chat_id=chat_id, message_id=message_id, message_id_bar=message_id_bar, question=question)
    bot.create_timer(parse(question), notify, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, message_id_bar, question):
    bot.update_message(chat_id, message_id, f"Осталось секунд: {secs_left}")
    bot.update_message(chat_id, message_id_bar, render_progressbar(parse(question), parse(question) - secs_left))


def notify(chat_id):
    bot.send_message(chat_id, "Время вышло!")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv("telegram_token")
    bot = ptbot.Bot(tg_token)

    bot.reply_on_message(reply)

    bot.run_bot()