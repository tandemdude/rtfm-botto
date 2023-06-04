import hikari
import lightbulb
import logging

logging.getLogger("lightbulb").setLevel(logging.DEBUG)
_LOGGER = logging.getLogger("rtfm_bot")

# List of all extensions to be loaded
extensions = ["ext.rtfm_commands", "ext.thommo_is_drunk"]

# Declares the bot prefix and token, taking values from files
prefix = "rtfm "
with open("token.txt") as fp:
    token = fp.read().strip()


# Main function creates bot, loads extensions and runs the bot
def run_bot():
    bot = lightbulb.BotApp(prefix=prefix, token=token, intents=hikari.Intents.ALL)
    if len(extensions) != 0:
        bot.load_extensions(*extensions)
    bot.run()


if __name__ == "__main__":
    run_bot()
