import os
import httpx
import json
import re
import random
import string
import discord
from discord.ext import commands
from io import BytesIO
import time
import requests
from discord_timestamps import format_timestamp, TimestampType
import json
import traceback
from discord import Embed

# dont skid fag's
# zt#7380 pw bot
# discord.gg/lead

api_key = "leak check key"
client = commands.Bot(
    command_prefix=".",
    help_command=None,
    reconnect=True,
    activity=discord.Streaming(name=".shelp", url="https://twitch.tv/twitch")
)

@client.event
async def on_ready():
    print("zt is running")

@client.command()
async def gen(ctx, type="keys"):
    if ctx.author.id in json.loads(open("admins.json", "r").read()):
        key = random.choices(string.ascii_letters + string.digits, k=16)
        keys=json.loads(open("keys.json", "r").read())
        newkey = ""
        for lol in key:
            newkey += lol
        keys.append(newkey)
        with open('keys.json', 'w') as f:
            json.dump(keys, f)
        embed=discord.Embed(title="success", description="sent key to your dms!", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)
        await ctx.author.send(newkey)
    else:
        embed=discord.Embed(title="error", description="you are not an admin!", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def redeem(ctx, key):
    if not ctx.author.id in json.loads(open("access.json", "r").read()):
        if key in json.loads(open("keys.json", "r").read()):
            keys=json.loads(open("keys.json", "r").read())
            keys.remove(key)
            with open('keys.json', 'w') as f:
                json.dump(keys, f)
            access=json.loads(open("access.json", "r").read())
            access.append(ctx.author.id)
            with open('access.json', 'w') as f:
                json.dump(access, f)
            embed=discord.Embed(title="success", description="redeemed your key!", color=000000)
            embed.set_author(name="zone", url="https://discord.com/api/oauth2/authorize?client_id=972735257516331069&permissions=274878286928&scope=bot", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="key doesn't exist!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="you already have access to zone!", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def revoke(ctx, id):  
    if ctx.author.id in json.loads(open("admins.json", "r").read()):
        if int(id) in json.loads(open("access.json", "r").read()):
            access=json.loads(open("access.json", "r").read())
            access.remove(int(id))
            with open('access.json', 'w') as f:
                json.dump(access, f)
            embed=discord.Embed(title="success", description="removed premium from user!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="user doesn't have premium!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="you are not an admin!", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def e(ctx, mail):
    if re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), mail):
        if int(ctx.author.id) in json.loads(open("access.json", "r").read()):
           
                info = requests.get(f'https://leakcheck.net/api?key={api_key}&check={mail}&type=email').json()
                if info["success"] == True:
                    if info["found"] > 0:
                        passwords = []
                        for elem in info['result']:
                            passwords.append({"name" : elem['line']})
                        content = '\n'.join(d['name'] for d in passwords)
                        if len(passwords) > 10:
                            buffer = BytesIO(content.encode('utf-8'))
                            file = discord.File(buffer, filename='passwords.txt')
                            embed=discord.Embed(title="Success!", description="please check the passwords using the file - zt", color=000000)
                            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                            embed.set_footer(text=ctx.author.name)
                            await ctx.send(embed=embed, file=file)
                            return
                        embed=discord.Embed(title="success", description="```" + content + "```", color=000000)
                        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                        embed.set_footer(text=ctx.author.name)
                        await ctx.send(embed=embed, file=file)
                    else:
                        embed=discord.Embed(title="failed", description="no passwords found", color=000000)
                        embed.set_author(name="zone", url="https://discord.com/api/oauth2/authorize?client_id=972735257516331069&permissions=274878286928&scope=bot", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                        embed.set_footer(text=ctx.author.name)
                        await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(title="failed", description=info["error"], color=000000)
                    embed.set_author(name="zone", url="https://discord.com/api/oauth2/authorize?client_id=972735257516331069&permissions=274878286928&scope=bot", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                    embed.set_footer(text=ctx.author.name)
                    await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="you don't have access to zone!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="thats not a valid email!", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def p(ctx, u):
  if int(ctx.author.id) in json.loads(open("access.json", "r").read()):
    if ctx.guild.id != 980538576850804776:
        return
    info=requests.get(f'https://leakcheck.net/api?key={api_key}&check={u}&type=password', headers={"user-agent": "zone"}).json()
    print("info")
    if info["success"] == True:
        if info["found"] > 0:
            passwords = []
            for elem in info['result']:
                passwords.append({"name" : elem['line']})
            content = '\n'.join(d['name'] for d in passwords)
            if len(passwords) > 10:
                buffer = BytesIO(content.encode('utf-8'))
                file = discord.File(buffer, filename='passwords.txt')
                embed=discord.Embed(title="Success", description="please check the passwords using the file - zt", color=000000)
                embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                embed.set_footer(text=ctx.author.name)
                await ctx.send(embed=embed, file=file)
                return
            embed=discord.Embed(title="success", description="```" + content + "```", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="failed", description="no passwords found", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="failed", description=info["error"], color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def start(ctx):
    if int(ctx.guild.id) == 980538576850804776:
        if int(ctx.author.id) in json.loads(open("access.json", "r").read()):
            for channel in ctx.guild.channels:
                if channel.name == str(ctx.author.id):
                    embed=discord.Embed(title="error", description=f"you already have a priv channel in <#{channel.id}>", color=000000)
                    embed.set_author(name="zone", url="https://discord.gg/ngf", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                    embed.set_footer(text=ctx.author.name)
                    await ctx.send(embed=embed)
                    return
            guild = ctx.guild
            user = ctx.message.author
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                user: discord.PermissionOverwrite(read_messages=True),
            }
            channel = await guild.create_text_channel(ctx.author.id, overwrites=overwrites)
            embed=discord.Embed(title="success", description=f"started private channel in <#{channel.id}>", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="you don't have access to zone!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="this command only works in zone", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)

@client.command()
async def close(ctx):
    if int(ctx.guild.id) == 980538576850804776:
        if int(ctx.author.id) in json.loads(open("access.json", "r").read()):
            for channel in ctx.guild.channels:
                if channel.name == str(ctx.author.id):
                    embed=discord.Embed(title="success", description=f"deleted <#{channel.id}>", color=000000)
                    embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
                    embed.set_footer(text=ctx.author.name)
                    await ctx.send(embed=embed)
                    time.sleep(1)
                    await channel.delete()
                    return
            embed=discord.Embed(title="error", description=f"couldn't find a priv channel", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="you don't have access to zone!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="this command only works in zone", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)
@client.command()
async def shelp(ctx):
    embed=discord.Embed(title="help", color=000000)
    embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
    embed.set_footer(text=ctx.author.name)
    embed.add_field(name=".leak", value="leakcheck cmds", inline=False)
    embed.add_field(name=".priv", value="priv cmds", inline=False)
    embed.add_field(name=".tt", value="tiktok user search", inline=False)
    embed.add_field(name=".shelp", value="all cmds", inline=False)
  
  
    await ctx.send(embed=embed)

@client.command()
async def priv(ctx):
    embed=discord.Embed(title="priv cmds", color=000000)
    embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
    embed.set_footer(text=ctx.author.name)
    embed.add_field(name=".start", value="create a priv channel", inline=True)
    embed.add_field(name=".close", value="close a priv channel", inline=True)
    await ctx.send(embed=embed)
@client.command()
async def leak(ctx):
    embed=discord.Embed(title="leakcheck cmds", color=000000)
    embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")

    embed.set_footer(text=ctx.author.name)
    embed.add_field(name=".e", value="leakcheck a email", inline=True)
    embed.add_field(name=".p", value="leakcheck a given user/name", inline=True)
    await ctx.send(embed=embed)


@client.command()
async def clear(ctx):
    if int(ctx.guild.id) == 946141223612207154:
        if int(ctx.author.id) in json.loads(open("admins.json", "r").read()):
            for channel in ctx.guild.channels:
                if len(channel.name) == 18 and channel.name.isdigit():
                    await channel.delete()
            embed=discord.Embed(title="success", description="cleared all priv channels!", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="error", description="you aren't an admin", color=000000)
            embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
            embed.set_footer(text=ctx.author.name)
            await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="error", description="this command only works in /ngf", color=000000)
        embed.set_author(name="zone", url="https://discord.gg/4cs", icon_url="https://i.pinimg.com/originals/1c/d2/00/1cd200b06a8ae254a8fa749d04121d58.pngg.com/originals/eb/01/15/eb011574e03abaa674e804eb2d5be0be.jpg")
        embed.set_footer(text=ctx.author.name)
        await ctx.send(embed=embed)






#----------------------------------------------------------------------------------------------------------------------------------------------------------


   
@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(f"```py\n{error_msg}```")

    


client.run("your token lol")

