import discord
from discord.ext import commands
from datetime import datetime

current = datetime.today().strftime('%Y-%m-%d')
with open(f'Logs/{current}.txt', 'a') as logs:
    logs.write('Body module has been loaded.')
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
drgon = commands.Bot(command_prefix='dr', intents=intents)
drgon.remove_command('help')


cogs_list = [
        'Runners.funchat'
    ]
for cog in cogs_list:
    drgon.load_extension(f'{cog}')

@drgon.event
async def on_ready():
    try:
        guild = drgon.get_guild(1107031522428588164)
        member_count = len(guild.members)
        await drgon.change_presence(status=discord.Status.idle,
                                         activity=discord.Game(name=f'Looking at {member_count} cuties!'))
    except:
        current = datetime.today().strftime('%Y-%m-%d')
        with open(f'Logs/{current}.txt', 'a') as logs:
            logs.write('\nServer can not be reached.')


try:
    drgon.run(open('Data/systemfiles/token.txt', 'r').readline())
except:
    current = datetime.today().strftime('%Y-%m-%d')
    with open(f'Logs/{current}.txt', 'a') as logs:
        logs.write('\nFile Data/systemfiles/token.txt can not be found.')