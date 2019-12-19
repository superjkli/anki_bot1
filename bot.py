import discord
import pytz
from datetime import datetime
from datetime import timedelta
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()
channels = 
tz_jp = pytz.timezone('Asia/Tokyo')
token = 
colo_notify = 0
fodder_notify = 0
time_in_jp = datetime.now(tz_jp)
five_minutes = timedelta(minutes=5)
time_in_jp_five_minutes_ago = datetime.now(tz_jp) - five_minutes
colo_time = datetime.now(tz_jp).replace(hour = 23, minute = 0)    
colo_time_five_min_ago = colo_time - five_minutes

async def update_notify():
    await client.wait_until_ready()
    
    while not client.is_closed():
        time_in_jp = datetime.now(tz_jp)
        time_in_jp_five_minutes_ago = time_in_jp
        if time_in_jp_five_minutes_ago.strftime("%H:%M") == colo_time_five_min_ago.strftime("%H:%M"):
            await client.get_channel(channels).send("Five minutes before colo")
        if time_in_jp.strftime("%H:%M") == colo_time.strftime("%H:%M"):
            await client.get_channel(channels).send("it's colo time")
        await asyncio.sleep(10)

    

@client.event
async def on_message(message):
    if message.content == ".time":
        time_in_jp = datetime.now(tz_jp)
        time_in_jp_five_min_ago = time_in_jp - five_minutes
        await message.channel.send(f"""Time in japan: {time_in_jp.strftime("%H:%M:%S")}""")

    if message.content.find(".notify") != -1:
        if message.content.find("set") != -1:
            if message.content.find("colo") != -1:
                if message.content.find("08:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 8, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("12:30") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 12, minute = 30)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("22:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 22, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("23:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 23, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("19:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 19, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("20:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 20,minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("21:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 21, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("18:00") != -1:
                    colo_time = datetime.now(tz_jp).replace(hour = 18, minute = 0)
                    colo_time_five_min_ago = colo_time - five_minutes
                    await message.channel.send(f"""Colo time set to notify at {colo_time.strftime("%H:%M")}""")
                elif message.content.find("off") != -1:
                    colo_time = "N/A"
                    colo_time_five_min_ago = "N/A"
                    await message.channel.send("Colo notify off")
                else :
                    await message.channel.send("Invalid input")
                    colo_notify = 0
            elif message.channel.find("fodder") != -1:
                pass
            elif message.channel.find("special") != -1:
                pass

client.loop.create_task(update_notify())
client.run(token)
