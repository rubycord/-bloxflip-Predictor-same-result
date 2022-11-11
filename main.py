import discord, time
import cloudscraper, requests
import random, threading
import asyncio
from discord import app_commands
from discord.ext import commands
from random import randint as tokenSearch
import bloxflip


bot = commands.Bot(command_prefix='-', intents= discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name = "matrix on top!", url = "https://www.twitch.tv/ttoppl"))
    print("Bot is up and ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} Command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="free-mines")
@app_commands.checks.cooldown(1, 60, key = lambda i: (i.guild_id))
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Please enter a vaild serverhash :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:'
        a = tokenSearch(1, 8)
        b = tokenSearch(9, 13)
        c = tokenSearch(14, 17)
        d = tokenSearch(18, 25)
        if a == 1:
          mine1 = ":green_square:"
        elif a == 2:
          mine2 = ":green_square:"
        elif a == 3:
          mine3 = ":green_square:"
        elif a == 4:
          mine4 = ":green_square:"
        elif a == 5:
           mine5 = ":green_square:"
        elif a == 6:
          mine6 = ":green_square:"
        elif a == 7:
          mine7 = ":green_square:"
        elif a == 8:
          mine8 = ":green_square:"
        if b == 9:
          mine9 = ":green_square:"
        elif b == 10:
          mine10 = ":green_square:"
        elif b == 11:
          mine11 = ":green_square:"
        elif b == 12:
          mine12 = ":green_square:"
        elif b == 13:
          mine13 = ":green_square:"
        if c == 14:
          mine14 = ":green_square:"
        elif c == 15:
          mine15 = ":green_square:"
        elif c == 16:
          mine16 = ":green_square:"
        elif c == 17:
          mine17 = ":green_square:"
        if d == 18:
          mine18 = ":green_square:"
        elif d == 19:
          mine19 = ":green_square:"
        elif d == 20:
          mine20 = ":green_square:"
        elif d == 21:
          mine21 = ":green_square:"
        elif d == 22:
          mine22 = ":green_square:"
        elif d == 23:
          mine23 = ":green_square:"
        elif d == 24:
          mine24 = ":green_square:"
        elif d == 25:
          mine25 = ":green_square:"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """
        gamedata = f"""
        Info
        ───────────────
        Mines: {mines}
        ───────────────
        :green_square: is a predicted safe spot
        ───────────────
        """
        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="Your Prediction", value=result)
        em.add_field(name="Game Data", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="This serverhash has already been used!", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()


@bot.tree.command(name="premium-mines")
@discord.app_commands.checks.has_role("Buyer")
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Please enter a vaild serverhash :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:'
        a = tokenSearch(1, 8)
        b = tokenSearch(9, 13)
        c = tokenSearch(14, 17)
        d = tokenSearch(18, 25)
        e = tokenSearch(22, 25)
        
        a1 = tokenSearch(26, 33)
        b1 = tokenSearch(34, 38)
        c1 = tokenSearch(39, 42)

        a2 = tokenSearch(1, 12)
        b2 = tokenSearch(13, 25)
        
 

        # normal mines

        if a == 1:
          mine1 = ":green_square:"
        elif a == 2:
          mine2 = ":green_square:"
        elif a == 3:
          mine3 = ":green_square:"
        elif a == 4:
          mine4 = ":green_square:"
        elif a == 5:
           mine5 = ":green_square:"
        elif a == 6:
          mine6 = ":green_square:"
        elif a == 7:
          mine7 = ":green_square:"
        elif a == 8:
          mine8 = ":green_square:"
        if b == 9:
          mine9 = ":green_square:"
        elif b == 10:
          mine10 = ":green_square:"
        elif b == 11:
          mine11 = ":green_square:"
        elif b == 12:
          mine12 = ":green_square:"
        elif b == 13:
          mine13 = ":green_square:"
        if c == 14:
          mine14 = ":green_square:"
        elif c == 15:
          mine15 = ":green_square:"
        elif c == 16:
          mine16 = ":green_square:"
        elif c == 17:
          mine17 = ":green_square:"
        if d == 18:
          mine18 = ":green_square:"
        elif d == 19:
          mine19 = ":green_square:"
        elif d == 20:
          mine20 = ":green_square:"
        elif d == 21:
          mine21 = ":green_square:"
        if e == 22:
          mine22 = ":green_square:"
        elif e == 23:
          mine23 = ":green_square:"
        elif e == 24:
          mine24 = ":green_square:"
        elif e == 25:
          mine25 = ":green_square:"


                # 50% mines

        if a2 == 1:
          mine1 = ":blue_square:"
        elif a2 == 2:
          mine2 = ":blue_square:"
        elif a2 == 3:
          mine3 = ":blue_square:"
        elif a2 == 4:
          mine4 = ":blue_square:"
        elif a2 == 5:
           mine5 = ":blue_square:"
        elif a2 == 6:
          mine6 = ":blue_square:"
        elif a2 == 7:
          mine7 = ":blue_square:"
        elif a2 == 8:
          mine8 = ":blue_square:"
        elif a2 == 10:
          mine10 = ":blue_square:"
        elif a2 == 11:
          mine11 = ":blue_square:"
        elif a2 == 12:
          mine12 = ":blue_square:"
        elif a2 == 13:
          mine12 = ":blue_square:"
        elif a2 == 14:
          mine12 = ":blue_square:"
        if b2 == 15:
          mine1 = ":blue_square:"
        if b2 == 16:
          mine1 = ":blue_square:"
        elif b2 == 17:
          mine2 = ":blue_square:"
        elif b2 == 18:
          mine3 = ":blue_square:"
        elif b2 == 19:
          mine4 = ":blue_square:"
        elif b2 == 20:
           mine5 = ":blue_square:"
        elif b2 == 21:
          mine6 = ":blue_square:"
        elif b2 == 22:
          mine7 = ":blue_square:"
        elif b2 == 23:
          mine8 = ":blue_square:"
        elif b2 == 24:
          mine10 = ":blue_square:"
        elif b2 == 23:
          mine11 = ":blue_square:"
        elif b2 == 24:
          mine12 = ":blue_square:"
        elif b2 == 25:
          mine12 = ":blue_square:"


        # grey mines

        if a1 == 26:
          mine1 = ":orange_square:"
        elif a1 == 27:
          mine2 = ":orange_square:"
        elif a1 == 28:
          mine3 = ":orange_square:"
        elif a1 == 29:
          mine4 = ":orange_square:"
        elif a1 == 30:
           mine5 = ":orange_square:"
        elif a1 == 31:
          mine6 = ":orange_square:"
        elif a1 == 32:
          mine7 = ":orange_square:"
        elif a1 == 33:
          mine8 = ":orange_square:"
        if b1 == 34:
          mine9 = ":orange_square:"
        elif b1 == 35:
          mine10 = ":orange_square:"
        elif b1 == 36:
          mine11 = ":orange_square:"
        elif b1 == 37:
          mine12 = ":orange_square:"
        elif b1 == 38:
          mine13 = ":orange_square:"
        if c1 == 39:
          mine14 = ":orange_square:"
        elif c1 == 40:
          mine15 = ":orange_square:"
        elif c1 == 41:
          mine16 = ":orange_square:"
        elif c1 == 42:
          mine17 = ":orange_square:"



        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """

        gamedata = f"""
        Info
        ────────────────
        Mines: {mines}
        ────────────────
        :red_square: Is where a bomb could possibly be
        ────────────────
        :orange_square: Is a commom pattern of mines
        ────────────────
        :green_square: Is showing a Predicton
        ────────────────
        :blue_square: Is a 50/50 prediction
        """


        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="Your Prediction", value=result)
        em.add_field(name="Info", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="This Round id has already been used", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()


# PAID MINES ----------------------------------------------------

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        return await interaction.response.send_message(error, ephemeral = True)
    elif isinstance(error, app_commands.BotMissingPermissions):
        return await interaction.response.send_message(error, ephemeral = True)
    else:
        await interaction.response.send_message("an error occurred!", ephemeral = True)
        raise error


bot.run("MTA0MDMzMTM2NTExMzEzOTI5MQ.Gll-HC.q0d2Mf5NciIAoDAixaWu-NFXhsTHdbjSbip_kc")
          mine3 = ":green_square:"
        elif a == 4:
          mine4 = ":green_square:"
        elif a == 5:
           mine5 = ":green_square:"
        elif a == 6:
          mine6 = ":green_square:"
        elif a == 7:
          mine7 = ":green_square:"
        elif a == 8:
          mine8 = ":green_square:"
        if b == 9:
          mine9 = ":green_square:"
        elif b == 10:
          mine10 = ":green_square:"
        elif b == 11:
          mine11 = ":green_square:"
        elif b == 12:
          mine12 = ":green_square:"
        elif b == 13:
          mine13 = ":green_square:"
        if c == 14:
          mine14 = ":green_square:"
        elif c == 15:
          mine15 = ":green_square:"
        elif c == 16:
          mine16 = ":green_square:"
        elif c == 17:
          mine17 = ":green_square:"
        if d == 18:
          mine18 = ":green_square:"
        elif d == 19:
          mine19 = ":green_square:"
        elif d == 20:
          mine20 = ":green_square:"
        elif d == 21:
          mine21 = ":green_square:"
        elif d == 22:
          mine22 = ":green_square:"
        elif d == 23:
          mine23 = ":green_square:"
        elif d == 24:
          mine24 = ":green_square:"
        elif d == 25:
          mine25 = ":green_square:"
        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        result = f"""
        Mines
        {row1}
        {row2}
        {row3}
        {row4}
        {row5}
        """
        gamedata = f"""
        Info
        ───────────────
        Mines: {mines}
        ───────────────
        :green_square: is a predicted safe spot
        ───────────────
        """
        dfile = open("dataRes.txt", "w")
        dfile.write(result)
        dfile.close()
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="Your Prediction", value=result)
        em.add_field(name="Game Data", value=gamedata)
        await interaction.response.send_message(embed=em)
      elif serverhash == rid:
        dafile = open("dataRes.txt", "r")
        pfp = ' '
        em = discord.Embed(color=0x030B33)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Enjoy! • Detect Predictor")
        em.add_field(name="This serverhash has already been used!", value=dafile.read())
        await interaction.response.send_message(embed=em)
        dafile.close()
      rfile.close()


