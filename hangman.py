import pygame
import random
pygame.init()

# Set up the game window
window = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Hangman Game')

# Load hangman images for each stage of the game (0 to 6 incorrect guesses)
hangman_images = [pygame.image.load(f'images/hangman{i}.png') for i in range(0,7)]

# Initialize font for rendering text
font = pygame.font.Font(None, 74)

# Initialize number of errors (wrong guesses)
errors = 0

# List of words to guess from
words_list = [
    "python","hangman", "programming","algorithm","function",
    "variable","exception","inheritance","polymorphism","encapsulation",
    "abstraction","recursion","iteration","syntax","debugging",
    "compilation","interpreter","framework","library","module"
]

# Function to randomly pick a word from the list
def pick_word():
    return random.choice(words_list)

# Class to handle word operations and display
class Word:
    def __init__(self, word):
        self.word = word  # The word to be guessed
        self.guessed_letters = []  # Letters that have been guessed

    # Display the word with guessed letters revealed and others as blanks
    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + "  "
            else:
                display += '__ '
        text = font.render(display, True, (0, 0, 0))
        window.blit(text, (0, 400))  # Display word in the window

    # Display the wrong letters that were guessed
    def display_wrong_letters(self):
        display = ''
        for letter in self.guessed_letters:
            if letter not in self.word:
                display += letter + ' '
        text = font.render(display, True, (0, 0, 0))
        window.blit(text, (0, 500))  # Display wrong guesses at the bottom

    # Check if the game is over (word fully guessed)
    def Game_over(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + "  "
            else:
                display += '__ '
        if "__" not in display:
            return True  # Game over if no blanks are left
        return False

# Class to handle hangman operations (counting errors and drawing)
class Hangman:
    def __init__(self, word):
        self.word = word
        self.errors = 0  # Start with 0 errors

    # Increase error count if guessed letter is not in the word
    def Count_errors(self, letter):
        if letter not in self.word:
            self.errors += 1

    # Check if the game is over (hangman fully drawn after 6 errors)
    def game_over(self):
        if self.errors == 6:
            return True
        else:
            return False

    # Display the current hangman image based on errors
    def display_hangman(self):
        window.blit(hangman_images[self.errors], (50, 50))

# Main game loop
run = True
wrd = Word(pick_word())
hangman = Hangman(wrd.word)
score = 0
while run:
    window.fill((255, 255, 255))  # Clear screen
    text = font.render(str(score), True, (0, 0, 0))
    window.blit(text, (350, 0))
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
        wrd = Word(pick_word())
        hangman = Hangman(wrd.word)
    elif wrd.Game_over():
        wrd = Word(pick_word())
        hangman = Hangman(wrd.word)
        score += 1
    pygame.display.update()
