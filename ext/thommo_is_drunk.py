import asyncio

import hikari
import lightbulb

HIKARI_STAFF_ROLE_ID = 734164204679856290
HIKARI_GUILD_ID = 574921006817476608
THOMMO_ID = 215061635574792192
plugin = lightbulb.Plugin("drunk")


async def unmute_task(bot: lightbulb.BotApp, user_id: hikari.Snowflakeish):
    await asyncio.sleep(60 * 60 * 8)
    await bot.rest.add_role_to_member(HIKARI_GUILD_ID, user_id, HIKARI_STAFF_ROLE_ID, reason="Thommo is probably not drunk anymore")


@plugin.command
@lightbulb.app_command_permissions(hikari.Permissions.ADMINISTRATOR, dm_enabled=False)
@lightbulb.command("thommo-is-drunk", "Save thommo from himself", guilds=[HIKARI_GUILD_ID])
@lightbulb.implements(lightbulb.SlashCommand)
async def thommo_is_drunk(ctx: lightbulb.Context):
    confirmation_buttons = (
        ctx.bot.rest.build_message_action_row()
        .add_interactive_button(hikari.ButtonStyle.SUCCESS, "drunk-confirm", label="Confirm")
        .add_interactive_button(hikari.ButtonStyle.DANGER, "drunk-cancel", label="Cancel")
    )
    msg = await ctx.respond(hikari.Embed(description="\n".join([
        "This command will mute thomm.o for 8 hours.",
        "You should only use this if he is embarrassing himself after drinking far too much (again).",
        "",
        "**Are you sure this is necessary?**",
    ])), component=confirmation_buttons)

    try:
        event = await ctx.bot.wait_for(
            hikari.InteractionCreateEvent,
            timeout=60,
            predicate=lambda e: isinstance(e.interaction, hikari.ComponentInteraction) and e.interaction.custom_id in ("drunk-confirm", "drunk-cancel")
        )
        confirmation_buttons = (
            ctx.bot.rest.build_message_action_row()
            .add_interactive_button(hikari.ButtonStyle.PRIMARY, "drunk-confirm", label="Confirm", is_disabled=True)
            .add_interactive_button(hikari.ButtonStyle.PRIMARY, "drunk-cancel", label="Cancel", is_disabled=True)
        )
        await event.interaction.create_initial_response(hikari.ResponseType.MESSAGE_UPDATE, components=[confirmation_buttons])
    except asyncio.TimeoutError:
        await msg.edit("Message timed out", embeds=[], components=[])
        return

    if event.interaction.custom_id == "drunk-confirm":
        await ctx.bot.rest.remove_role_from_member(ctx.guild_id, THOMMO_ID, HIKARI_STAFF_ROLE_ID, reason="Thommo is drunk again")
        await ctx.respond("Action confirmed - thomm.o is now muted.")
        ctx.bot.create_task(unmute_task(ctx.bot, THOMMO_ID))
    else:
        await ctx.respond("Action cancelled.")


def load(bot):
    bot.add_plugin(plugin)
