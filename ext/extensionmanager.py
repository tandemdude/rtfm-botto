import lightbulb


class ExtensionManager(lightbulb.Plugin):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @lightbulb.owner_only()
    @lightbulb.command()
    async def load(self, ctx, *, extension):
        """
        Loads the specified error if possible
        Otherwise returns the error
        """
        try:
            self.bot.load_extension(extension)
            await ctx.respond("Extension Loaded Successfully")
        except Exception as e:
            await ctx.respond(f"{extension} Failed To Load.")
            await ctx.respond(e)

    @lightbulb.owner_only()
    @lightbulb.command()
    async def unload(self, ctx, *, extension):
        """
        Unloads the specified extension if possible
        Otherwise returns the error
        """
        try:
            self.bot.unload_extension(extension)
            await ctx.send("Extension Unloaded Successfully")
        except Exception as e:
            await ctx.respond(f"{extension} Failed To Load.")
            await ctx.respond(e)

    @lightbulb.owner_only()
    @lightbulb.command()
    async def reload(self, ctx, *, extension):
        """
        Reloads the specified extension if possible
        Otherwise returns the error
        """
        try:
            self.bot.reload_extension(extension)
            await ctx.send("Extension Reloaded Successfully")
        except Exception as e:
            await ctx.respond(f"{extension} Failed To Load.")
            await ctx.respond(e)

    @lightbulb.owner_only()
    @lightbulb.command()
    async def listext(self, ctx):
        """Lists all the currently loaded extensions"""
        extensions = ", ".join(self.bot.extensions)
        await ctx.respond(f"Currently Loaded Extensions:\n```{extensions}```")


def load(bot):
    bot.add_plugin(ExtensionManager(bot))


def unload(bot):
    bot.remove_plugin("ExtensionManager")
