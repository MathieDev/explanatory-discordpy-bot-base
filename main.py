import discord
from discord.ext import commands
import os

# This project will explain what most of the code is doing because there's too many github projects about discordpy bot bases but none of them actually explain anything.

#Uncomment the part below to load the bot token from a .env file for replit users or for other reasons (Pretty sure repl.it doesn't support .env files because it is deprecated so I don't know. I'm just going to leave it here for now)
#from dotenv import load_dotenv
#load_dotenv()

prefix = "!" # The prefix that the bot will use.
status = "With Mathie's Bot Base!" # Keep in mind that it will say "Playing With Mathie's Bot Base!"
token = "TOKEN_HERE" # Replace this with your bot token


bot = commands.Bot(command_prefix=[prefix], description="Mathie's Bot Base For His Stupid Little Github Page So That He Can Be Proud Of Himself For Once!") # This is the bot itself




@bot.event
async def on_ready(): #  What you put here will be ran when ur bot runs/is ready
    await bot.change_presence(activity=discord.Game(status)) # If u would like to change it from a variable to an actual string just change the status variable to the string you want.
    print('You are logged in with username: ' + bot.user.name) # This will print the username of the bot in console when the bot is logged in successfully.

@bot.command() # You must put this before every command so that the bot knows that is it a command and not a method
async def theoneandonlytestcommand(ctx): # This is the command that will be ran, the ctx is the context of the command
    await ctx.send("This is the one and only test command!") # Everything after the command is what the command will execute, this is how you send a message in chat. A common issue people do is forget to put a "await" before the message.




bot.run(token) # This is the token for your bot, set at the start of the code as the token variable. You can get a token from the discord developer website. This just runs the bot.
#To load ur token from a .env file, uncomment the 2 lines at the top of the code and change the token variable to os.getenv("DISCORD_TOKEN"). Then create a .env file with a DISCORD_TOKEN variable in it in the root directory of your project aka the directory that the main.py file is in.



# Shoutout to github copilot for the helping me comment on this code more easily and without spelling mistakes.
# Made by Mathie#8820