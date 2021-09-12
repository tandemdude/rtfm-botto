import lightbulb

from ext.utils import api


class API(lightbulb.Plugin):
    @lightbulb.command(aliases=["py", "python3", "py3"])
    async def python(self, ctx, *, obj=None):
        await ctx.respond(await api.manager.do_rtfm("py", obj))

    @lightbulb.command(aliases=["dpy"])
    async def discordpy(self, ctx, *, obj=None):
        await ctx.respond(await api.manager.do_rtfm("dpy", obj))

    @lightbulb.command(aliases=["hk"])
    async def hikari(self, ctx, *, obj=None):
        await ctx.respond(await api.manager.do_rtfm("hikari", obj))

    @lightbulb.command(name="lightbulb", aliases=["lb", "betterdpy"])
    async def _lightbulb(self, ctx, *, obj=None):
        await ctx.respond(await api.manager.do_rtfm("lightbulb", obj))

    @lightbulb.owner_only()
    @lightbulb.command(aliases=["clearcache"])
    async def reloadcache(self, ctx):
        api.manager.purge_cache()
        await ctx.respond("RTFM cache deleted.")


def load(bot):
    bot.add_plugin(API())


def unload(bot):
    bot.remove_plugin("API")
