import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# VOICE CHANNEL ID
VOICE_CHANNEL_ID = 1525434017955184690

@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel:
        await channel.connect(reconnect=True)
        print("Connected to voice channel 24/7!")

client.run(os.getenv('BOT_TOKEN'))