import redis
import pickle
import json


def get_connection():
    return redis.Redis()

#criar a base de dados
class RedisClient:

    def __init__(self, connection):
        """Initialize client."""
        self.r = connection

    def set(self, key, value, **kwargs):
        """Store a value in Redis."""
        return self.r.set(key, pickle.dumps(value), **kwargs)

    def set_initial(self, key, value):
        """Store a value in Redis."""
        if not self.get(key):
            self.set(key, value)

    def get(self, key):
        """Retrieve a value from Redis."""
        val = self.r.get(key)
        if val:
            return pickle.loads(val)
        return None

    def dump(self, keys, filename):
        data = {}
        for k in keys:
            data[k] = self.get(k)
        print("storing configuration: %s" % json.dumps(data, indent=2))
        with open(filename, "w") as fp:
            json.dump(data, fp, indent=2)

    def load(self, filename):
        data = {}
        with open(filename) as fp:
            data = json.load(fp)
        print("configuration loaded: %s" % json.dumps(data, indent=2))
        for k in data:
            self.set(k, data[k])


#variaveis de controlo que vem do telefone
class LittleBerryConfig:
    def  __init__(self, connection):
        self.client = RedisClient(connection)
        self.client.set_initial("animacaoInativo", 404)




    @property
    def intensidadeDosLeds(self):
        return self.client.get("intensidadeDosLeds")
    @intensidadeDosLeds.setter
    def intensidadeDosLeds(self, value):
        self.client.set("intensidadeDosLeds", value)


    @property
    def cor(self):
        return self.client.get("cor")
    @cor.setter
    def cor(self, value):
        self.client.set("cor", value)


    @property
    def horasDoAlarme1(self):
        return self.client.get("horasDoAlarme1")
    @horasDoAlarme1.setter
    def horasDoAlarme1(self, value):
        self.client.set("horasDoAlarme1", value)

    
    @property
    def nomeDoAlarme1(self):
        return self.client.get("nomeDoAlarme1")
    @nomeDoAlarme1.setter
    def nomeDoAlarme1(self, value):
        self.client.set("nomeDoAlarme1", value)


    @property
    def somDoAlarme1(self):
        return self.client.get("somDoAlarme1")
    @somDoAlarme1.setter
    def somDoAlarme1(self, value):
        self.client.set("somDoAlarme1", value)


    @property
    def estiloDosLeds1(self):
        return self.client.get("estiloDosLeds1")
    @estiloDosLeds1.setter
    def estiloDosLeds1(self, value):
        self.client.set("estiloDosLeds1", value)


    @property
    def horasDoAlarme2(self):
        return self.client.get("horasDoAlarme2")
    @horasDoAlarme2.setter
    def horasDoAlarme2(self, value):
        self.client.set("horasDoAlarme2", value)


    @property
    def nomeDoAlarme2(self):
        return self.client.get("nomeDoAlarme2")
    @nomeDoAlarme2.setter
    def nomeDoAlarme2(self, value):
        self.client.set("nomeDoAlarme2", value)


    @property
    def somDoAlarme2(self):
        return self.client.get("somDoAlarme2")
    @somDoAlarme2.setter
    def somDoAlarme2(self, value):
        self.client.set("somDoAlarme2", value)


    @property
    def estiloDosLeds2(self):
        return self.client.get("estiloDosLeds2")
    @estiloDosLeds2.setter
    def estiloDosLeds2(self, value):
        self.client.set("estiloDosLeds2", value)


    @property
    def horasDoAlarme3(self):
        return self.client.get("horasDoAlarme3")
    @horasDoAlarme3.setter
    def horasDoAlarme3(self, value):
        self.client.set("horasDoAlarme3", value)


    @property
    def nomeDoAlarme3(self):
        return self.client.get("nomeDoAlarme3")
    @nomeDoAlarme3.setter
    def nomeDoAlarme3(self, value):
        self.client.set("nomeDoAlarme3", value)


    @property
    def somDoAlarme3(self):
        return self.client.get("somDoAlarme3")
    @somDoAlarme3.setter
    def somDoAlarme3(self, value):
        self.client.set("somDoAlarme3", value)


    @property
    def estiloDosLeds3(self):
        return self.client.get("estiloDosLeds3")
    @estiloDosLeds3.setter
    def estiloDosLeds3(self, value):
        self.client.set("estiloDosLeds3", value)

    
    @property
    def chamada(self):
        return self.client.get("chamada")
    @chamada.setter
    def chamada(self, value):
        self.client.set("chamada", value)


    @property
    def nomeDaChamada(self):
        return self.client.get("nomeDaChamada")
    @nomeDaChamada.setter
    def nomeDaChamada(self, value):
        self.client.set("nomeDaChamada", value)


    @property
    def somDoToque(self):
        return self.client.get("somDoToque")
    @somDoToque.setter
    def somDoToque(self, value):
        self.client.set("somDoToque", value)


    @property
    def estiloDosLeds(self):
        return self.client.get("estiloDosLeds")
    @estiloDosLeds.setter
    def estiloDosLeds(self, value):
        self.client.set("estiloDosLeds", value)


    @property
    def notificacao(self):
        return self.client.get("notificacao")
    @notificacao.setter
    def notificacao(self, value):
        self.client.set("notificacao", value)


    @property
    def nomeDaNotificacao(self):
        return self.client.get("nomeDaNotificacao")
    @nomeDaNotificacao.setter
    def nomeDaNotificacao(self, value):
        self.client.set("nomeDaNotificacao", value)


    @property
    def conteudo(self):
        return self.client.get("conteudo")
    @conteudo.setter
    def conteudo(self, value):
        self.client.set("conteudo", value)

    
    @property
    def somDoToqueNotificacao(self):
        return self.client.get("somDoToqueNotificacao")
    @somDoToqueNotificacao.setter
    def somDoToqueNotificacao(self, value):
        self.client.set("somDoToqueNotificacao", value)


    @property
    def estiloDosLedsNotificacao(self):
        return self.client.get("estiloDosLedsNotificacao")
    @estiloDosLedsNotificacao.setter
    def estiloDosLedsNotificacao(self, value):
        self.client.set("estiloDosLedsNotificacao", value)
    
    @property
    def animacaoInativo(self):
        return self.client.get("animacaoInativo")
    @animacaoInativo.setter
    def animacaoInativo(self, value):
        self.client.set("animacaoInativo", value)



