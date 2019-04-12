from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import CantParseEntities
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.telegram'))
from os import getenv
from itertools import count
import fire
import uvloop
import asyncio_redis

uvloop.install()

REDIS_HOST = getenv('REDIS_URL', 'localhost')
channel_id = getenv('CHANNEL_ID')

async def push_update(content, bot):
    try:
        return await bot.send_message(
            channel_id, content, parse_mode='Markdown')
    except CantParseEntities:
        return await bot.send_message(channel_id, content)

async def subscribe_and_listen(bot, channel_name='processed'):
    conn = await asyncio_redis.Connection.create(REDIS_HOST)
    pubsub = await conn.start_subscribe()
    await pubsub.subscribe([channel_name])
    for i in count():
        msg = await pubsub.next_published()
        await push_update(msg.value, bot)

def main():
    fire.Fire(TelegramPublisher)

class TelegramPublisher:
    def publish(self, channel_name='processed'):
        try:
            loop = uvloop.new_event_loop()
            bot = Bot(token=getenv('TELGRAM_BOT_API'), loop=loop)
            task = loop.create_task(subscribe_and_listen(bot, channel_name))
            loop.run_until_complete(task)
        except KeyboardInterrupt as e:
            print("Caught keyboard interrupt. Canceling tasks...")
            task.cancel()
        finally:
            loop.run_until_complete(bot.close())
            loop.close()


if __name__ == "__main__":
    main()
