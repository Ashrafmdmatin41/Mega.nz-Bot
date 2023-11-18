# @Author: https://github.com/Itz-fork
# @Project: https://github.com/Itz-fork/Mega.nz-Bot
# @Version: nightly-0.2
# @Description: Contains all the commands of the bot


from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start"))
async def start_msg(_: Client, msg: Message):
    await msg.reply_text(
        f"""
    Hi `{msg.from_user.first_name}`, this is your personal Mega.nz bot!
    """
    )
