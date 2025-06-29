# ~/display/pygame_display.py
import pygame
from display.display import BaseScreen

class PygameScreen(BaseScreen):
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((320, 240))
        pygame.display.set_caption("Pokedex Display")
        self.font_cache = {}

    def clear(self):
        self.surface.fill((0, 0, 0))

    def draw_image(self, path, position):
        image = pygame.image.load(path)
        self.surface.blit(image, position)

    def draw_text(self, text, position, size=16, color=(255, 255, 255)):
        if size not in self.font_cache:
            self.font_cache[size] = pygame.font.SysFont(None, size)
        font = self.font_cache[size]
        text_surface = font.render(text, True, color)
        self.surface.blit(text_surface, position)

    def update(self):
        pygame.display.flip()