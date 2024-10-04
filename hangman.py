import pygame
import random
pygame.init()

window = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Hangman Game')
hangman_images = [pygame.image.load(f'images/hangman{i}.png') for i in range(0,7)]
font = pygame.font.Font(None, 74)
errors = 0

words_list = [
"python","hangman", "programming","algorithm","function",
"variable","exception","inheritance","polymorphism","encapsulation",
"abstraction","recursion","iteration","syntax","debugging",
"compilation","interpreter","framework","library","module"]

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
                display += letter + "  "
            else:
                display += '__ '
        text = font.render(display, True, (0, 0, 0))
        window.blit(text, (0, 400))
    
    def display_wrong_letters(self):
        display = ''
        for letter in self.guessed_letters:
            if letter not in self.word:
                display += letter + ' '
        text = font.render(display, True, (0, 0, 0))
        window.blit(text, (0, 500))
    
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

# Main game loop
run = True
wrd = Word(pick_word())
hangman = Hangman(wrd.word)
while run:
    window.fill((255, 255, 255))  # Clear screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():  # Only handle alphabetic characters
                letter = event.unicode.lower()
                if letter not in wrd.guessed_letters:
                    wrd.guessed_letters.append(letter)
                    hangman.Count_errors(letter)  # Update errors if necessary

    # Display hangman, guessed word, and wrong letters
    wrd.display_word()
    wrd.display_wrong_letters()
    hangman.display_hangman()

    # Check for game over
    if hangman.game_over():
        print("Game Over! The word was:", wrd.word)
        run = False

    pygame.display.update()
