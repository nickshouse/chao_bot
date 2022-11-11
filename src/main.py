# Imports
import os
import discord
import bot_token
import asyncio
from discord.ext import commands
from discord import Interaction

# All commands must start with !
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!", case_insensitive=True, intents = discord.Intents.all())
client.remove_command("help")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=f"/chao", type=discord.ActivityType.playing))
    print("Chao Bot is online")
    try:
        synced = await client.tree.sync()
        print(f"Synced len({synced}) commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@client.event
async def on_command_error(ctx, error):
    print(f"An error occured: {str(error)}")
    
@client.tree.command(name="hello")
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello!")


async def main():
    await load_extensions()
    await client.start(bot_token.your_bot_token)


asyncio.run(main())
