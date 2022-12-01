from discord import app_commands
from discord.ext import commands

# all cogs inherit from this base class
class Chao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # adding a bot attribute for easier access

    # doing something when the cog gets loaded/unloaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot):
    await bot.add_cog(Chao(bot=bot))
