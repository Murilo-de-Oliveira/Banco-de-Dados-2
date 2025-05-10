import pprint
from database import Database
from game_database import GameDatabase

db = Database("bolt://54.164.58.184:7687", "neo4j", "peace-miners-trays")
db.drop_all()

game_database = GameDatabase(db)

game_database.create_player("Jogador A")
game_database.create_player("Jogador B")

game_database.create_match([("Jogador A", 10), ("Jogador B", 20)])

pprint.pprint(game_database.list_matches())

match_id = game_database.list_matches()[0]["id"]
pprint.pprint(game_database.get_match(match_id))

player_id = game_database.get_player("Jogador A")[0]["id"]
pprint.pprint(game_database.get_player_history(player_id))

db.close()




