import pygame
import random
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hangman Game')

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