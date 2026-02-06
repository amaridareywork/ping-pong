import pygame


class GameSprite(pygame.sprite.Sprite):
    SPRITE_SIZE = (65, 65)

    def __init__(self, image_path, pos, speed, size=SPRITE_SIZE):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image_path),
            size
        )

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.speed = speed
    
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed