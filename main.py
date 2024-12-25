import discord
from discord.ext import commands
from config import token
from logic import Pokemon

# Mengatur intents untuk bot
intents = discord.Intents.default()  # Mendapatkan pengaturan default
intents.messages = True              # Memungkinkan bot untuk memproses pesan
intents.message_content = True       # Memungkinkan bot untuk membaca konten pesan
intents.guilds = True                # Memungkinkan bot untuk bekerja dengan server (guilds)

# Membuat bot dengan prefix perintah yang telah ditentukan dan intents yang diaktifkan
bot = commands.Bot(command_prefix='!', intents=intents)

# Event yang dijalankan ketika bot siap untuk dijalankan
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Menampilkan nama bot ke konsol

# Perintah '!go'
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mendapatkan nama pengirim pesan
    # Check whether the user already has a Pokémon. If not, then...
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)  # Membuat Pokémon baru
        await ctx.send(await pokemon.info())  # Mengirim informasi tentang Pokémon
        image_url = await pokemon.show_img()  # Mendapatkan URL gambar Pokémon
        if image_url:
            embed = discord.Embed()  # Membuat pesan embed
            embed.set_image(url=image_url)  # Mengatur gambar Pokémon
            await ctx.send(embed=embed)  # Mengirim pesan embed dengan gambar
        else:
            await ctx.send("Gagal mengunggah gambar Pokémon.")
    else:
        await ctx.send("Anda sudah memiliki Pokémon sendiri.")  # Pesan yang ditampilkan jika Pokémon sudah dibuat
# Menjalankan bot
bot.run(token)
