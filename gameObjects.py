import pygame
from levelSettings import *

battleLoopGrunt = False
gruntLoopRunOnce = False

# Level 1 Sprites


class PrisionTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "prisonfloortile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class DoorTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "prisonDoor.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class GruntTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "grunt.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

# Level 2 Sprites


class WaterTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "watertile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class GrassTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "grasstile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class SandTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "sandtile.jpg").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

# Level 3 Sprites

# Level 4 Sprites

# ALL LEVELS


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "new_rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites, grunt_sprite):
        super().__init__(groups)
        self.image = pygame.image.load(
            "sridhar_player_icon.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.grunt_sprite = grunt_sprite

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed
        self.collision("vertical")

    def collision(self, direction):
        global gruntLoopRunOnce
        global battleLoopGrunt

        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

        if gruntLoopRunOnce == False:
            for sprite in self.grunt_sprite:
                if sprite.rect.colliderect(self.rect):
                    battleLoopGrunt = True
                    gruntLoopRunOnce = True

    def update(self):
        self.input()
        self.move()
