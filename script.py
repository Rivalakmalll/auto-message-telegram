import asyncio
from telethon import TelegramClient

api_id = '24400448'
api_hash = 'aaab42191b59530107d5554736c9e148'
phone = '+6289525229836'

async def send_messages():
    async with TelegramClient('session_name', '24400448', 'aaab42191b59530107d5554736c9e148') as client:
        await client.start(phone)
        group_entity = await client.get_input_entity('@LPM_BBG_MMK_DDK_BBB')
        group_entity = await client.get_input_entity('t.me/LPM_DDK_BBG_BBB_MMK')
        group_entity = await client.get_input_entity('https://t.me/BBG_DDK_RPRL')
        group_entity = await client.get_input_entity('https://t.me/BBG_DDK_RPRL')
        group_entity = await client.get_input_entity('https://t.me/lpm_bbg_ddk')
        message = "Need bbg rprl chat aja sini @onlyskyy2"

        while True:  # Infinite loop
            await client.send_message(group_entity, message)
            await asyncio.sleep(8)

async def main():
    await send_messages()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())