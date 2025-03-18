from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyser import ProductAnalyser

db = Database(database="mercado", collection="produtos")

verificador = ProductAnalyser(db)

vendas_por_dia = verificador.vendasPorDia()
writeAJson(vendas_por_dia, "vendas_totais_por_dia")

mais_vendido = verificador.maisVendido()
writeAJson(mais_vendido, "produtos_mais_vendidos")

maior_compra = verificador.maiorCompra()
writeAJson(maior_compra, "maior_compra")

comprado_maior_que_1 = verificador.comprasMaiorQueUm()
writeAJson(comprado_maior_que_1, "produtos_vendidos_acima_de_uma_unidade")