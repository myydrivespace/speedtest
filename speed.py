"""
Author: Bisnu Ray
Telegram: https://t.me/SmartBisnuBio
"""

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime
import speedtest

bot_token = "Your Bot Token"
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['speedtest'])
async def speedtest_command(message: types.Message):
    loading_msg = await message.reply("<b>Calculating your server's speed...</b>", parse_mode=types.ParseMode.HTML)

    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = datetime.now()
    ms = (end - start).seconds

    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")

    speedtest_result = (
        "<b>Smart-Tool Server Status\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"Download: <code>{convert_from_bytes(download_speed)}</code>\n"
        f"Upload: <code>{convert_from_bytes(upload_speed)}</code>\n"
        f"Ping: <code>{ping_time} ms</code>\n"
        f"Internet Provider: <code>{i_s_p} ({i_s_p_rating})</code></b>"
    )

    await loading_msg.delete()
    await message.reply(speedtest_result, parse_mode=types.ParseMode.HTML)


def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kilobytes/s", 2: "Megabytes/s", 3: "Gigabytes/s", 4: "Terabytes/s"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