@bot.tree.command(name="premium-mines")
@discord.app_commands.checks.has_role("Buyer")
@app_commands.describe(serverhash = "enter your serverhash", mines = "enter your amount of mines")
async def mines(interaction: discord.Interaction, serverhash: str, mines: str):
    serverhash = str(serverhash)
    serverhash_length = len(serverhash)
    if serverhash_length < 64:
        await interaction.response.send_message(":x: Please enter a vaild serverhash :x:")
    elif serverhash_length == 64:
      try:
        rfile = open("dataID.txt", "r")
      except:
        e = open("dataID.txt", "w")
        e.write("data")
        e.close()
        rfile = open("dataID.txt", "r")

      rid = rfile.read(64)
      if rid != serverhash:
        wfile = open("dataID.txt", "w")
        wfile.write(serverhash)
        wfile.close()
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:', ':red_square:'
        a = tokenSearch(1, 8)
        b = tokenSearch(9, 13)
        c = tokenSearch(14, 17)
        d = tokenSearch(18, 25)
        e = tokenSearch(22, 25)
        
        a1 = tokenSearch(26, 33)
        b1 = tokenSearch(34, 38)
        c1 = tokenSearch(39, 42)

        a2 = tokenSearch(1, 12)
        b2 = tokenSearch(13, 25)
        
 

        # normal mines

        if a == 1:
          mine1 = ":green_square:"
        elif a == 2:
          mine2 = ":green_square:"
        elif a == 3:
          mine3 = ":green_square:"
        elif a == 4:
          mine4 = ":green_square:"
        elif a == 5:
           mine5 = ":green_square:"
        elif a == 6:
          mine6 = ":green_square:"
        elif a == 7:
          mine7 = ":green_square:"
        elif a == 8:
          mine8 = ":green_square:"
        if b == 9:
          mine9 = ":green_square:"
        elif b == 10:
          mine10 = ":green_square:"
        elif b == 11:
          mine11 = ":green_square:"
        elif b == 12:
          mine12 = ":green_square:"
        elif b == 13:
          mine13 = ":green_square:"
        if c == 14:
          mine14 = ":green_square:"
        elif c == 15:
          mine15 = ":green_square:"
        elif c == 16:
          mine16 = ":green_square:"
        elif c == 17:
          mine17 = ":green_square:"
        if d == 18:
          mine18 = ":green_square:"
        elif d == 19:
          mine19 = ":green_square:"
        elif d == 20:
          mine20 = ":green_square:"
        elif d == 21:
          mine21 = ":green_square:"
        if e == 22:
          mine22 = ":green_square:"
        elif e == 23:
          mine23 = ":green_square:"
        elif e == 24:
          mine24 = ":green_square:"
        elif e == 25:
          mine25 = ":green_square:"


                # 50% mines

        if a2 == 1:
          mine1 = ":blue_square:"
        elif a2 == 2:
          mine2 = ":blue_square:"
        elif a2 == 3:
          mine3 = ":blue_square:"
        elif a2 == 4:
          mine4 = ":blue_square:"
        elif a2 == 5:
           mine5 = ":blue_square:"
        elif a2 == 6:
          mine6 = ":blue_square:"
        elif a2 == 7:
          mine7 = ":blue_square:"
        elif a2 == 8:
          mine8 = ":blue_square:"
        elif a2 == 10:
          mine10 = ":blue_square:"
        elif a2 == 11:
          mine11 = ":blue_square:"
        elif a2 == 12:
          mine12 = ":blue_square:"
        elif a2 == 13:
          mine12 = ":blue_square:"
        elif a2 == 14:
          mine12 = ":blue_square:"
        if b2 == 15:
          mine1 = ":blue_square:"
        if b2 == 16:
          mine1 = ":blue_square:"
        elif b2 == 17:
          mine2 = ":blue_square:"
        elif b2 == 18:
          mine3 = ":blue_square:"
        elif b2 == 19:
          mine4 = ":blue_square:"
        elif b2 == 20:
           mine5 = ":blue_square:"
        elif b2 == 21:
          mine6 = ":blue_square:"
        elif b2 == 22:
          mine7 = ":blue_square:"
        elif b2 == 23:
          mine8 = ":blue_square:"
        elif b2 == 24:
          mine10 = ":blue_square:"
        elif b2 == 23:
          mine11 = ":blue_square:"
        elif b2 == 24:
          mine12 = ":blue_square:"
        elif b2 == 25:
          mine12 = ":blue_square:"


        # grey mines

        if a1 == 26:
          mine1 = ":orange_square:"
        elif a1 == 27:
          mine2 = ":orange_square:"
        elif a1 == 28:
          mine3 = ":orange_square:"
        elif a1 == 29:
          mine4 = ":orange_square:"
        elif a1 == 30:
           mine5 = ":orange_square:"
        elif a1 == 31:
          mine6 = ":orange_square:"
        elif a1 == 32:
          mine7 = ":orange_square:"
        elif a1 == 33:
          mine8 = ":orange_square:"
        if b1 == 34:
          mine9 = ":orange_square:"
        elif b1 == 35:
          mine10 = ":orange_square:"
        elif b1 == 36:
          mine11 = ":orange_square:"
        elif b1 == 37:
          mine12 = ":orange_square:"
        elif b1 == 38:
          mine13 = ":orange_square:"
        if c1 == 39:
          mine14 = ":orange_square:"
        elif c1 == 40:
          mine15 = ":orange_square:"
        elif c1 == 41:
          mine16 = ":orange_square:"
        elif c1 == 42:
          mine17 = ":orange_square:"





bot.run("token here")
