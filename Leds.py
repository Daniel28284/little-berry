import time
import board
import neopixel


class neoPixels:
	def __init__(self):
		
		#Os Neopixels apenas funcionam se ligados ao pinos D10, D12, D18 or D21, porque sao os unicos que tem PWM
		#sao os pinos gpio 
		self.pixel_pin = board.D18

		# O numero de pixel que a fita tem
		self.num_pixels = 72

		# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed
		self.ORDER = neopixel.RGB

		#onde diz o brightness define a intensidade maxima dos leds
		intensidadeDosLeds=db.intensidadeDosLeds
		self.pixels = neopixel.NeoPixel(
			self.pixel_pin, self.num_pixels, brightness= intensidadeDosLeds, auto_write=False, pixel_order=self.ORDER
		)

	#faz parte do efeito de andar a roda multicor
	def wheel(self, pos):
		# Input a value 0 to 255 to get a color value.
		# The colours are a transition r - g - b - back to r.
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

	# efeito de andar a roda multicor
	def rainbow_cycle(self, wait):
		for j in range(255):
			for i in range(self.num_pixels):
				pixel_index = (i * 256 // self.num_pixels) + j
				self.pixels[i] = self.wheel(pixel_index & 255)
			self.pixels.show()
			time.sleep(wait)

	#efeito limpar que começa de uma lado e vai acendedo os leds com delay e as cores que podem ser passadas
	def limpar(self, r,g,b,delay):
		'''
		r,g,b : RGB compoennets 0-255; delay: seconds
		'''
		for i in range(self.num_pixels):
			self.pixels[i] = (r, g, b)
			self.pixels.show()
			time.sleep(delay)
		

	#mover 1 led a volta da fita
	#verificar o for acho que tem o i+1 a toa 
	def mover_led(self, delay,red,green,blue):
		for i in range(self.num_pixels):
			self.pixels[i]=(red,green,blue)
			self.pixels.show()
			time.sleep(delay)
		
			self.pixels[i-1]=(0,0,0)
			self.pixels[i]=(0,0,0)
			self.pixels.show()
			
			i=i+1


	def main():
		while True:
			loop=db.loopLeds
			while loop:
				if db.PresetSorrir == True:
					sorrir()
				elif db.animationToPlay == 1:
					triste()

				
				




			
	

			

	
		


if __name__ == "__main__":
	leds = neoPixels()
	print("SOU O LITTLEB ERRY NO RASPBERRY")
	leds.limpar(0,0,255, 0.5)
    