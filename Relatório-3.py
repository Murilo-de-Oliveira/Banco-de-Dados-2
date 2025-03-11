from database import Database
from helper.writeAJson import writeAJson

class pokedex:
    def __init__(self, database: Database):
        self.database = database

    # Lista de pokemons em ordem alfabética
    def listPokemons(self):
        pokemons = self.database.collection.find().sort("name", 1)

        writeAJson(pokemons, 'lista_pokemons')

        return pokemons
    
    # Busca de um pokemon específico
    def getPokemonByName(self, name: str):
        pokemons = self.database.collection.find({"name": name})

        writeAJson(pokemons, 'pokemon_por_nome')

        return pokemons
    
    # Busca pokemons de tipos específicos
    def getPokemonsByType(self, types: list):
        pokemons = self.database.collection.find({"type": {"$in": types}})

        writeAJson(pokemons, 'lista_pokemons_por_tipo')

        return pokemons
    
    # Lista as chances de spawn de cada pokemon
    def getSpawnChance(self):
        pokemons = self.database.collection.find({},{"name": 1,"spawn_chance": 1, "_id":0})

        writeAJson(pokemons, 'chances_de_spawn')

        return pokemons
    
    # Lista de pokemons que não possuem evolução
    def getNotEvolutions(self):
        query = {"$or": [{"next_evolution": {"$exists": False}}, {"next_evolution": {"$size": 0}}]}

        pokemons = self.database.collection.find(query)

        writeAJson(pokemons, 'pokemons_sem_evolucao')

        return pokemons


db = Database(database="pokedex", collection="pokemons")

minha_pokedex = pokedex(db)

pokemons = minha_pokedex.listPokemons()
pokemon = minha_pokedex.getPokemonByName('Pikachu')
pokemons_tipos = minha_pokedex.getPokemonsByType(['Poison','Ice'])
pokemons_spawn_chance = minha_pokedex.getSpawnChance()
pokemons_sem_evolucao = minha_pokedex.getNotEvolutions()
