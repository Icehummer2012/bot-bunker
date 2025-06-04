from __future__ import annotations

import logging
import os

from telegram.ext import (
    CommandHandler,
    Updater,
)

from . import handlers


logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")


def main() -> None:
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("join", handlers.join))
    dispatcher.add_handler(CommandHandler("leave", handlers.leave))
    dispatcher.add_handler(CommandHandler("begin", handlers.begin))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

