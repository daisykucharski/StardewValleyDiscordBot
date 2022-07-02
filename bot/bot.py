import discord
import os
from dotenv import load_dotenv
import requests
import json

from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = os.getenv("API_URL")

bot = commands.Bot(command_prefix="!")

# COMMANDS

@bot.event
async def on_ready():
    """
    Print to console when the bot is ready
    """
    print('Bot online')

@bot.command(help='Get the birthday of a NPC')
async def birthday(ctx, name):
    """
    Get the birthday of the NPC with the given name
    and send to channel
    """
    # get birthday data from API
    url = f'{API_URL}/birthday?name={name}'
    birthday = requests.get(url).text

    # send bithday data to channel
    await ctx.channel.send(birthday)

@bot.command(help='Get the best gifts for a NPC')
async def best_gifts(ctx, name):
    """
    Get the best gifts for the NPC with the given 
    name and send to channel
    """
    # get best gift data from API
    url = f'{API_URL}/bestgifts?name={name}'
    best_gifts = requests.get(url).text

    # send best gift data to channel
    await ctx.channel.send(best_gifts)

@bot.command(help='Get a list of gifts that are universally loved')
async def universal_loves(ctx):
    """
    Get a list of gifts that are universally loved and send to channel
    """
    # get universal loves data from API
    url = f'{API_URL}/universalloves'
    universal_loves = requests.get(url).text

    # send universal loves data to channel
    await ctx.channel.send(universal_loves)

@bot.command(help='Get information about the given fish')
async def fish(ctx, fish):
    """
    Get information about the location, and season/time to 
    catch the given fish and send to channel
    """

    # get fish data from API
    url = f'{API_URL}/fishinfo?fish={fish}'
    response = requests.get(url)

    # if there was an error, send the error message that was received
    if response.status_code == 404:
        await ctx.channel.send(response.text)
        return

    # get fish info into object form
    fish_info = json.loads(response.text)

    # build embed to put fish info into
    embed = discord.Embed(title=fish)
    embed.add_field(name='Seasons', value=fish_info['seasons'], inline=False)
    embed.add_field(name='Time', value=fish_info['time'], inline=False)
    embed.add_field(name='Locations', value=fish_info['locations'], inline=False)

    # send embed to channel
    await ctx.send(embed=embed)


@bot.command(help='Get information about the given crop')
async def crop(ctx, crop):
    """
    Get information about the growth time and season of 
    the given crop and send to channel
    """
    # get crop data from API
    url = f'{API_URL}/cropinfo?crop={crop}'
    response = requests.get(url)

    # if there was an error, send the error message that was received
    if response.status_code == 404:
        await ctx.channel.send(response.text)
        return

    # get crop info into object form
    crop_info = json.loads(response.text)

    # build embed to put crop info into
    embed = discord.Embed(title=crop)
    embed.add_field(name='Seasons', value=crop_info['seasons'], inline=False)
    embed.add_field(name='Growth Time', value=crop_info['growth_time'], inline=False)

    # send embed to channel
    await ctx.send(embed=embed)


bot.run(DISCORD_TOKEN)