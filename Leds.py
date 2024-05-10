class neoPixels():
	#Os Neopixels apenas funcionam se ligados ao pinos D10, D12, D18 or D21, porque sao os unicos que tem PWM
	pixel_pin = board.D18

	# O numero de pixel que a fita tem
	num_pixels = 72

	# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed
	ORDER = neopixel.RGB
	
	#onde diz o brightness define a intensidade maxima dos leds
	pixels = neopixel.NeoPixel(
		pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
	)

	#faz parte do efeito de andar a roda multicor
	def wheel(pos):
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
		return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

	# efeito de andar a roda multicor
	def rainbow_cycle(wait):
		for j in range(255):
			for i in range(num_pixels):
				pixel_index = (i * 256 // num_pixels) + j
				pixels[i] = wheel(pixel_index & 255)
			pixels.show()
			time.sleep(wait)

	#efeito limpar que começa de uma lado e vai acendedo os leds com delay e as cores que podem ser passadas
	def limpar(r,g,b,delay):
		for i in range(num_pixels):
			pixels[i] = (r, g, b)
			pixels.show()
			time.sleep(delay)
			
			
		
		
	#mover 1 led a volta da fita
	#verificar o for acho que tem o i+1 a toa 
	def mover_led(delay,red,green,blue):
		for i in range(num_pixels):
			pixels[i]=(red,green,blue)
			pixels.show()
			time.sleep(delay)
		
			pixels[i-1]=(0,0,0)
			pixels[i]=(0,0,0)
			pixels.show()
			
			i=i+1
	

			

	
		


if __name__ == "__main__":
    print("SOU O LITTLEB ERRY NO RASPBERRY")
    