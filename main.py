import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import discord
from discord.ext import commands

# 1. Dummy HTTP Server for Render Port Check
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_http_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_http_server, daemon=True).start()

# 2. Discord Bot Logic
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

VOICE_CHANNEL_ID = 1525434040822403283

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel:
        await channel.connect(reconnect=True)
        print("Connected to Voice Channel!")

token = os.environ.get("BOT_TOKEN")
bot.run(token)
