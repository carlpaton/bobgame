import pygame

from .settings import (
    ARROW_COLOR, BOB_RADIUS, BOB_SPEED, HAIR_COLOR, HEIGHT, SKIN_COLOR, WIDTH,
)


class Bob:
    def __init__(self) -> None:
        self.pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self.facing = pygame.Vector2(0, -1)

    def update(self, dt: float, keys, mouse_pos) -> None:
        direction = pygame.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w],
        )
        if direction.length_squared() > 0:
            direction.normalize_ip()
        self.pos += direction * BOB_SPEED * dt
        self.pos.x = max(BOB_RADIUS, min(WIDTH - BOB_RADIUS, self.pos.x))
        self.pos.y = max(BOB_RADIUS, min(HEIGHT - BOB_RADIUS, self.pos.y))

        to_mouse = pygame.Vector2(mouse_pos) - self.pos
        if to_mouse.length_squared() > 0:
            self.facing = to_mouse.normalize()

    def draw(self, surface: pygame.Surface) -> None:
        center = (round(self.pos.x), round(self.pos.y))
        pygame.draw.circle(surface, SKIN_COLOR, center, BOB_RADIUS)
        # Hair: ring around the head plus a cap on the back half.
        pygame.draw.circle(surface, HAIR_COLOR, center, BOB_RADIUS, 4)
        back = self.pos - self.facing * (BOB_RADIUS * 0.35)
        pygame.draw.circle(
            surface, HAIR_COLOR, (round(back.x), round(back.y)), BOB_RADIUS * 0.6
        )

        # Arrow: line from the head edge plus a triangle tip.
        start = self.pos + self.facing * (BOB_RADIUS * 0.5)
        tip = self.pos + self.facing * (BOB_RADIUS + 18)
        base = tip - self.facing * 10
        side = pygame.Vector2(-self.facing.y, self.facing.x) * 6
        pygame.draw.line(surface, ARROW_COLOR, start, base, 3)
        pygame.draw.polygon(surface, ARROW_COLOR, [tip, base + side, base - side])
