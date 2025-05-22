from database import Database

class TeacherCrud:
    def __init__(self, db: Database):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        result = self.db.execute_query(query, {'name': name, 'ano_nasc': ano_nasc, 'cpf': cpf})
        if result is not None:
            print(f'O professor {name} foi criado no banco de dados')

    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS nome, t.cpf AS cpf, t.ano_nasc AS ano_nasc"
        result = self.db.execute_query(query, {'name': name})
        return result
    
    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        result = self.db.execute_query(query, {'name': name, 'newCpf': newCpf})
        if result is not None:
            print(f'O professor {name} foi alterado, novo cpf: {newCpf}')

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        result = self.db.execute_query(query, {'name': name})
        if result is not None:
            print(f'O professor {name} foi deletado do banco de dados')
