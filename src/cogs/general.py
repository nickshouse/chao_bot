from discord import app_commands
from discord.ext import commands

# all cogs inherit from this base class
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # adding a bot attribute for easier access

    # adding a command to the cog
    @commands.command(name="ping")
    async def pingcmd(self, ctx):
        await ctx.send(ctx.author.mention)
    
    # adding a slash command to the cog (make sure to sync this!)
    @app_commands.command(name="ping")
    async def slash_pingcmd(self, interaction):
        await interaction.response.send_message(interaction.user.mention)

    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot):
    await bot.add_cog(General(bot=bot))
