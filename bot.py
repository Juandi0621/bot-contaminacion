import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} está listo para combatir la contaminación!')

@client.event
async def on_member_join(member):
    await member.send(f"¡Hola {member.name}! Bienvenido al servidor. Aquí te dejo algunos consejos para prevenir la contaminación: \n\n"
                      "**Reduce, Reutiliza, Recicla:** Es el mantra clave. Reduce tu consumo, reutiliza los objetos antes de desecharlos y recicla todo lo que puedas. \n\n"
                      "**Elige transporte sostenible:** Camina, anda en bicicleta o usa el transporte público siempre que sea posible. Si necesitas usar un coche, elige uno eléctrico o híbrido. \n\n"
                      "**Ahorra energía:** Apaga las luces cuando no las necesites, desconecta los aparatos electrónicos cuando no los uses y utiliza bombillas LED. \n\n"
                      "**Consume productos ecológicos:** Busca productos que sean respetuosos con el medio ambiente y que no contengan sustancias tóxicas. \n\n"
                      "**Reduce el consumo de agua:** Toma duchas cortas, reutiliza el agua de lluvia y arregla cualquier fuga que tengas. \n\n"
                      "¡Juntos podemos hacer la diferencia! 😄")

client.run('')
