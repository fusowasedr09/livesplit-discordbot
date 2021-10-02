import discord, subprocess, socket
from discord.ext import commands 

bot = commands.Bot(command_prefix="/") # 起動コマンドの先頭記号を変えたい時はcommand_prefixの""内を変更
token="ここに自分のbotのトークンを入力"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 16834)) # 自身のポート番号に合わせる（デフォルト:16834）

@bot.event
async def on_ready():
    print("we have logged in as {0}".format(bot.user))

@bot.command()
@commands.has_role("Timekeeper") # 別のロール名称を使いたいときはここを変更（他のコマンドも同様）
async def start(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"starttimer\r\n")
    await ctx.send("タイマーをスタートします") # ""内を変えると送信メッセージが変わる
# 関数名を変えるとコマンド名称が変わる,権限内場合はエラーメッセ

@bot.command()
@commands.has_role("Timekeeper")
async def split(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"split\r\n")
    await ctx.send("次のスプリットに進みます")

@bot.command()
@commands.has_role("Timekeeper")
async def reset(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"reset\r\n")
    await ctx.send("タイマーをリセットします")

@bot.command()
@commands.has_role("Timekeeper")
async def pause(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"pause\r\n")
    await ctx.send("タイマーを一時停止します")

@bot.command()
@commands.has_role("Timekeeper")
async def resume(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"resume\r\n")
    await ctx.send("タイマーを再開します")

@bot.command()
@commands.has_role("Timekeeper")
async def back(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"unsplit\r\n")
    await ctx.send("前の区間に戻します")

@bot.command()
@commands.has_role("Timekeeper")
async def skip(ctx):
    if ctx.author == bot.user:
        return
    s.send(b"skipsplit\r\n")
    await ctx.send("この区間を飛ばします")

bot.run(token)
