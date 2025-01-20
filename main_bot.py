from src.bot_tools.client import create_client
from telethon import events
from response import get_answer

class SingpassBot:
    def __init__(self):
        self.bot_name = 'singpass_bot'
        self.client = create_client(self.bot_name)  # Initialize client with the bot name

    async def register_handlers(self):

        @self.client.on(events.NewMessage(pattern='/start'))
        async def handle_start(event):
            await event.reply('Hello! I am your friendly Singpass Bot. How can I help you?')
            raise events.StopPropagation

        @self.client.on(events.NewMessage)
        async def handle_new_message(event):

            message_text = event.message.text

            # Process the message text
            response = get_answer(message_text)

            # Send the response
            await event.reply(response)

    async def run(self):
        await self.client.start()
        await self.register_handlers()
        await self.client.run_until_disconnected()