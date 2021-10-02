import discord, subprocess, socket
from discord.ext import commands 

bot = commands.Bot(command_prefix="!") # 起動コマンドの先頭記号を変えたい時はcommand_prefixの""内を変更
token="ここに自分のbotのトークンを入力"
s.connect(("localhost", 16834)) # livesplit.serverのポート番号に合わせる（デフォルト:16834）
user_role = "Timekeeper" # コマンドを使用できる権限を変えたい時はここの""内を変更

@bot.event
async def on_ready():
    print("we have logged in as {0}".format(bot.user))

@bot.command()
@commands.has_role(user_role) 
async def start(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"starttimer\r\n")
    await ctx.send("タイマーをスタートします") # ""内を変えると送信メッセージが変わる（他も同様）

@bot.command()
@commands.has_role(user_role)
async def split(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"split\r\n")
    await ctx.send("次のスプリットに進みます")

@bot.command()
@commands.has_role(user_role)
async def reset(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"reset\r\n")
    await ctx.send("タイマーをリセットします")

@bot.command()
@commands.has_role(user_role)
async def pause(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"pause\r\n")
    await ctx.send("タイマーを一時停止します")

@bot.command()
@commands.has_role(user_role)
async def resume(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"resume\r\n")
    await ctx.send("タイマーを再開します")

@bot.command()
@commands.has_role(user_role)
async def back(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"unsplit\r\n")
    await ctx.send("前の区間に戻します")

@bot.command()
@commands.has_role(user_role)
async def skip(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"skipsplit\r\n")
    await ctx.send("この区間を飛ばします")

bot.run(token)
