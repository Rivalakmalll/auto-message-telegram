import asyncio
import random
from telethon import TelegramClient
from telethon.errors import FloodWaitError, UsernameNotOccupiedError

api_id = ''
api_hash = ''
phone = ''
group_links = [
    '',
    '',
    '',
    ''
] #put your link group here!!

async def send_messages():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(phone)
        while True:
            for link in group_links:
                try:
                    # Get entity information
                    group_entity = await client.get_entity(link)
                    
                    # Log the name/title of the group
                    if hasattr(group_entity, 'title'):
                        print(f"Sending message to: {group_entity.title}")
                    else:
                        print(f"Sending message to: {link}")
                    
                    # Send message to the group
                    message = "your message here" #input you message here
                    await client.send_message(group_entity, message)
                    await asyncio.sleep(random.uniform(30, 60))  # Randomize delay between messages (30-60 seconds)
                except UsernameNotOccupiedError as e:
                    print(f"Username not found error for {link}: {e}")
                    # Handle username not found error
                except FloodWaitError as e:
                    print(f"Hit FloodWaitError for {link}: {e}")
                    await asyncio.sleep(e.seconds + random.uniform(5, 10))  # Wait for suggested time + additional random time
                except Exception as e:
                    print(f"Error occurred for {link}: {e}")
                    # Handle other exceptions if needed
            await asyncio.sleep(30)  # Cooldown between loops

async def main():
    await send_messages()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
