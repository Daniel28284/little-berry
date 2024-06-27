import BaseDados

import BaseDados



#classe para testes na base de dados

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)



print(configdb.cor)
#print(configdb.intensidadeDosLeds)
print(configdb.animacaoInativo)
#print(controldb.CONTROLanimacaoLeds)


configdb.animacaoInativo=12
configdb.cor=0



print(controldb.CONTROLplayvideo)
controldb.CONTROLplayvideo=int(1)





