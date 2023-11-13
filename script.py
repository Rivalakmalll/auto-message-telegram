import asyncio
from telethon import TelegramClient

api_id = ''
api_hash = ''
phone = ''

async def send_messages():
    async with TelegramClient('session_name', 'your_api', 'your_api_hash') as client:
        await client.start(phone)
        group_entity = await client.get_input_entity('')  #input yout telegram group id you can put it more than 1 
        message = "Your Message Here"

        while True:  # Infinite loop
            await client.send_message(group_entity, message)
            await asyncio.sleep(9)

async def main():
    await send_messages()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())