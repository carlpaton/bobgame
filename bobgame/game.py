import pygame

from .player import Bob
from .settings import BG_COLOR, FPS, HEIGHT, WIDTH


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bobgame")
        self.clock = pygame.time.Clock()
        self.bob = Bob()
        self.running = True

    def step(self, dt: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                self.running = False
        self.bob.update(dt, pygame.key.get_pressed(), pygame.mouse.get_pos())
        self.screen.fill(BG_COLOR)
        self.bob.draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            self.step(self.clock.tick(FPS) / 1000)
        pygame.quit()
