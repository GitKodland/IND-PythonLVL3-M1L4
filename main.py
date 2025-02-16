import discord
from discord.ext import commands
from config import token
from logic import Pokemon

# Pengaturan intents untuk bot
intents = discord.Intents.default()  # Mendapatkan pengaturan default
intents.messages = True              # Mengizinkan bot untuk memproses pesan
intents.message_content = True       # Mengizinkan bot untuk membaca isi pesan
intents.guilds = True                # Mengizinkan bot untuk bekerja dengan server (guilds)

# Membuat bot dengan prefix command dan intents yang telah diatur
bot = commands.Bot(command_prefix='!', intents=intents)

# Event yang terpicu ketika bot siap bekerja
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Menampilkan nama bot di console

# Command '!go'
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mendapatkan nama pengirim pesan
    # Memeriksa apakah pengguna sudah memiliki pokemon
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)  # Membuat pokemon baru
        await ctx.send(await pokemon.info())  # Mengirim informasi pokemon
        image_url = await pokemon.show_img()  # Mendapatkan URL gambar pokemon
        if image_url:
            embed = discord.Embed()  # Membuat pesan embed
            embed.set_image(url=image_url)  # Mengatur gambar pokemon
            await ctx.send(embed=embed)  # Mengirim pesan embed dengan gambar
        else:
            await ctx.send("Tidak dapat memuat gambar pokemon.")
    else:
        await ctx.send("Kamu sudah memiliki pokemon.")  # Pesan jika pokemon sudah dibuat

# Menjalankan bot
bot.run(token)
