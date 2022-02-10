import pygame

class Ino(pygame.sprite.Sprite):
    """Класс одной вагины"""

    def __init__(self, screen):
        """Инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/vagina.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод вагины на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает вагины"""
        self.y += 0.1
        self.rect.y = self.y