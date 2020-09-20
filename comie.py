import discord
import random
from discord import utils
from secretsanta import secretsanta
from imgur import imgur

adminNames = ["y0sh1#1990", "Sh4ky#3017"]

def mentionUser(user):
    return "<@" + str(user.id) + ">"

class Comie(discord.Client):
    santaRoleName = "Wichtel"

    ### READY MESSAGE
    async def on_ready(self):
        print("Bot is up and running.")
        return
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        ##### SECRET SANTA
        if message.content.startswith("!wichteln") and str(message.author) in adminNames:
            await secretsanta.exec(self, message)

        ##### IMGUR
        elif message.content.startswith("!img"):
            await imgur.exec(self, message)
            return

        ##### SELF HELP
        elif message.content.startswith("!help"):
            await message.channel.send("Hi " + mentionUser(message.author) + "!\nLeider kann ich noch nichts :(")
            return

        ##### UNKNOWN COMMAND
        elif message.content.startswith("!") and len(message.content) != 0:
            await message.channel.send("Den Befehl kenne ich nicht :/")
            return