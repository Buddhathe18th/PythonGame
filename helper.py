import pygame

class Interactable:
    def __init__(self, container,x, y, width, height,subItems=[]):
        self.container = container
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.subItems = subItems
    
    def update(self):
        self.container.update()
        self.container.fill((0,0,0))
        pygame.draw.rect(self.container, (255, 0, 0), self.rect)
        # self.container.blit(self.image, self.rect)
        
    
    # def draw(self, screen):
    #     pass

    def collides(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_point(self, x, y):
        return self.rect.collidepoint(x, y) 

class Player(Interactable):
    def __init__(self, container, x, y, width, height,speed,velocityX,velocityY,subItems=[]):
        super().__init__(container, x, y, width, height,subItems)
        self.speed = speed
        self.velocityX = velocityX
        self.velocityY = velocityY

    def update(self,key,deltaTime):
        self.move(key,deltaTime)

        # TODO: add refresh for container
        self.container.fill((0,0,0))
        pygame.draw.rect(self.container, (255, 0, 0), self.rect)
        # self.container.blit(self.image, self.rect)
        

    def move(self,key,deltaTime):
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-deltaTime*self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(deltaTime*self.speed,0)
        elif key[pygame.K_UP]:
            self.rect.move_ip(0,-deltaTime*self.speed)
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0,deltaTime*self.speed)