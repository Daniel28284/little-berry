import BaseDados

import BaseDados
conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)



print(configdb.cor)
print(configdb.intensidadeDosLeds)
print(configdb.animacaoInativo)
print(controldb.CONTROLanimacaoLeds)