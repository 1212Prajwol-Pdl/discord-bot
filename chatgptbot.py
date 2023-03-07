'''
using chatgpt api to generate output for discord bot.
'''
import openai
import discord
from keys import chatgptkey
import keys


openai.api_key = chatgptkey
client = discord.Client()

@client.event
async def on_ready():
    print('bot activated {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('#question'):
        question = message.content.split('#question', 1)[1]   
        output = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[{"role":"user",
                        "content":question}]
        )
        await message.channel.send(output['choices'][0]['message']['content'])


client.run(keys.TOKEN)