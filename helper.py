import pygame

class Interactable:
    def __init__(self, container, x, y, width, height):
        self.container = container
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    def update(self):
        self.container.update()
        self.container.fill((0,0,0))
        pygame.draw.rect(self.container, (255, 0, 0), self.rect)
        # self.container.blit(self.image, self.rect)
        pygame.display.update()
        
    
    # def draw(self, screen):
    #     pass

    def collides(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_point(self, x, y):
        return self.rect.collidepoint(x, y) 

class Player(Interactable):
    def __init__(self, container, x, y, width, height,speed):
        super().__init__(container, x, y, width, height)
        self.speed = speed

    def update(self,key,deltaTime):
        self.move(key,deltaTime)
        self.container.fill((0,0,0))
        pygame.draw.rect(self.container, (255, 0, 0), self.rect)
        # self.container.blit(self.image, self.rect)
        pygame.display.update()
        

    def move(self,key,deltaTime):
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-deltaTime*self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(deltaTime*self.speed,0)
        elif key[pygame.K_UP]:
            self.rect.move_ip(0,-deltaTime*self.speed)
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0,deltaTime*self.speed)