import pygame
import random
import copy
import time
import sys


#what i want in the bottom
#wpm
#accuracy
#streak
#issue with red and green text not working cuz first letter is not capitaled
#solution, change the font
#scroling text animation
#main menu
#maybe a pause
#add a input box
#highest wpm instead of best and score
#make exit button

pygame.init()

width, height = 1000,600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Typing game in Python!")
surface = pygame.Surface((width, height), pygame.SRCALPHA)
timer = pygame.time.Clock()
text = open('Python\Random\jamall.txt', "r").read().split("\n")
fps = 60
#game variables
wpm = 0
accuracy = 100
high_score = 0
streak = 0
#rng chooses text
# random.choice(text) 
current_text = "hi" 
typed_text = ''
start_time = None
clock=pygame.time.Clock()



def draw_screen():
  screen.fill('gray')
  pygame.draw.rect(screen, (32, 42, 68), [0, height - 100, width, 100], 0)
  pygame.draw.rect(screen, 'white', [0, 0, width, height], 5)
  pygame.draw.line(screen, 'white', (250, height - 100), (250, height), 2)
  pygame.draw.line(screen, 'white', (700, height - 100), (700, height), 2)
  pygame.draw.line(screen, 'white', (0, height - 100), (width, height - 100), 2)

  # Display stats
  screen.blit(header_font.render(f'WPM: {wpm}', True, 'white'), (10, height - 75))
  screen.blit(header_font.render(f'Accuracy: {accuracy}%', True, 'white'), (270, height - 75))
  screen.blit(banner_font.render(f'Score: {streak}', True, 'white'), (250, 10))
  screen.blit(banner_font.render(f'Best: {high_score}', True, 'white'), (550, 10))

  # Display text to type and user input
  screen.blit(font.render(current_text, True, 'white'), (50, 200))
  screen.blit(font.render(typed_text, True, 'green'), (50, 300))

#prevent text from going offscreen

#font
header_font = pygame.font.Font('Python\Random\Square.ttf', 50)
pause_font = pygame.font.Font('Python\Random\Square.ttf', 38)
banner_font = pygame.font.Font('Python\Random\Square.ttf', 28)
font = pygame.font.Font('Python\Random\RobotoMono-Light.ttf', 20)

def calculate_wpm(typed_text, start_time):
    if start_time is None:
        return 0
    elapsed_time = time.time() - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / elapsed_time) * 60
    return round(wpm)

run = True
while run:
  timer.tick(fps)
  draw_screen()
  if typed_text != current_text[0:len(typed_text)]:
      screen.blit(font.render(typed_text, True, 'red'), (50, 300))
  else:
      screen.blit(font.render(typed_text, True, 'green'), (50, 300))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
                run = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            if typed_text == current_text:
                streak += 1
                if streak > high_score:
                    high_score = streak
            else:
                streak = 0
            current_text = random.choice(text)
            typed_text = ""
            start_time = None
        elif event.key == pygame.K_BACKSPACE:
            typed_text = typed_text[:-1]
        else:
            if start_time is None:
                start_time = time.time()
            typed_text += event.unicode
    if typed_text == current_text:
        while True:
            # time_img = pygame.image.load('Python\Random\icon.png')
            # time_img = pygame.transform.scale(time_img, (150, 150))

            # #screen.blit(self.time_img, (80,320))
            # screen.blit(time_img, (width/2-75, height-140))
            # screen.blit(header_font.render(f'Reset:', True, 'white'), (width/2-90, height-140))
            button_surface = pygame.Surface((200, 50))

            # Render text on the button
            text = header_font.render("reset", True, (0, 0, 0))
            text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))


            # Create a pygame.Rect object that represents the button's boundaries
            button_rect = pygame.Rect(750, height - 75, 200, 50)  # Adjust the position as needed

            # Start the main loop
            while True:
            # Set the frame rate
                clock.tick(60)
            
            # Fill the display with color
            # screen.fill((155, 255, 155))

            # Get events from the event queue
                for event in pygame.event.get():
            # Check for the quit event
                   if event.type == pygame.QUIT:
            # Quit the game
                    pygame.quit()
                    sys.exit()

            # Check for the mouse button down event
                   if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
                     if button_rect.collidepoint(event.pos):
                         print("Button clicked!")

            # Check if the mouse is over the button. This will create the button hover effect
                   if button_rect.collidepoint(pygame.mouse.get_pos()):
                     pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
                   else:
                    pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
                    pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            
            
            
            # Shwo the button text
                button_surface.blit(text, text_rect)

            # Draw the button on the screen
                screen.blit(button_surface, (button_rect.x, button_rect.y))

            # Update the game state
                pygame.display.update()



    elif typed_text:
        wpm = calculate_wpm(typed_text, start_time)

        # accuracy = calculate_accuracy(typed_text, current_text)

  pygame.display.flip()


pygame.quit()



