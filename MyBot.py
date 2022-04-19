import os
#import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

#client = discord.Client()

class DocBot(commands.Bot):
    def _init_(self):
        super()._init_(command_prefix="!")


    async def on_ready(self):
        print(f"Bonjour {self.user.display_name} :)!")


    async def on_message(self,message):
        if message.content.lower() == "Coucou":
            await message.channel.send("Coucou :)")

        if message.content.lower() == "Help":
            await message.channel.send("Les commandes à taper sont !Coucou, !ping et !Help")

        if message.content.lower() == "ping":
            await message.channel.send("pong")
    
doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN")) 