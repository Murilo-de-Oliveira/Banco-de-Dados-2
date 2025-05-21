import pprint
from database import Database

db = Database("bolt://18.208.163.76:7687", "neo4j", "dedication-hotels-visions")
#db.drop_all()

def questao_1_a(db: Database):
    query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc AS ano_nascimento, t.cpf AS cpf"
    result = db.execute_query(query, {"name": "Renzo"})
    for record in result:
        print(f'Ano de nascimento: {record["ano_nascimento"]} \nCPF: {record["cpf"]}')

def questao_1_b(db: Database):
    query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS nome, t.cpf AS cpf"
    result = db.execute_query(query,)
    for record in result:
        print(f'Nome: {record["nome"]} \nCPF: {record["cpf"]}')

def questao_1_c(db: Database):
    query = "MATCH (c:City) RETURN c.name AS nome"
    result = db.execute_query(query)
    for record in result:
        print(f'Cidade: {record["nome"]}')

def questao_1_d(db: Database):
    query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS nome, s.address AS endereço, s.number AS numero"
    result = db.execute_query(query)
    for record in result:
        print(f'Escola: {record["nome"]} \nEndereço: {record["endereço"]} \nNúmero: {record["numero"]}')

def questao_2_a(db: Database):
    query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS menor_idade, MIN(t.ano_nasc) AS maior_idade"
    result = db.execute_query(query)
    print(f'Professor mais jovem: {result[0]['menor_idade']} \nProfessor mais velho: {result[0]['maior_idade']}')

def questao_2_b(db: Database):
    query = "MATCH (c:City) RETURN AVG(c.population) AS media_populacao"
    result = db.execute_query(query)
    print(f'Média da população: {result[0]['media_populacao']:.2f} habitantes')

def questao_2_c(db: Database):
    query = "MATCH (c:City) WHERE (c.cep = '37540-000') RETURN REPLACE(c.name, 'a', 'A') AS nome_a"
    result = db.execute_query(query)
    print(f'Cidade com CEP 37540-000 e nome alterado: {result[0]['nome_a']}')

def questao_2_d(db: Database):
    query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS terceira_letra"
    result = db.execute_query(query)
    for record in result:
        print(f'Terceira letra do nome: {record['terceira_letra']}')

print('=== Questão 1 ===')
print('a)')
questao_1_a(db)
print('b)')
questao_1_b(db)
print('c)')
questao_1_c(db)
print('d)')
questao_1_d(db)

print('=== Questão 2 ===')
print('a)')
questao_2_a(db)
print('b)')
questao_2_b(db)
print('c)')
questao_2_c(db)
print('d)')
questao_2_d(db)