#variaveis de controlo que são controladas pelo main e tem impacto nos restantes processos
class LittleBerryControl:
    def  __init__(self, connection):
        self.client = RedisClient(connection)
        self.client.set_initial("CONTROLloopLeds", 1)

    #leds
    @property
    def CONTROLloopLeds(self):
        return self.client.get("CONTROLloopLeds")
    @CONTROLloopLeds.setter
    def CONTROLloopLeds(self, value):
        self.client.set("CONTROLloopLeds", value)

    @property
    def CONTROLanimacaoLeds(self):
        return self.client.get("CONTROLanimacaoLeds")
    @CONTROLanimacaoLeds.setter
    def CONTROLanimacaoLeds(self, value):
        self.client.set("CONTROLanimacaoLeds", value)



    #Camera
    @property
    def CONTROLloopCamera(self):
        return self.client.get("CONTROLloopCamera")
    @CONTROLloopCamera.setter
    def CONTROLloopCamera(self, value):
        self.client.set("CONTROLloopCamera", value)


     #servo
    @property
    def CONTROLservoDireita(self):
        return self.client.get("CONTROLservoDireita")
    @CONTROLservoDireita.setter
    def CONTROLservoDireita(self, value):
        self.client.set("CONTROLservoDireita", value)

    @property
    def CONTROLservoEsquerda(self):
        return self.client.get("CONTROLservoEsquerda")
    @CONTROLservoEsquerda.setter
    def CONTROLservoEsquerda(self, value):
        self.client.set("CONTROLservoEsquerda", value)

    @property
    def CONTROLservoMeio(self):
        return self.client.get("CONTROLservoMeio")
    @CONTROLservoMeio.setter
    def CONTROLservoMeio(self, value):
        self.client.set("CONTROLservoMeio", value)

    #Player
    @property
    def CONTROLplayvideo(self):
        return self.client.get("CONTROLplayvideo")
    @CONTROLplayvideo.setter
    def CONTROLplayvideo(self, value):
        self.client.set("CONTROLplayvideo", value)

    @property
    def ERRORplayVide(self):
        return self.client.get("ERRORplayVide")
    @ERRORplayVide.setter
    def ERRORplayVide(self, value):
        self.client.set("ERRORplayVide", value)


    @property
    def FATALERRORplayVideo(self):
        return self.client.get("FATALERRORplayVideo")
    @FATALERRORplayVideo.setter
    def FATALERRORplayVideo(self, value):
        self.client.set("FATALERRORplayVideo", value)




