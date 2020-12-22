import pygame

def draw_ui(screen):
	# Menu
	tag_list = {
		'Red': (189, 43, 43), 
		'Pink': (204, 65, 130), 
		'Purple': (92, 45, 125), 
		'Blue':(61, 85, 173), 
		'Green': (101, 189, 64), 
		'Yellow': (232, 227, 65), 
		'Orange': (227, 119, 48)
	}
	i = 0
	global button_list
	button_list = []
	for cle, val in tag_list.items():
		button_list.append(pygame.draw.rect(screen, val, (45+100*i, 25, 60, 35)))
		pygame.draw.rect(screen, (0, 0, 0), (45+100*i, 25, 60, 35), width=3)
		screen.blit(FONT.render(cle , 1, (255, 255, 255)), (48+100*i, 30))
		i += 1

	# gradient's zone
	pygame.draw.rect(screen, (255, 255, 255), (22, 80, 705, 392), width=5)

	# RGB values
	screen.blit(FONT.render('RGB Values :', 1, (255, 255, 255)), (50, 520))
	for i in range(3):
		pygame.draw.rect(screen, (255, 255, 255), (50+75*i, 550, 50, 35))
		pygame.draw.rect(screen, (0, 0, 0), (50+75*i, 550, 50, 35), width=3)
		screen.blit(FONT.render(str(COLOR[i]) , 1, (0, 0, 0)), (60+75*i, 560))

	# Current color
	screen.blit(FONT.render('Current color :', 1, (255, 255, 255)), (320, 520))
	global current_color_rect
	current_color_rect = pygame.draw.rect(screen, COLOR, (320, 550, 150, 60))
	pygame.draw.rect(screen, (0, 0, 0), (320, 550, 150, 60), width=3)

	# Hex value
	screen.blit(FONT.render('Hex Value :', 1, (255, 255, 255)), (550, 520))
	pygame.draw.rect(screen, (255, 255, 255), (550, 550, 100, 35))
	pygame.draw.rect(screen, (0, 0, 0), (550, 550, 100, 35), width=3)
	screen.blit(FONT.render('#'+str(rgb_to_hex(COLOR[:-1])) , 1, (0, 0, 0)), (560, 560))

	# COPY - PASTE
	pygame.draw.line(screen, (255, 255, 255), (175, 630), (700, 630))
	screen.blit(FONT.render('Paste colors :', 1, (255, 255, 255)), (50, 620))
	global square_list
	square_list = []
	for i in range(6):
		square_list.append(pygame.draw.rect(screen, PALET[i], (50+115*i, 650, 75, 75)))
		pygame.draw.rect(screen, (0, 0, 0), (50+115*i, 650, 75, 75), width=3)

def draw_gradient(screen, color):
	# Load gradient
	gradient = pygame.image.load('gradients/'+color+'.png')
	
	# Set gradient position
	global gradient_rect
	gradient_rect = gradient.get_rect()
	gradient_rect.x, gradient_rect.y = 22, 80

	# Draw gradient
	screen.blit(gradient, gradient_rect)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Color picker with Python   --   Version : 1.0')

BACKGROUND = (22, 45, 53)
FONT = pygame.font.Font(None, 25)
COLOR = (255, 255, 255, 255)
PALET = [(255, 255, 255) for i in range(6)]
GRADIENT_LIST = ['red', 'pink', 'purple', 'blue', 'green', 'yellow', 'orange']
current_gradient = 'red'

while 1:
	screen.fill(BACKGROUND)

	draw_gradient(screen, current_gradient)
	draw_ui(screen)

	pygame.display.flip()

	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			if gradient_rect.collidepoint(ev.pos):
				paste_mode = True
				COLOR = screen.get_at(ev.pos)
			if current_color_rect.collidepoint(ev.pos):
					paste_mode = False
					COLOR = (0, 0, 0, 255)
			for i in range(len(square_list)):
				if square_list[i].collidepoint(ev.pos):
					if paste_mode:	
						PALET[i] = COLOR
					else:
						COLOR = screen.get_at(ev.pos)
			for i in range(len(button_list)):
				if button_list[i].collidepoint(ev.pos):
					current_gradient = GRADIENT_LIST[i]
