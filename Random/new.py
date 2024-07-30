import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Typing game in Python!")
timer = pygame.time.Clock()
fps = 60

# Load texts


# Game variables
wpm = 0
text = open('Python\Random\jamall.txt', "r").read().split("\n")
accuracy = 100
streak = 0
high_score = 0
current_text = random.choice(text)
typed_text = ""
start_time = None
running = True

# Fonts
header_font = pygame.font.Font('Python\Random\Square.ttf', 50)
pause_font = pygame.font.Font('Python\Random\Square.ttf', 38)
banner_font = pygame.font.Font('Python\Random\Square.ttf', 28)
font = pygame.font.Font('Python\Random\Square.ttf', 48)

def calculate_wpm(typed_text, start_time):
    if start_time is None:
        return 0
    elapsed_time = time.time() - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / elapsed_time) * 60
    return round(wpm)

def calculate_accuracy(typed_text, current_text):
    matches = sum(1 for i, c in enumerate(typed_text) if i < len(current_text) and c == current_text[i])
    accuracy = matches / len(current_text) if len(current_text) > 0 else 0
    return round(accuracy * 100, 2)

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

while running:
    timer.tick(fps)
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if start_time is None:
                start_time = time.time()
            
            if event.key == pygame.K_RETURN:
                if typed_text == current_text:
                    streak += 1
                    if streak > high_score:
                        high_score = streak
                else:
                    streak = 0
                current_text = random.choice(current_text)
                typed_text = ""
                start_time = None
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            else:
                typed_text += event.unicode
    
    if typed_text:
        wpm = calculate_wpm(typed_text, start_time)
        accuracy = calculate_accuracy(typed_text, current_text)

    pygame.display.flip()

pygame.quit()
