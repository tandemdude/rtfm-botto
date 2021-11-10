import lightbulb
from lightbulb import commands

from ext.utils import api

api_plugin = lightbulb.Plugin("API")


@api_plugin.command
@lightbulb.command("rtfm", "Searches the docs for the given library")
@lightbulb.implements(commands.SlashCommandGroup)
async def _rtfm(_: lightbulb.context.Context) -> None:
    pass


@api_plugin.command
@_rtfm.child
@lightbulb.option("obj", "Query to search the docs for", required=False)
@lightbulb.command(
    "python", "Searches the python docs for the given query", aliases=["py"]
)
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _python(ctx: lightbulb.context.Context) -> None:
    await ctx.respond(await api.manager.do_rtfm("py", ctx.options.obj))


@api_plugin.command
@_rtfm.child
@lightbulb.option("obj", "Query to search the docs for", required=False)
@lightbulb.command("hikari", "Searches the hikari docs for the given query")
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _hikari(ctx: lightbulb.context.Context) -> None:
    await ctx.respond(await api.manager.do_rtfm("hikari", ctx.options.obj))


@api_plugin.command
@_rtfm.child
@lightbulb.option("obj", "Query to search the docs for", required=False)
@lightbulb.command(
    "lightbulb",
    "Searches the hikari-lightbulb docs for the given query",
    aliases=["hikari-lightbulb", "lb"],
)
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _lightbulb(ctx: lightbulb.context.Context) -> None:
    await ctx.respond(await api.manager.do_rtfm("lightbulb", ctx.options.obj))


@api_plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("purgecache", "Clears the rtfm cache")
@lightbulb.implements(commands.PrefixCommand)
async def purgecache(ctx: lightbulb.context.Context) -> None:
    api.manager.purge_cache()
    await ctx.respond("RTFM cache deleted.")


def load(bot):
    bot.add_plugin(api_plugin)


def unload(bot):
    bot.remove_plugin(api_plugin)
