import os
from tkinter import * 
from tkinter.messagebox import *

def create_bot():
    global nom
    global tokken
    if tokken.get()==None or tokken.get()=="Discord Bot Token ?" or nom.get()==None or nom.get()=="Discord Bot Name ?":
        showinfo("Echec", "Veuillez vérifie les informations saisies")
        return
    try:
        os.mkdir(f"./{nom.get()}")

        with open(f"./{nom.get()}/{nom.get()}.py","w") as f:
            f.write('''
import discord
import os
from discord.ext import commands

client = discord.Client()

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    print("Discord Bot has been launched")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
''')
            f.write(f"bot.run('{str(tokken.get())}')")

        os.mkdir(f"./{nom.get()}/cogs")

        with open(f"./{nom.get()}/cogs/first_cog.py","w") as f:
            f.write('''
import discord
import discord
from discord.embeds import EmptyEmbed
from discord.ext import commands

class FirstCog(commands.Cog, name='FirstCog'):
    def __init__(self, bot, **kwargs):
        self.bot = bot


    @commands.command(name="!ping")
    async def ping(self, ctx):
        embed = discord.Embed(title=f"PONG", description=f"Your first command", color=discord.Color.blue())
        embed.set_footer(text=f"Your first Discord Bot By <<Esteban>>#9789",icon_url="https://cdn.discordapp.com/avatars/384743597658079243/090917f54f563802757ab5243afab427.png?size=1024")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FirstCog(bot))
    ''')
    except:
        showinfo("Echec", "Veuillez vérifie les informations saisies")

fenetre = Tk()
fenetre.geometry("600x105")
fenetre.title("Discord Bot Creator by Esteban")
fenetre.configure(bg="grey14")

label = Label(fenetre, text="Discord Bot Creator",bg="grey14",fg="white")
label.pack()

nom = StringVar() 
nom.set("Discord Bot Name ?")
entree = Entry(fenetre, textvariable=nom, width=68,bg="grey")
entree.pack()

tokken = StringVar() 
tokken.set("Discord Bot Token ?")
entree2 = Entry(fenetre, textvariable=tokken, width=68,bg="grey")
entree2.pack()

bouton = Button(fenetre, text="Valider", command=create_bot,bg="green")
bouton.pack()

texte=Label(fenetre,text="Python Script by <<Esteban>>#9789",bg="grey14",fg="red")
texte.pack()

fenetre.mainloop()


