import queue
import os
import discord
from discord.ext import commands, tasks

from bocik import token_holder
from bocik.features import message_checker

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
last_used_channel = None
message_queue = queue.Queue()


# @tasks.loop(seconds=30)
# async def message_queue_loop():
#     if last_used_channel is not None and message_queue.empty() is False:
#         await last_used_channel.send(message_queue.get())


@client.event
async def on_message(message):
    global last_used_channel
    last_used_channel = message.channel

    if message.author.bot is False and message.author.id != 8065 and len(message.content) != 0:
        print(message.author.display_name + ": " + message.content)
        message.content = message.content.lower()
        if not message.content.startswith("."):
            # say hello
            await check_and_send(message, message_checker.check_for_hello(message))
            # say bye
            await check_and_send(message, message_checker.check_for_bye(message))
            # say something nice
            await check_and_send(message, message_checker.check_for_compliment(message))
            # toss a coin
            await check_and_send(message, message_checker.check_for_coins(message))
            # rolling a dice
            await check_and_send(message, message_checker.check_for_dice(message))
            # rolling 8ball
            await check_and_send(message, message_checker.check_for_8ball(message))
            # jokes
            await check_and_send(message, message_checker.check_for_joke(message))
            # bajo jajo
            await check_and_send(message, message_checker.check_for_bajo_jajo(message))
            # kotki
            await check_and_send(message, message_checker.check_for_cats(message))
            # training
            await check_and_send(message, message_checker.check_for_exercise(message))
            # weather
            await check_and_send(message, message_checker.check_for_weather(message))


async def check_and_send(message, tmp):
    if tmp != "":
        await message.channel.send(tmp)


@client.event
async def on_ready():
    print("Your bot is ready!")


@client.command()
async def load(ctx, extension):
    client.load_extension(extension)


@client.command()
async def unload(ctx, extension):
    client.unload_extension(extension)


@client.command()
async def reload(ctx, extension):
    client.unload_extension(extension)
    client.load_extension(extension)


@client.command()
async def reload_all(ctx):
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            client.unload_extension(file[:-3])
            client.load_extension(file[:-3])


@client.event
async def on_member_join(member):
    print(f'{member} dołączył/a!')


@client.event
async def on_member_remove(member):
    print(f'{member} opuścił/a nas!')


# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(filename[:-3])

client.run(token_holder.TOKEN)
