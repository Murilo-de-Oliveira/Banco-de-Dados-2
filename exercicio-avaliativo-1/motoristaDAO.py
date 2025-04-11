from bson.objectid import ObjectId
from motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database
    
    def criar_motorista(self, motorista: Motorista):
        documento = motorista.to_dict()
        try:
            res = self.db.collection.insert_one(documento)
            print(f"Motorista com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao inserir o motorista: {e}")
            return None
    
    def buscar_motorista(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado:")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao encontrar o motorista: {e}")
            return None
        
    def atualizar_motorista(self, motorista_id, motorista):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": motorista})
            print(f"Motorista alterado: {res.modified_count} documento(s) alterado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao alterar o motorista: {e}")
            return None
    
    def deletar_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None
    