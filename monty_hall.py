import pygame as pygame
import random
pygame.init()
white = (255, 255, 255)
X = 900
Y = 650 
a = random.sample(range(1, 4), 3)
goat1 = a[0]
goat2 = a[1]
goats = [goat1, goat2]
car = a[2]
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Image')
image = pygame.image.load('door_bg.png')
change = False
msg_disp = False 
def music():
	file = 	'click.mp3'
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play(-1)
def show_car(car, state):
	my_font = pygame.font.SysFont("latoblack", 26)
	display_surface = pygame.display.set_mode((900, 650))
	car1 = pygame.image.load('car1.jpg') 
	car2 = pygame.image.load('car2.jpg') 
	car3 = pygame.image.load('car3.jpg') 

	if car == 1:
		display_surface.blit(car1, (0, 0))
		pygame.display.update()
	elif car == 2:
		display_surface.blit(car2, (0, 0))
		pygame.display.update()
	elif car == 3:
		display_surface.blit(car3, (0, 0))
		pygame.display.update()
	if state == 1:
		the_text = my_font.render("You won by switching!", True, (231, 0, 10))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 2:
		the_text = my_font.render("You could've won by switching!", True, (231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 3:
		the_text = my_font.render("You won by staying!", True, (231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 4:
		the_text = my_font.render("You could've won by staying!", True, (231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
def draw_rect():
	pygame.draw.rect(display_surface, (20,24,11), (300, 220, 300, 40), 1)
	pygame.display.update()
	pygame.draw.rect(display_surface, (14, 2, 200), (300, 260, 300, 40), 1)
	pygame.display.update()		


while True: 
	music()
	if change == False:
		display_surface.fill(white)
		display_surface.blit(image, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		# if event.type == pygame.MOUSEBUTTONDOWN:
		#  	print(u"Down button pressed in the position {}".format(event.button, event.pos))
		pygame.display.update()
		# if event.type == pygame.MOUSEMOTION:
		# 	print(event.pos)
		clicked = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if(event.pos[0] >= 71 and event.pos[0] <= 203 and event.pos[1] >= 387 and event.pos[1] <= 632): #Check if door 1 is pressed.
				user = 1
				clicked = True
				music()
			elif(event.pos[0] >= 353 and event.pos[0] <= 485 and event.pos[1] >= 386 and event.pos[1] <= 635): #Check if door 2 is pressed.
				user = 2
				clicked = True
				music()
			elif(event.pos[0] >= 638 and event.pos[0] <= 765 and event.pos[1] >= 387 and event.pos[1] <= 633): #Check if door 3 is pressed. 
				user = 3
				#print("Clicked on door 3.")
				clicked = True
				music()
		if clicked:
			# if(user == car):	
			# 	print("You won!")
			# else:
			image1 = pygame.image.load('goat1.jpg')
			image2 = pygame.image.load('goat2.jpg')
			image3 = pygame.image.load('goat3mod.jpg')
			image4 = pygame.image.load('car1.jpg')
			image5 = pygame.image.load('car2.jpg')
			image6 = pygame.image.load('car3.jpg')
			wr = random.randint(0, 1)
			if(goats[0] == user):
				g = goats[1]
			elif(goats[1] == user):
				g = goats[0]
			else:
				g = goats[wr]
			if g == 1:
				change = True 
				display_surface.blit(image1, (0, 0))
				pygame.display.update()
			elif g == 2:
				change = True
				display_surface.blit(image2, (0, 0))
				pygame.display.update()
			elif g == 3:
				change = True 
				display_surface.blit(image3, (0, 0))
				pygame.display.update()
			print(u"There is a goat behind door {}".format(g))
		# clicked2 = False 
		# choice = int(input("\t1.Stay\n\t2.Switch"))
		# if(choice2 == 1):
			my_font = pygame.font.SysFont("mvboli", 26)
			the_text = my_font.render("Do you want to:", True, (231, 0, 0))
			display_surface.blit(the_text, (350, 180))
			the_text2 = my_font.render("1.Switch", True, (0, 0, 190))
			display_surface.blit(the_text2, (350, 220))
			the_text3 = my_font.render("2.Stay", True, (190, 0, 0))
			display_surface.blit(the_text3, (350, 260))
			draw_rect()
			clicked2 = False
			print(u"The car is behind door {}".format(car))

	# for event in pygame.event.get():
		clicked2 = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if(event.pos[0] >= 299 and event.pos[0] <= 597 and event.pos[1] >= 220 and event.pos[1] <= 260):
				user2 = 1
				clicked2 = True
			elif(event.pos[0] >= 301 and event.pos[0] <= 598 and event.pos[1] >= 259 and event.pos[1] <= 297):
				user2 = 2
				clicked2 = True
			# if(event.pos[0] >= 71 and event.pos[0] <= 203 and event.pos[1] >= 387 and event.pos[1] <= 632): #Check if door 1 is pressed.
			# 	user2 = 1
			# 	clicked2 = True
			# elif(event.pos[0] >= 353 and event.pos[0] <= 485 and event.pos[1] >= 386 and event.pos[1] <= 635): #Check if door 2 is pressed.
			# 	user2 = 2
			# 	clicked2 = True
			# elif(event.pos[0] >= 638 and event.pos[0] <= 765 and event.pos[1] >= 387 and event.pos[1] <= 633): #Check if door 3 is pressed. 
			# 	user2 = 3
			# 	clicked2 = True
		if clicked2:
			
			if user2 == 1:
				print("You chose to switch!")
				if user in goats:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text = my_font.render("You won by switching!", True, (231, 0, 0))
					state = 1
					display_surface.blit(the_text, (350, 180))
					pygame.display.update()
					print("You won by switching!") 		
				elif user == car:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text2 = my_font.render("You could've won by switching!", True, (231, 0, 0))
					state = 2
					display_surface.blit(the_text2, (350, 180))
					pygame.display.update()
					print("You could have won by switching!")
			elif user2 == 2:
				print("You chose to stay!")
				if user == car:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text3 = my_font.render("You won by staying!", True, (231, 0, 0))
					display_surface.blit(the_text3, (350, 180))
					state = 3
					pygame.display.update()
					print("You won by staying!")
				else:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text4 = my_font.render("You could've won by staying!", True, (231, 0, 0))
					display_surface.blit(the_text4, (350, 180))
					state = 4
					pygame.display.update()
					print("You could have won by staying!")
			show_car(car, state)
	
		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	if(event.pos[0] <= 597 and event.pos[0] >= 299 and event.pos[1] <= 260 and event.pos[1] >= 220):
		# 		print("You chose to switch!")
		# 		break
		# 	elif(event.pos[0] <= 598 and event.pos[0] >= 301 and event.pos[1] <= 297 and event.pos[1] >= 259):
		# 		print("You chose to stay!")
		# 		break

			#pygame.display.update()
		# if event.type == pygame.MOUSEMOTION:
		# 	print(u"Pressed button {} and position {}".format(event.buttons, event.pos)) 
		# if clicked2:
		# 	if user2 == car: 
		# 		print("You by switching!")
		# 	elif user == user2 == car:
		# 		print("You won by staying!")
		# 	elif user2 != car and user == car:
		# 		print("You could have won by staying!")
		# 	elif user2 == car and user != car:
		# 		print("You won by switching!")
			# if user2 == 1:
			# 	print("Your final choice is door 1.")
			# elif user2 == 2:
			# 	print("Your final choice is door 2.")
			# elif user2 == 3:
			# 	print("Your final choice is door 3.")
	# pygame.draw.rect(display_surface, (20,24,11), (300, 220, 300, 40), 1)
	# pygame.display.update()
	# pygame.draw.rect(display_surface, (14, 2, 200), (300, 260, 300, 40), 1)
	

			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	if(event.pos[0] >= 300 and event.pos[0] <= 600 and event.pos[1] >= 220 and event.pos[1] <= 260):
			# 		print("You chose to s")	
			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	if(event.pos[0] >= 350 and event.pos[0] <= 441 and event.pos[1] >= 231 and event.pos[1] <= 232):
			# 		sw = 1
			# 		msg_disp = True
			# 	elif(event.pos[0] >= 354 and event.pos[0] <= 411 and event.pos[1] >= 267 and event.pos[1] <= 270):
			# 		sw = 2
			# 		msg_disp = True
			# if msg_disp:
			# 	if sw == 1:
			# 		print("You clicked on switch.")
			# 	elif sw == 2:
			# 		print("You clicked on stay.")
	
			# def stay():
			# 	if user == car:
			# 		print("You won by staying!")
			# 	else:
			# 		print("You could have won by staying!")
			# def switch():
			# 	if user != car:
			# 		print("You won by switching!")
			# 	else:
			# 		print("You could've won by staying!")
			# ch = int(input("1. Stay\n 2.Switch\n"))
			# if(ch == 1):
			# 	if(user == car):
			# 		print("You won by staying!")
			# else:
			# 	if(user != car):
			# 		print("You won by switching!")

		# if event.type == pygame.MOUSEMOTION:
		# 	print(u"Up button pressed in the position {}".format(event.pos))
			# if event.type == pygame.MOUSEMOTION:
			# 	print(u"Pressed button {} and position {}".format(event.buttons, event.pos))

