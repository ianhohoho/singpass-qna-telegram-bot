
from telethon import TelegramClient, events, Button

from dotenv import load_dotenv
load_dotenv()
import os

def create_client(bot_name):
    """
    Create a new TelegramClient instance with the specified bot name.

    :param bot_name: The name of the bot.
    :return: A new TelegramClient instance.
    """
    return TelegramClient(
        f'./tmp_sessions/{bot_name}',
        os.getenv('BOT_API_ID'),
        os.getenv('BOT_API_HASH')
    ).start(bot_token=os.getenv('BOT_TOKEN'))