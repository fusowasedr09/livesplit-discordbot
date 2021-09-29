import discord, subprocess, socket
token="ここにアクセストークンを入れる"
client = discord.Client()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

@client.event
async def on_ready():
    s.connect(("localhost", 16834))
    print("ログインしました")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!start":
        s.send(b"starttimer\r\n")
        await message.channel.send("タイマースタート！")
    if message.content == "!split":
        s.send(b"split\r\n")
        await message.channel.send("次の区間に進みます")
    if message.content == "!reset":
        s.send(b"reset\r\n")
        await message.channel.send("タイマーをリセットしました")
    if message.content == "!pause":
        s.send(b"pause\r\n")
        await message.channel.send("タイマーを一時停止しました")
    if message.content == "!resume":
        s.send(b"resume\r\n")
        await message.channel.send("タイマーを再開します")
    if message.content == "!back":
        s.send(b"unsplit\r\n")
        await message.channel.send("前の区間に戻します")

client.run(token)
