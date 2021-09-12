import lightbulb
import hikari


class CustomHelpCommand(lightbulb.HelpCommand):
	async def send_help_overview(self, context):
		emb = hikari.Embed(
			title="RTFM Help",
			description=f"Use `{context.clean_prefix}help [command]` for more info on a command.",
			colour=0x39393f
		)
		commands = await lightbulb.filter_commands(context, self.bot.commands)
		available_commands = f"```\n{', '.join(sorted([command.name for command in commands]))}\n```"
		emb.add_field(name="Available Commands", value=available_commands)
		await context.respond(emb)

	async def send_command_help(self, context, command):
		emb = hikari.Embed(title="RTFM Help", description=f"```{lightbulb.get_command_signature(command)}```", colour=0x39393f)
		emb.add_field(name="Details", value=lightbulb.get_help_text(command) or "No details available.", inline=False)
		emb.add_field(name="Aliases", value=f"```{', '.join(command.aliases)}```" if command.aliases else "No aliases exist.", inline=False) 
		await context.respond(emb)
