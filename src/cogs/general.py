# Imports
import discord
import random
from time import sleep
from discord.ext import commands


# Class to hold functions for general commands
class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Dice roller
    @commands.command()
    async def d(self, ctx, num: int, amount: int):
        for i in range(amount):
            await ctx.send(random.randint(1, num))


# Setup function for cog
async def setup(client):
    await client.add_cog(General(client))
