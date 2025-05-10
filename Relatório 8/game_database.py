import uuid

class GameDatabase():
    def __init__(self, db):
        self.db = db

    def _generate_id(self):
        return str(uuid.uuid4())

    # === MÉTODOS DO JOGADOR ===

    def create_player(self, name):
        player_id = self._generate_id()
        query = "CREATE (:Player {id: $id, name: $name})"
        self.db.execute_query(query, {"id": player_id, "name": name})
        return player_id

    def get_player(self, name):
        query = "MATCH (p:Player {name: $name}) RETURN p.id AS id, p.name AS name"
        result = self.db.execute_query(query, {"name": name})
        return [record.data() for record in result]

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $id}) SET p.name = $new_name"
        self.db.execute_query(query, {"id": player_id, "new_name": new_name})

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $id}) DETACH DELETE p"
        self.db.execute_query(query, {"id": player_id})

    def list_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        result = self.db.execute_query(query)
        return [record.data() for record in result]

    # === MÉTODOS DA PARTIDA ===

    def create_match(self, players: list[tuple[str, int]]):
        match_id = self._generate_id()

        # Cria o nó da partida
        query = "CREATE (:Match {id: $id})"
        self.db.execute_query(query, {"id": match_id})

        winner = ""
        winner_score = 0

        for player_name, player_score in players:
            query = """
            MATCH (p:Player {name: $name}), (m:Match {id: $id})
            CREATE (p)-[:PARTICIPATED_IN {score: $score}]->(m)
            """
            parameters = {
                "name": player_name,
                "id": match_id,
                "score": player_score
            }
            self.db.execute_query(query, parameters)

            if player_score > winner_score:
                winner_score = player_score
                winner = player_name

        self.update_match_winner(match_id, winner)
        return match_id

    def update_match_winner(self, match_id, winner):
        query = "MATCH (m:Match {id: $id}) SET m.winner = $winner"
        self.db.execute_query(query, {"id": match_id, "winner": winner})

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $id}) DETACH DELETE m"
        self.db.execute_query(query, {"id": match_id})
    
    def list_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS id"
        result = self.db.execute_query(query)
        return [record.data() for record in result]

    def get_match(self, match_id):
        # Recupera o vencedor
        query = "MATCH (m:Match {id: $id}) RETURN m.winner AS winner"
        winner_result = self.db.execute_query(query, {"id": match_id})
        winner = winner_result[0].data()['winner'] if winner_result else None

        # Recupera os participantes e suas pontuações
        query = """
        MATCH (m:Match {id: $id})<-[P:PARTICIPATED_IN]-(p:Player)
        RETURN p.name AS player, P.score AS score
        """
        results = self.db.execute_query(query, {"id": match_id})

        match = {
            "id": match_id,
            "winner": winner,
            "players_score": [
                {result["player"]: result["score"]} for result in [r.data() for r in results]
            ]
        }
        return match

    def get_player_history(self, player_id):
        query = """
        MATCH (p:Player {id: $id})-[P:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS match_ID,
               m.winner AS match_winner,
               CASE WHEN m.winner = p.name THEN true ELSE false END AS is_winner,
               P.score AS score
        """
        result = self.db.execute_query(query, {"id": player_id})
        return [record.data() for record in result]