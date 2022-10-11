import discord
from discord.ext import commands
from discord.flags import Intents
import asyncio
from random import choice, randint
from lista import lista
from datetime import datetime
from senha import token
from time import sleep
import os
from comandos import comandos_bot

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = ("{} bem vindo ao Servidor {}".format(member.mention, guild.name))
            await guild.system_channel.send(mensagem)    

    async def on_member_left(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = ("Aff, o {} é chato e acabou de sair do Servidor".format(member.mention))
            await guild.system_channel.send(mensagem)  

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content == '?oi' or message.content == '?ola' or message.content == '?salve' or message.content == '?aoba' or message.content == '?opa':
            await message.channel.send('Ola {}!'.format(message.author.name))

        elif message.content == '?sabedoria':
            await message.channel.send(choice(lista))

        elif message.content == "?bom dia" or message.content == "?dia":
            await message.channel.send('Bom dia {}!'.format(message.author.name))

        elif message.content == "?boa tarde" or message.content == "?tarde":
            await message.channel.send('Boa Tarde {}!'.format(message.author.name))

        elif message.content == "?boa noite" or message.content == "?noite":
            await message.channel.send('Boa Noite {}!'.format(message.author.name))

        elif message.content == "?boa madrugada" or message.content == "?madrugada":
            await message.channel.send('Boa Madrugada {}!'.format(message.author.name))

        elif message.content == "?data" or message.content == "?hora":
            now = datetime.now()
            data = now.strftime("%d/%m/%Y %H:%M:%S")
            await message.channel.send("Data e Hora Atual: {}".format(data))

        elif message.content == "?numero" or message.content == "?num":
            randnum = randint(1, 1000000)
            await message.channel.send("Seu numero é: {}".format(randnum))

        elif message.content == "?criador" or message.content == "?Calil":
            await message.channel.send("O Calil é brabo, ele é meu criador!")

        elif message.content == "?nome" or message.content == "?bot":
            await message.channel.send("Meu nome é Bob, o Bot")   

        elif message.content == "?cuidado":
            await message.author.send("Eu vou caçar você e toda sua familia...") 
            sleep(2.5)
            await message.author.send("Brincadeirinha, sou um Bot bonzinho :)") 

        elif message.content == "?roll":
            msg = await message.channel.send("Qual Dado?")

            def roll_dice(m):
                return m.author == message.author and m.content.isdigit()

            try:
                msg = await self.wait_for('message', check=roll_dice, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Operacão Cancelada devido a Demora')

            msg = int(msg.content)
            dado = randint(1, msg)
            await message.channel.send("Resultado D{}: {}".format(msg, dado))

        elif message.content == "?conte minutos" or message.content == "?minutos":
            minutos = await message.channel.send("Quantos Minutos?")

            def conta_tempo(t):
                return t.author == message.author and t.content.isdigit()  

            try:
                minutos = await self.wait_for('message', check=conta_tempo, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Operacão Cancelada devido a Demora') 

            minutos = int(minutos.content)
            await message.channel.send("Contando {} minuto(s) a partir de agora!".format(minutos))

            await asyncio.sleep(minutos*60)
            await message.channel.send("Ding Dong!! Já se passaram {} minuto(s)!".format(minutos))  
        
        elif message.content == "?conte segundos" or message.content == "?segundos":
            segundos = await message.channel.send("Quantos Segundos?")

            def conta_segundos(s):
                return s.author == message.author and s.content.isdigit()  

            try:
                segundos = await self.wait_for('message', check=conta_segundos, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Operacão Cancelada devido a Demora') 

            segundos = int(segundos.content)
            await message.channel.send("Contando {} segundos a partir de agora!".format(segundos))

            await asyncio.sleep(segundos)
            await message.channel.send("Ding Dong!! Já se passaram {} segundos!".format(segundos))  

        elif message.content == "?comando" or message.content == "?comandos":
            await message.channel.send(comandos_bot) 

intents = discord.Intents.all()
intents.members = True

client = MyClient(intents=intents)
client.run(token)