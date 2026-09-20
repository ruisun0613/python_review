"""
12-5. Keys: Make a Pygame file that creates an empty screen. In the event
loop, print the event.key attribute whenever a pygame.KEYDOWN event is
detected. Run the program and press various keys to see how Pygame
responds.
"""

import pygame

class Key:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (1200, 800)
        )

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key, pygame.key.name(event.key))
            
    def run_key(self):
        while True:
            self.__check_events()

if __name__ == '__main__':
    test = Key()
    test.run_key()