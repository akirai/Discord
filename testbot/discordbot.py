import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('おはよう'):
        # 送り主がBotだった場合反応しない
        if client.user != message.author:
            # メッセージを書く
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送る
            await client.send_message(message.channel, m)
    elif message.content.startswith('こんばんは'):
        if client.user != message.author:
            m = "こんばんは" + message.author.name + "さん！"
            await client.send_message(message.channel, m)

client.run("NDU2NDI0MjE2NjMyMjI5ODk5.DgKWXQ.gXLEuZ5dNi587jZYl709UECzVIQ")