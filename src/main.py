# Some notes...
# @bot.tree.command() registers a command to the CommandTree
# class MyBot(commands.Bot): means that MyBot extends from commands.Bot
# Extension paths use a . instead of a /
# pip install discord

from discord.ext import commands
import discord
import logger
import bot_token


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix="!")

    async def setup_hook(self):
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.sync")

#bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")
bot = MyBot()
MY_GUILD = discord.Object(id=815388895994839071)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


bot.run(bot_token.your_bot_token, log_handler=logger.log())
