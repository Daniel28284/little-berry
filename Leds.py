import time
import board
import neopixel
import BaseDados
import random
import numpy as np
import os

conn = BaseDados.get_connection()
configdb = BaseDados.LittleBerryConfig(conn) 
controldb = BaseDados.LittleBerryControl(conn)


# Classe responsável pelo contolo dos leds
# Esta classe é executada em segundo plano e vai recebendo ordens da classs main
# Class com processos sensíveis: Sim extrema preucpação porque caso ocorra algum erro pode induzir os leds a consumir 3A (a fonte de alimentação não aguenta) 
# Proteção contra erros: Sim a todos os niveis com shutdown em caso extremos
# Nível de Recursos utilizados: Medio a Alto
class neoPixels:
    def __init__(self):
        
        #Os Neopixels apenas funcionam se ligados ao pinos D10, D12, D18 or D21, porque sao os unicos que tem PWM
        #sao os pinos gpio 
        self.pixel_pin = board.D12
        # O numero de pixel que a fita tem
        self.num_pixels = 50
        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed
        self.ORDER = neopixel.GRB
        #onde diz o brightness define a intensidade maxima dos leds
        
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness= configdb.intensidadeDosLeds, auto_write=False, pixel_order=self.ORDER
        )

        

    # Parte do efeito de roda multicor
    def wheel(self, pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    # Efeito de roda multicor
    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)

    # Efeito que move um LED ao longo da fita
    def mover_led(self, red, green, blue, delay):
        for i in range(self.num_pixels):
            self.pixels[i] = (red, green, blue)
            self.pixels.show()
            time.sleep(delay)
            self.pixels[i - 1] = (0, 0, 0)
            self.pixels[i] = (0, 0, 0)
            self.pixels.show()

    # Efeito de limpar que vai acendendo os LEDs ao longo da fita
    def color_wipe(self, color, wait):
        for i in range(self.num_pixels):
            self.pixels[i] = color
            self.pixels.show()
            time.sleep(wait)

    # Cria um efeito de luzes intermitentes em grupos, movendo-se de forma alternada
    def theater_chase(self, color, wait, loop):
        for j in range(10):  # Repetir 10 vezes
            for q in range(3):
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = color
                self.pixels.show()
                time.sleep(wait)
                for i in range(0, self.num_pixels, 3):
                    self.pixels[i + q] = (0, 0, 0)
        if loop == False:
            for l in range(self.num_pixels):
                self.pixels[l] = (0, 0, 0)
                self.pixels.show()

    # Efeito que faz a fita piscar
    def blink(self, color, wait):
        for _ in range(5):
            for i in range(self.num_pixels):
                self.pixels[i] = color
            self.pixels.show()
            time.sleep(wait)
            for i in range(self.num_pixels):
                self.pixels[i] = (0, 0, 0)
            self.pixels.show()
            time.sleep(wait)

    # Efeito parecido com o piscar, mas que vai desvanecendo e acendendo proporcionalmente
    def fade(self, color, wait, wait2):
        for j in range(0, 256, 5):
            for i in range(self.num_pixels):
                self.pixels[i] = (int(color[0] * (j / 255.0)),
                                  int(color[1] * (j / 255.0)),
                                  int(color[2] * (j / 255.0)))
            self.pixels.show()
            time.sleep(wait)
        time.sleep(wait2)
        for j in range(255, -1, -5):
            for i in range(self.num_pixels):
                self.pixels[i] = (int(color[0] * (j / 255.0)),
                                  int(color[1] * (j / 255.0)),
                                  int(color[2] * (j / 255.0)))
            self.pixels.show()
            time.sleep(wait)

    # Função que acende 10 LEDs na frente do robô com o propósito de iluminar
    def luz(self, loop):
        pixel3 = int(self.num_pixels / 2)
        pixelleft = pixel3 - 5
        pixelright = pixel3 + 5
        
        pixelstodo = np.arange(pixelleft, pixelright)
        for i in range(15,25):
            self.pixels[i] = (255, 255, 255)
        
        self.pixels.show()

        if loop == False:
            for l in range(self.num_pixels):
                self.pixels[l] = (0, 0, 0)
                self.pixels.show()

    # Efeito noite estrelada, acendendo e apagando LEDs aleatórios para parecer uma noite estrelada
    def sparkle(self, color, wait, loop):
        for _ in range(1):
            pixel = random.randint(0, self.num_pixels - 1)
            self.pixels[pixel] = color
            self.pixels[random.randint(0, self.num_pixels - 1)] = color
            self.pixels[random.randint(0, self.num_pixels - 1)] = color
            self.pixels.show()
            time.sleep(wait)
            self.pixels[pixel] = (0, 0, 0)
            self.pixels.show()
        
        if loop == False:
            for l in range(self.num_pixels):
                self.pixels[l] = (0, 0, 0)
                self.pixels.show()

    # Efeito que acende um número de LEDs e estes se deslocam ao longo da fita
    def chaser(self, color, size, wait):
        for i in range(self.num_pixels + size):
            for j in range(size):
                if i - j < self.num_pixels and i - j >= 0:
                    self.pixels[i - j] = color
            self.pixels.show()
            time.sleep(wait)
            for j in range(size):
                if i - j < self.num_pixels and i - j >= 0:
                    self.pixels[i - j] = (0, 0, 0)

    # Parecido com o efeito chaser, mas os últimos LEDs (cauda) têm uma luz mais fraca, parecendo um cometa ou uma estrela cadente
    def comet(self, color, tail_length, wait):
        for i in range(self.num_pixels + tail_length):
            for j in range(tail_length):
                if i - j < self.num_pixels and i - j >= 0:
                    brightness = 1.0 - (j / float(tail_length))
                    self.pixels[i - j] = (int(color[0] * brightness), int(color[1] * brightness), int(color[2] * brightness))
            self.pixels.show()
            time.sleep(wait)
            for j in range(tail_length):
                if i - j < self.num_pixels and i - j >= 0:
                    self.pixels[i - j] = (0, 0, 0)

    # Método executado infinitamente e tem o propósito de reconhecer alterações feitas pela class main na variável de controle e atuar os LEDs
    def main(self):
        try:
            cores = ((100, 0, 200), (0, 0, 255), (255, 0, 0))  # (roxo, azul, vermelho)
            delay = 0.1
            atual = 0

            while True:    
                vez1 = True

                if atual != controldb.CONTROLanimacaoLeds:
                    print("mudou os leds")
                    while controldb.CONTROLloopLeds or vez1:
                        vez1 = False
                    
                        if controldb.CONTROLanimacaoLeds == 2:
                            self.mover_led(cores[configdb.cor], delay)
                            atual = 2
                        elif controldb.CONTROLanimacaoLeds == 3:
                            self.color_wipe(cores[configdb.cor], 0.1)
                            atual = 3
                        elif controldb.CONTROLanimacaoLeds == 4:
                            self.theater_chase(cores[configdb.cor], 0.1, controldb.CONTROLloopLeds)
                            atual = 4
                        elif controldb.CONTROLanimacaoLeds == 5:
                            self.blink(cores[configdb.cor], 0.3)
                            atual = 5
                        elif controldb.CONTROLanimacaoLeds == 6:
                            self.fade(cores[configdb.cor], 0.01, 2)
                            atual = 6
                        elif controldb.CONTROLanimacaoLeds == 7:
                            self.fade(cores[configdb.cor], 0.01, 0)
                            atual = 7
                        elif controldb.CONTROLanimacaoLeds == 8:
                            self.luz(controldb.CONTROLloopLeds)
                            atual = 8
                        elif controldb.CONTROLanimacaoLeds == 9:
                            self.sparkle(cores[configdb.cor], 0.01, controldb.CONTROLloopLeds)
                            atual = 9
                        elif controldb.CONTROLanimacaoLeds == 10:
                            self.chaser(cores[configdb.cor], 10, 0.1)
                            atual = 10
                        elif controldb.CONTROLanimacaoLeds == 11:
                            self.chaser(cores[configdb.cor], 10, 0.01)
                            atual = 11
                        elif controldb.CONTROLanimacaoLeds == 12:
                            self.comet(cores[configdb.cor], 10, 0.1)
                            atual = 12
                        elif controldb.CONTROLanimacaoLeds == 404:
                            self.fade(cores[2], 0.01, 0)
                            atual = 404
        except:
            print("erro FATAL nos leds, a desligar o robot")
            for l in range(self.num_pixels):
                self.pixels[l] = (0, 0, 0)
                self.pixels.show()
            

if __name__ == "__main__":
    leds = neoPixels()
    leds.main()
    
