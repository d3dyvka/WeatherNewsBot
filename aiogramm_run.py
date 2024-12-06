import asyncio
from create_bot import bot, dp
from handlers.start import start_Router

async def main():
    dp.include_router(start_Router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    print("Bot is working")
    asyncio.run(main())