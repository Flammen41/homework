from game.game.image.open import open_image
from game.game.sound.play import play_sound

def start_game():
    print('Starting game')

def main():
    start_game()
    open_image()
    play_sound()

if __name__ == '__main__':
    main()