from __future__ import annotations

from telegram import Update
from telegram.ext import CallbackContext

from .game_logic import BunkerGame


game = BunkerGame()


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to the Bunker game! Use /join to enter the lobby."
    )


def join(update: Update, context: CallbackContext) -> None:
    user = update.effective_user.first_name
    added = game.add_player(user)
    if added:
        update.message.reply_text(f"{user} joined the lobby")
    else:
        update.message.reply_text(f"{user} is already in the lobby")


def leave(update: Update, context: CallbackContext) -> None:
    user = update.effective_user.first_name
    removed = game.remove_player(user)
    if removed:
        update.message.reply_text(f"{user} left the lobby")
    else:
        update.message.reply_text(f"{user} is not in the lobby")


def begin(update: Update, context: CallbackContext) -> None:
    try:
        game.start_game()
    except RuntimeError as e:
        update.message.reply_text(str(e))
        return
    for player in game.players:
        role = game.get_role(player)
        update.message.reply_text(f"{player} is a {role}")

