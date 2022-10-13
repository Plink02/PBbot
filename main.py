import discord
from twitchio.ext import commands
import os
import asyncio
from dotenv import load_dotenv
from srcapi import findPB

load_dotenv()

Token = os.environ.get('DISCORD_BOT_SECRET')
client = discord.Client()
twitchBot = commands.Bot(
  token = os.environ['TWITCH_TOKEN'],
  client_id = os.environ['TWITCH_CLIENT_ID'],
  nick='pacealertbot',
  prefix='!',
  initial_channels=['plink02']
)


async def send_alert(alert, ctx):
  try:
    channels = client.get_all_channels()
    channel = discord.utils.get(channels, name="tests")
    guild = channel.guild
    role = discord.utils.get(guild.roles, name="Pace Alerts")
    await channel.send(f"""
    {role.mention}
    {alert}
    """)
    await ctx.send("Pace alert sent")
  except:
    await ctx.send("Failed to send pace alert")

  
@twitchBot.command(name='alert')
async def pace_alert_command(ctx):
  info = ctx.message.content
  info = info[6::]
  user = ctx.channel.name
  twitchUrl = " https://www.twitch.tv/" + user
  alert = user + info + twitchUrl
  print(alert)
  await send_alert(alert, ctx)

@twitchBot.command(name='pb')
async def get_player_pb(ctx):
  content = ctx.message.content
  content = content[4::]
  params = content.split(None,1)
  player = params[0]
  if player.startswith('@'):
    player = player[1::]
  #if only player is entered, default to any%/single segment
  if len(params) > 1:
    category = params[1]
    pb = findPB(player, category)
  else:
    pb = findPB(player)
  await ctx.send(pb)



if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.create_task(client.start(Token))
  loop.create_task(twitchBot.run())
  loop.run_forever()
  
