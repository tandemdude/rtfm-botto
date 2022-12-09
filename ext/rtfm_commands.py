import hikari
import lightbulb
from lightbulb import commands

from ext.utils import api

from rapidfuzz import fuzz
from rapidfuzz import process

api_plugin = lightbulb.Plugin("API", include_datastore=True)
api_plugin.d.managers = {
    "python": api.RTFMManager("python", "https://docs.python.org/3"),
    "hikari": api.RTFMManager("hikari", "https://docs.hikari-py.dev/en/stable/"),
    "lightbulb": api.RTFMManager(
        "lightbulb", "https://hikari-lightbulb.readthedocs.io/en/latest"
    ),
}


@api_plugin.command
@lightbulb.command("rtfm", "Searches the docs for the given library")
@lightbulb.implements(commands.SlashCommandGroup)
async def _rtfm(_: lightbulb.context.Context) -> None:
    pass


@api_plugin.command
@_rtfm.child
@lightbulb.option(
    "obj", "Query to search the docs for", required=False, autocomplete=True
)
@lightbulb.command(
    "python",
    "Searches the python docs for the given query",
    aliases=["py"],
    pass_options=True,
)
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _python(ctx: lightbulb.Context, obj: str) -> None:
    await ctx.respond(await api_plugin.d.managers["python"].do_rtfm(obj))


@_python.autocomplete("obj")
async def autocomplete_obj_python_docs(option: hikari.AutocompleteInteractionOption, _):
    matches = process.extract(
        option.value,
        api_plugin.d.managers["python"]._rtfm_cache.keys(),
        scorer=fuzz.QRatio,
        limit=5,
    )
    return [m[0] for m in matches]


@api_plugin.command
@_rtfm.child
@lightbulb.option(
    "obj", "Query to search the docs for", required=False, autocomplete=True
)
@lightbulb.command(
    "hikari", "Searches the hikari docs for the given query", pass_options=True
)
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _hikari(ctx: lightbulb.Context, obj: str) -> None:
    await ctx.respond(await api_plugin.d.managers["hikari"].do_rtfm(obj))


@_hikari.autocomplete("obj")
async def autocomplete_obj_hikari_docs(option: hikari.AutocompleteInteractionOption, _):
    matches = process.extract(
        option.value,
        api_plugin.d.managers["hikari"]._rtfm_cache.keys(),
        scorer=fuzz.QRatio,
        limit=5,
    )
    return [m[0] for m in matches]


@api_plugin.command
@_rtfm.child
@lightbulb.option(
    "obj", "Query to search the docs for", required=False, autocomplete=True
)
@lightbulb.command(
    "lightbulb",
    "Searches the hikari-lightbulb docs for the given query",
    aliases=["hikari-lightbulb", "lb"],
    pass_options=True,
)
@lightbulb.implements(commands.PrefixCommand, commands.SlashSubCommand)
async def _lightbulb(ctx: lightbulb.Context, obj: str) -> None:
    await ctx.respond(await api_plugin.d.managers["lightbulb"].do_rtfm(obj))


@_lightbulb.autocomplete("obj")
async def autocomplete_obj_lightbulb_docs(
    option: hikari.AutocompleteInteractionOption, _
):
    matches = process.extract(
        option.value,
        api_plugin.d.managers["lightbulb"]._rtfm_cache.keys(),
        scorer=fuzz.QRatio,
        limit=5,
    )
    return [m[0] for m in matches]


@api_plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("purgecache", "Clears the rtfm cache")
@lightbulb.implements(commands.PrefixCommand)
async def purgecache(ctx: lightbulb.Context) -> None:
    for manager in api_plugin.d.managers.values():
        manager.purge_cache()
    await ctx.respond("RTFM cache deleted.")


def load(bot):
    bot.add_plugin(api_plugin)


def unload(bot):
    bot.remove_plugin(api_plugin)
