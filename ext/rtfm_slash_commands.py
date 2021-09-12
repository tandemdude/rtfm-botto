import typing

import lightbulb
from lightbulb import slash_commands

from ext.utils import api


class SlashAPI(slash_commands.SlashCommandGroup):
    name = "rtfm"
    description = "Searches the docs for the given library."


@SlashAPI.subcommand()
class PythonRTFM(slash_commands.SlashSubCommand):
    name = "python"
    description = "Searches python's API documentation."
    # Options
    object_: typing.Optional[str] = slash_commands.Option("Search query.", name="object")

    async def callback(self, context):
        await context.respond(await api.manager.do_rtfm("py", context.option_values.object))


@SlashAPI.subcommand()
class HikariRTFM(lightbulb.slash_commands.SlashSubCommand):
    name = "hikari"
    description = "Searches hikari's API documentation."
    # Options
    object_: typing.Optional[str] = slash_commands.Option("Search query.", name="object")

    async def callback(self, context):
        await context.respond(await api.manager.do_rtfm("hikari", context.option_values.object))


@SlashAPI.subcommand()
class LightbulbRTFM(lightbulb.slash_commands.SlashSubCommand):
    name = "lightbulb"
    description = "Searches hikari-lightbulb's API documentation."
    # Options
    object_: typing.Optional[str] = slash_commands.Option("Search query.", name="object")

    async def callback(self, context):
        await context.respond(await api.manager.do_rtfm("lightbulb", context.option_values.object))


def load(bot):
    bot.add_slash_command(SlashAPI)


def unload(bot):
    bot.remove_slash_command(SlashAPI)
