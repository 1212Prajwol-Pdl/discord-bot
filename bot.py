import discord 
from discord.ext import commands
import keys
from transformers import pipeline
import pickle

nlp_qa = pipeline('question-answering')

client = discord.Client()

@client.event
async def on_ready():
  print('bot activated {0.user}'.format (client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#context') :
        await message.channel.send("context received MOFO")
        context_temp = pickle.load(open('data/context.p','rb'))
        context_temp2 = message.content.split('#context',1)[1]
        context_merged = context_temp+context_temp2
        with open(f'data/context.p','wb') as f:
            pickle.dump(context_merged, f)

    if message.content.startswith('#question'):
        question = message.content.split('#question',1)[1]
        context=pickle.load(open('data/context.p','rb'))
        answer1 = nlp_qa(context=context, question=question)
        await message.channel.send(answer1["answer"])

client.run(keys.TOKEN)
