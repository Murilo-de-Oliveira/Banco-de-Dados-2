from pymongo import MongoClient
from bson.objectid import ObjectId

class BookModel:
    # Construtor da classe bookModel
    def __init__(self, database):
        self.db = database

    # Função que adiciona um livro ao BD
    def create_book(self, title: str, author: str, year: int, price: float):
        try:
            res = self.db.collection.insert_one({"titulo": title, "autor": author, "ano": year, "preco": price})
            print(f"Livro criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao inserir o livro: {e}")
            return None

    # Função que busca um livro no BD usando seu ID
    def read_book_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao encontrar um livro: {e}")
            return None

    # Função que atualiza um livro no BD, o critério de busca é seu ID
    def update_book(self, id: str, title: str, author: str, year: int, price: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": title, "autor": author, "ano": year, "preco": price}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    # Função que deleta um livro no BD, o critério de busca é seu ID
    def delete_book(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None