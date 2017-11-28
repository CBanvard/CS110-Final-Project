import pygame
import collection
import hand
import player
import table
import tests
import os, sys

height = 1000
width = 1000

#globalconstants (sorry for using globalspace, but i think this is most effective)

black = (250,250,250)
black = (0,0,0)
grey = (50,50,50)
red = (200,0,0)

class Initial:
	def __init__(self):
		deck = collection.Deck()
		self.images = {}
self.scale = .5
self.cardSize = (width / 6, width / 5)
self.Lctn = (insertbackgroundhere) #i need to find a background image
self.cardBack1 = #need to find cardbacks
self.cardBack2 = #maybe these two can be colin and melanie

font = pygame.font.Font(‘font/Arial’, 50) #font recommendations?
loadText = font.render(“Loading!”, 1, black)
loadSize = font.size(“Loading!)
loadBack = (width / 2 - loadSize[0] /2, height/2 - loadSize[0] / 2)

screen.blit(self.Lctn, (-300, 100))
screen.blit(loadText, loadBack)

pygame.display.flip()

def main(self):
#options menu (1,2,3,4 for the different keys)
	if self.state  == 0:
		self.start_up()
	elif self.state == 1:
		self.play()
	elif self.state == 2:
		self.results()
	elif self.state == 3:
		self.new_game()

def first_init(self): [will work on this part ™] 
#menu graphics

self.font = 
self.font.bold()
	
self.startText  = 
self.startSize = 
self.startLctn = 

self.startButton
self.buttonSize
self.buttonLctn

self.buttonRect
self.buttonRectOutline

self.state = 0

