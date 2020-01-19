import discord
import pytz
from datetime import datetime
from datetime import timedelta
import asyncio
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

channels = 
tz_jp = pytz.timezone('Asia/Tokyo')
token = ""
colo_notify = 0
fodder_notify = 0
time_in_jp = datetime.now(tz_jp)
five_minutes = timedelta(minutes=5)
time_in_jp_five_minutes_ago = datetime.now(tz_jp) - five_minutes
colo_time = datetime.now(tz_jp).replace(hour = 23, minute = 0)    
colo_time_five_min_ago = colo_time - five_minutes
colo_notified_flag = 0
colo_notified_five_ago_flag = 0
colo_flag = 1
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')    

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="help")
    embed.add_field(name="help", value="display this help", inline=False)
    embed.add_field(name="time", value="display time in JST", inline=False)
    embed.add_field(name="notify", value="set notify(only colo now)", inline=False)
    embed.add_field(name="notify usage", value="notify set [colo] [time(23:00 preset)/off]", inline=False)
    await ctx.send(embed=embed)
@bot.command()    
async def notify(ctx, action, area, do):
        if action == "set":
            if area == "colo":
                colo_flag = 1
                if do == "08:00":
                    colo_time = datetime.now(tz_jp).replace(hour = 8, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "12:30" :
                    colo_time = datetime.now(tz_jp).replace(hour = 12, minute = 30)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "22:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 22, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "23:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 23, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "19:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 19, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "20:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 20,minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "21:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 21, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif do == "18:00" :
                    colo_time = datetime.now(tz_jp).replace(hour = 18, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await ctx.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                else :
                    if do == "off" :
                        colo_flag = 0
                        await ctx.send("Colo notify off")
                    else:
                        await ctx.send("Invalid input")
            elif area == "fodder" :
                pass
            elif area == "special" :
                pass

async def update_notify():
    await bot.wait_until_ready()
    
    while not bot.is_closed():
        time_in_jp = datetime.now(tz_jp)
        time_in_jp_five_minutes_ago = time_in_jp
        if colo_flag == 1:
            if time_in_jp_five_minutes_ago.strftime("%H:%M") == colo_time_five_min_ago.strftime("%H:%M") and colo_notified_five_ago_flag == 0:
                await bot.get_channel(channels).send("Five minutes before colo")
                colo_notified_five_ago_flag = 1
            if time_in_jp.strftime("%H:%M") == colo_time.strftime("%H:%M") and colo_notified_flag == 0:
                await bot.get_channel(channels).send("it's colo time")
                colo_notified_flag = 1
            if time_in_jp.strftime("%H:%M") == (colo_time - five_minutes).strftime("%H:%M"):
                colo_notified_flag = 0
                colo_notified_five_ago_flag = 0
        await asyncio.sleep(1)


@bot.command()
async def time(ctx):
        time_in_jp = datetime.now(tz_jp)
        time_in_jp_five_min_ago = time_in_jp - five_minutes
        await ctx.send(f"""Time in japan: {time_in_jp.strftime("%H:%M:%S")}""")

bot.loop.create_task(update_notify())
bot.run(token)
