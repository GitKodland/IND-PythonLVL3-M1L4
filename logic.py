import aiohttp  # Pustaka untuk request HTTP secara asinkron
import random

class Pokemon:
    pokemons = {}
    # Inisialisasi objek (konstruktor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # Metode asinkron untuk mendapatkan nama pokémon melalui PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API untuk request
        async with aiohttp.ClientSession() as session:  # Membuka sesi HTTP
            async with session.get(url) as response:  # Mengirim request GET
                if response.status == 200:
                    data = await response.json()  # Menerima dan mendekode respons JSON
                    return data['forms'][0]['name']  # Mengembalikan nama pokémon
                else:
                    return "Pikachu"  # Mengembalikan nama default jika permintaan gagal

    async def info(self):
        # Metode yang mengembalikan informasi tentang pokémon
        if not self.name:
            self.name = await self.get_name()  # Mengambil nama jika belum diunggah
        return f"Nama Pokémon Anda: {self.name}"  # Mengembalikan string dengan nama pokémon

    async def show_img(self):
        # Metode asinkron untuk mengambil URL gambar pokémon melalui PokeAPI
