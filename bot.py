import hikari
import lightbulb
import logging

from ext import help as help_

logging.getLogger("lightbulb").setLevel(logging.DEBUG)
_LOGGER = logging.getLogger("rtfm_bot")

# List of all extensions to be loaded
extensions = ["ext.extensionmanager", "ext.rtfm_commands", "ext.rtfm_slash_commands"]

# Link to root of the documentation page
DOCUMENTATION_LINK = "https://docs.python.org/3"

# Declares the bot prefix and token, taking values from files
prefix = "rtfm "
with open("token.txt") as fp:
    token = fp.read().strip()


# Main function creates bot, loads extensions and runs the bot
def run_bot():
    bot = lightbulb.Bot(prefix=prefix, token=token, intents=hikari.Intents.ALL, help_class=help_.CustomHelpCommand)
    bot.docs_link = DOCUMENTATION_LINK
    if len(extensions) != 0:
        for ext in extensions:
            bot.load_extension(ext)
            _LOGGER.info(f"Loaded ext {ext}")
    bot.run()


if __name__ == "__main__":
    run_bot()
