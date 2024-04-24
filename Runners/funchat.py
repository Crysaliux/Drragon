import discord
from discord.ext import commands
import asyncio

class Funchat(commands.Cog):
    def __init__(self, drgon):
        self.drgon = drgon

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id != 1107031522428588164:
            pass
        else:
            if message.author.id == 1219334236759392377:
                pass
            else:
                actual = message.content.lower()
                if 'ruu' in actual:
                    await message.reply('Ruuuur! :3')
                elif 'rawr' in actual:
                    await message.reply('Mrawrrrr! :3')
                elif 'rur' in actual:
                    await message.reply('Mrrh! >:3')
                elif 'awr' in actual:
                    await message.reply('Awwar! :3')

                await asyncio.sleep(2)

def setup(drgon):
    drgon.add_cog(Funchat(drgon))