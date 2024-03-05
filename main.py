import asyncio
import logging
import sys
from create_bot import dp, bot

from handlers import user, admin, other, test, docx


async def main() -> None:

    dp.include_routers(
        docx.user.docx_router,
        docx.atp_write.docx_router,
        docx.atp.docx_router,
        user.user_router,
        other.msg_router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    loop.run_forever()
