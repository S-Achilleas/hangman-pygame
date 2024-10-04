import pygame
import random
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman Game')
hangman_images = [pygame.image.load(f'images/hangman{i}.png') for i in range(0,7)]
errors = 0

words_list = [
    "python",
    "hangman",
    "programming",
    "algorithm",
    "function",
    "variable",
    "exception",
    "inheritance",
    "polymorphism",
    "encapsulation",
    "abstraction",
    "recursion",
    "iteration",
    "syntax",
    "debugging",
    "compilation",
    "interpreter",
    "framework",
    "library",
    "module"
]

def pick_word():
    return random.choice(words_list)

def add_letter(guessed_letters):
    while True:
        letter = input('Enter a letter: ').lower()
        if len(letter) != 1:
            print('Please enter a single letter.')
        elif letter in guessed_letters:
            print('You have already guessed that letter.')
        elif not letter.isalpha():
            print('Please enter a letter.')
        else:
            return letter
        
def display_hangman(errors):
    window.blit(hangman_images[errors], (50, 50))
    pygame.display.update()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    pygame.display.update()