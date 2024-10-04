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

class Word:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        
    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += '_'
        return display
    
class Hangman:
    def __init__(self, word):
        self.word = word
        self.errors = 0
        
    def Count_errors(self, letter):
        if letter not in self.word:
            self.errors += 1

    def game_over(self):
        if self.errors == 6:
            return True
        else:
            return False
        
    def display_hangman(self):
        window.blit(hangman_images[self.errors], (50, 50))

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

# Main game loop
run = True
guessed_letters = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    pygame.display.update()