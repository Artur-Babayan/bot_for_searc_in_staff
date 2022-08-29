from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import requests


bot = Bot("5444821336:AAEM0BYnmmMkzlWS-1F3YthFAM_qeu0t8H0")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id,
     """Բարև, ես քո <b>Telegram Bot</b> եմ,կոգնեմ գտնես քո ուզած աշխատանքը <b> <a href="https://staff.am/am">Staff</a></b> կայքում։ Ներքևի դաշտում մուտքագրիր քո ուզած աշխատանքի անվանումը։ """, 
     parse_mode="html", disable_web_page_preview=0)


@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = "https://staff.am/am/jobs?JobsFilter%5Bcompany%5D=&JobsFilter%5Bkey_word%5D=" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    all_links = soup.find_all("a", class_="history_block_style history_block_padding")
    for link in all_links:
        url = "https://staff.am" + link["href"]
        await bot.send_message(message.chat.id, url, parse_mode="html")

if __name__ == '__main__':
    executor.start_polling(dp)