import asyncio
import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
SOURCE_CHANNEL_ID = 0
TARGET_CHANNEL_ID = 0

client = TelegramClient("my", API_ID, API_HASH)


async def list_dialogs():
    """use this for lookup your dialogs"""
    print("List All Dialogs Below.")
    async for dialog in client.iter_dialogs():
        print("{:>14}: {}".format(dialog.id, dialog.title))


async def main():
    me = await client.get_me()
    print(f"Login as {me.username}.")

    print("Start Listening Messages...")

    @client.on(events.NewMessage(incoming=True))
    async def forward_message(event):
        if event.chat_id == SOURCE_CHANNEL_ID:
            await client.forward_messages(TARGET_CHANNEL_ID, event.message)
            print(event.message)

    while client.is_connected():  # <- new
        await asyncio.sleep(10)


with client:
    client.loop.run_until_complete(main())
