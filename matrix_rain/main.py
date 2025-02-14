import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
FONT_SIZE = 14

# Cores
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 50, 0)

class Drop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(4, 8)
        self.char_list = []
        self.length = random.randint(5, 20)
        self.update_interval = random.randint(2, 5)
        self.counter = 0
        self.characters = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン1234567890"
        self.font = pygame.font.Font(None, FONT_SIZE)
    
    def update(self):
        self.y += self.speed
        self.counter += 1
        if self.counter >= self.update_interval:
            self.counter = 0
            if len(self.char_list) < self.length:
                self.char_list.append(random.choice(self.characters))
            
        if len(self.char_list) > self.length:
            self.char_list = self.char_list[-self.length:]
        
        return self.y - len(self.char_list) * FONT_SIZE < HEIGHT

    def draw(self, surface):
        for i, char in enumerate(self.char_list):
            pos_y = self.y - (i * FONT_SIZE)
            
            if pos_y < 0 or pos_y > HEIGHT:
                continue
            
            intensity = 255 - (i * (255 // len(self.char_list)))
            color = (0, max(intensity, 50), 0)
            
            char_surface = self.font.render(char, True, color)
            surface.blit(char_surface, (self.x, pos_y))

class MatrixRain:
    def __init__(self):
        self.drops = []
        self.spawn_interval = 5
        self.counter = 0
    
    def update(self):
        self.counter += 1
        if self.counter >= self.spawn_interval:
            self.counter = 0
            x = random.randint(0, WIDTH - FONT_SIZE)
            self.drops.append(Drop(x, 0))
        
        self.drops = [drop for drop in self.drops if drop.update()]
    
    def draw(self, surface):
        for drop in self.drops:
            drop.draw(surface)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Matrix Rain")
    
    clock = pygame.time.Clock()
    matrix = MatrixRain()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        matrix.update()
        
        screen.fill(BLACK)
        matrix.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
