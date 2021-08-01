import discord 
from discord.ext import commands
import keys

from transformers import pipeline

nlp_qa = pipeline('question-answering')

client = discord.Client()
context = """
Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. Unqualified, the word football normally means the form of football that is the most popular where the word is used. Sports commonly called football include association football (known as soccer in some countries); gridiron football (specifically American football or Canadian football); Australian rules football; rugby football (either rugby union or rugby league); and Gaelic football.[1][2] These various forms of football share to varying extent common origins and are known as football codes.

There are a number of references to traditional, ancient, or prehistoric ball games played in many different parts of the world.[3][4][5] Contemporary codes of football can be traced back to the codification of these games at English public schools during the 19th century.[6][7] The expansion and cultural influence of the British Empire allowed these rules of football to spread to areas of British influence outside the directly controlled Empire.[8] By the end of the 19th century, distinct regional codes were already developing: Gaelic football, for example, deliberately incorporated the rules of local traditional football games in order to maintain their heritage.[9] In 1888, The Football League was founded in England, becoming the first of many professional football competitions. During the 20th century, several of the various kinds of football grew to become some of the most popular team sports in the world.[10] 
"""

@client.event
async def on_ready():
  print('boom boom roboto,mai hu {0.user}'.format (client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
     return

    if message.content.startswith('#hello'):
      answer1=nlp_qa(context=context, question='what is football')
      await message.channel.send(answer1["answer"])



client.run(keys.TOKEN)


