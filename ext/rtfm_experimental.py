import lightbulb

plugin = lightbulb.Plugin("Experimental", description="Experimental commands that may or may not work")

ACCEPTED_LIBS = {
    "lightbulb": "https://hikari-lightbulb.readthedocs.io/en/latest",
}


@plugin.command
@lightbulb.option("lib", "Library to search the docs for")
@lightbulb.command("rtfd", "Experimental RTFM implementation")
@lightbulb.implements(lightbulb.PrefixCommand)
async def rtfd_command(ctx: lightbulb.PrefixContext) -> None:
    if ctx.options.lib not in ACCEPTED_LIBS:
        await ctx.respond("Requested lib not recognised.")
        return



def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
