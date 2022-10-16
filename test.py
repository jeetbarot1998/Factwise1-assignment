import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

ctxs = discord.Client()

# FOR COMMAND==============================================================
bot = commands.Bot(command_prefix='!')
username =  'quibler#9786'
channelname = 'locked access'

# @commands.has_role("locked access") # This must be exactly the name of the appropriate role
#  ADD
# @bot.command()
# async def addrole(ctx, arg: discord.Member):
#     member = ctx.message.author
#     await ctx.send(arg)
#     knownrole = discord.utils.get(ctx.guild.roles, name="locked_access")
#     await ctx.send(knownrole)
#     await arg.add_roles(knownrole)

# REVOKE
# @bot.command()
# async def revoke(ctx, arg: discord.Member):
#     member = ctx.message.author
#     await ctx.send(arg)
#     knownrole = discord.utils.get(ctx.guild.roles, name="locked_access")
#     await arg.remove_roles(knownrole)

# To SWITCH
# @bot.command(name="alter_roles")
# async def _role(ctx, role: discord.Role):
#     if role in ctx.author.roles:
#         await ctx.author.remove_roles(role)
#     else:
#         await ctx.author.add_roles(role)

@bot.event
async def on_ready():
  print('We have logged in{0.user}'.format(bot))


@bot.event
async def on_message(msg):
  # if msg.author == bot.guilds.user:
  #   return
  if msg.content.startswith('$hello'):
      # print(bot.guild)
      async for guild in bot.fetch_guilds(limit=150):
          print(guild.name)
      # knownrole = discord.utils.get(discord.Member.guild.roles, name="locked_access")
      # knownrole = discord.utils.get(bot.guild.roles, name="locked_access")
      # print(knownrole)

bot.run('OTQzNTEyNzM5NDE3MDU1MzEy.Yg0Itg._vRM5-otUJ31GQn8fCikAocpuBo')
# ==================================