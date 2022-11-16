# Some notes...
# @client.tree.command() registers a command to the CommandTree

from typing import Optional
import typing
import bot_token
import discord
from discord import app_commands
from discord.ext import commands


MY_GUILD = discord.Object(id=815388895994839071)  # replace with your guild id


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), command_prefix="!")


bot = MyBot()
MY_GUILD=discord.Object(id=815388895994839071)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.tree.command()
async def hellow(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')



""" Umbra's Sync command, DM the bot to use
!sync   -> global sync
!sync ~ -> sync current guild
!sync * -> copies all global app commands to current guild and syncs
!sync ^ -> clears all commands from the current guild target and syncs (removes guild commands)
"""
@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[typing.Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=MY_GUILD)
            synced = await ctx.bot.tree.sync(guild=MY_GUILD)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}")
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.client.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


bot.run(bot_token.your_bot_token)
