import discord 
from discord.ext import commands
import keys
from transformers import pipeline

#


nlp_qa = pipeline('question-answering')

client = discord.Client()

@client.event
async def on_ready():
  print('activated {0.user}'.format (client))

context="The son of a civil servant, Turing was educated at a top private school.Death is the permanent, irreversible cessation of all biological functions that sustain a living organism.To put it simply, plain text is any text that isn’t formatted. It does not take any special formatting, such as varying fonts, font sizes, bold font, or italics. It also only contains standard characters, which are those found in the default set of characters that an application can display. It can also refer to a document that only contains these unformatted characters.Plain text files are often made by the most basic text file format, which takes on the “.txt” extension. These files are often created and edited by Notepad, the text editor found on every Windows device, or by another text editor. However, text files can be opened by virtually any document or text editor, including more powerful applications such as Notepad++, Wordpad, Microsoft Office, or OpenOffice."

@client.event
async def on_message(message):
  if message.author == client.user:
   return

  if message.content.startswith('#bot'):
      question= message.content.split('#bot',1)[1]
      answer1=nlp_qa(context=context, question=question)
      await message.channel.send(answer1["answer"])



client.run(keys.TOKEN)


