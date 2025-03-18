from database import Database

class ProductAnalyser:
    def __init__(self, db):
        self.collection = db.collection
    
    #Retorna o total de vendas por dia
    def vendasPorDia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$data_compra",
                    "total_vendas": {
                        "$sum": {
                            "$multiply": ["$produtos.quantidade", "$produtos.preco",]
                        }
                    },
                }
            },
            {"$sort": {"_id": 1}},
        ]
        result = list(
            self.collection.aggregate(pipeline)
        )
        return result
    
    #Retorna o produto mais vendido
    def maisVendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total": {"$sum": "$produtos.quantidade"}
                }
            },
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = list(
            self.collection.aggregate(pipeline)
        )
        return result
    
    #Retorne o cliente que mais comprou produtos
    def maiorCompra(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$cliente_id", 
                    "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
                }
            },
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = list(
            self.collection.aggregate(pipeline)
        )
        return result
    
    # Retorna as compras que foram maiores que uma unidade
    def comprasMaiorQueUm(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {
                "$group": {
                    "_id": "$produtos.descricao", 
                    "total_vendido": {"$sum": "$produtos.quantidade"}
                }
            },
            {"$match": {"total_vendido": {"$gt": 1}}},
            {"$sort": {"total": -1}}, 
        ]
        result = list(
            self.collection.aggregate(pipeline)
        )
        return result
    