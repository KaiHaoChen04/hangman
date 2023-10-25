# Hangman Game
# Began on September 24, 2023
# Created by KaiHao Chen. I hold Copyright to the entirety of the project.

import pygame, math, time, random
import button

pygame.init()
screen_width = 950
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman")
images = [pygame.image.load(f"hangman{i}.jpg").convert() for i in range(8)]
resume = pygame.image.load("button_resume.png").convert()
resume_button = button.Button(600, 400, resume, 1)
font = pygame.font.Font('freesansbold.ttf', 32)
player1_text = font.render('Player 1', True, (0, 0, 128), (0, 255, 0))
player2_text = font.render('Player 2', True, (255, 0, 0), (0, 255, 0))
LIST_OF_WORDS = ["PYTHON", "UNIVERSITY", "HOUSE", "HANGMAN", "MINER", "SNACK", "MUSIC", "HEADPHONE", 
                 "COMPUTER","INTERNET", "CHOCOLATE", "MATHEMATICS", "SCIENCE", "PHYSICS", "PITBULL",
                 "NEIGHBORHOOD", "FEELING", "GRACEFUL"]
random_index = random.randint(0, len(LIST_OF_WORDS) - 1) 

def main():
    running = True
    paused = False
    wrong_guessed = 0
    type_box = pygame.Rect(150, 500, 60, 40)
    type_box2 = pygame.Rect(750, 500, 60, 40)
    text = ""
    text2 = ""
    guessed = []
    color = pygame.Color('white')
    clock = pygame.time.Clock() 
    image_index = 0
    image_timer = pygame.time.get_ticks()
    while running: 
        clock.tick(60)
        if paused:
            screen.blit(resume)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if type_box.collidepoint(event.pos):
                        typing = True
                        typing2 = False
                    elif type_box2.collidepoint(event.pos): 
                        typing2 = True
                        typing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                    if typing or typing2:
                        if typing:
                            if event.key == pygame.K_BACKSPACE or len(text) >= 1:
                                text = text[:-1]
                            else:
                                guessed_letter = event.unicode.upper()
                                if guessed_letter.isalpha():
                                    if guessed_letter not in LIST_OF_WORDS[random_index]:
                                        wrong_guessed += 1
                                        image_index = min(wrong_guessed, len(images) - 1)
                                    guessed.append(guessed_letter)
                                text += event.unicode.upper()
                        elif typing2:
                            if event.key == pygame.K_BACKSPACE or len(text2) >= 1:
                                text2 = text2[:-1]
                            else:
                                guessed_letter = event.unicode.upper()
                                if guessed_letter.isalpha():
                                    if guessed_letter not in LIST_OF_WORDS[random_index]:
                                        wrong_guessed += 1
                                        image_index = min(wrong_guessed, len(images) - 1)
                                    guessed.append(guessed_letter)
                                text2 = event.unicode.upper()
        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        txt_surface2 = font.render(text2, True, color)
        screen.blit(txt_surface, (type_box.x+5, type_box.y+5))
        screen.blit(txt_surface2, (type_box2.x+5, type_box2.y+5))
        pygame.draw.rect(screen, color, type_box, 2)    
        pygame.draw.rect(screen, color, type_box2, 2)    
        draw(image_index, text or text2, guessed)          
        pygame.display.update()      
    pygame.quit() 

def draw(id, input, guessed):
    WORD_FONT = pygame.font.SysFont('comicsans', 40)
    underscore_text = ""
    guessed.append(input)
    for word in LIST_OF_WORDS[random_index]:
        if word in guessed:
            underscore_text += word + " "
        else:
            underscore_text += "_ "
    text = WORD_FONT.render(underscore_text, 1, (255, 255, 255))
    screen.blit(text, (320, 550))
    screen.blit(player1_text, (20, 20))
    screen.blit(player2_text, (800, 20))
    screen.blit(images[id], (380, 50))

if __name__ == "__main__":
    main()