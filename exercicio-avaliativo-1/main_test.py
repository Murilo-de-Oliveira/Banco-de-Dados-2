from motorista import Motorista
import pprint

motorista = Motorista.obter_dados_motorista()
dicionario_motorista = motorista.to_dict()
pprint.pprint(dicionario_motorista)