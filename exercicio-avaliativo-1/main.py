from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="exercicio_avaliativo_1", collection="Motorista")

motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)

motoristaCLI.run()