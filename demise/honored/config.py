import os
import discord
from discord.ext.commands import (Flag, ColorConverter)

class Authorization:
    async def getprefix(bot, message):
       if not message.guild: return "-"
       res = await bot.db.fetchrow("SELECT * FROM prefixes WHERE guild_id = $1", message.guild.id) 
       if res: guildprefix = res["prefix"]
       else: guildprefix = "-"    

       return guildprefix


      
    token = os.environ['MTE1MjQ4NTQ2OTE4NDA4NjA0Ng.GuHAWJ.Fe0-GEBT2X1gpsSuicdw5U1EvA1eOL8iZbW4Cg']
    owner_ids = [738981890043805707] 
    
    class database:
      host = 'db.dxnexsnwlrrbxaivjsvt.supabase.co'
      password = 'demisexstand123'
      database = 'postgres'
      user = 'postgres'
      port: int = 5432




class Color:
    normal = 0x2c2d31
    deny = 0x2c2d31
    warn = 0x2c2d31
    approve = 0x2c2d31
    msg = 0x2c2d31
  
class Emoji:
  approve = '<:check:1136608110144913438>'
  deny = '<:x_:1136608097331318904>'
  warn = '<:error:1131261503987781773>'
  lock = '<:emoji_12:1136609886365552730>'
  unlock = '<:unlock:1131261455535181876>'