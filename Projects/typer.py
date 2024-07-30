import pygame
import random
import copy
import time
import threading
import random

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Typing game in Python!")
surface = pygame.Surface((width, height), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60

def draw_screen():
  pygame.draw.rect(screen,(32,42,68),[0, height - 100, width, 100], 0)
  pygame.draw.rect(screen,'white',[0,0,width,height],5)
  pygame.draw.line(screen,'white',(250,height-100),(250,height),2)
run = True
while run:
  screen.fill('gray')
  timer.tick(fps)
  draw_screen()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.flip()
pygame.quit()



