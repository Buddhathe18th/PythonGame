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
        self.readInputs(key)
        self.move(deltaTime)


        # TODO: add refresh for container
        self.container.fill((0,0,0))
        pygame.draw.rect(self.container, (255, 0, 0), self.rect)
        # self.container.blit(self.image, self.rect)
    
    def readInputs(self,key):
        if key[pygame.K_LEFT]:
            self.velocityX=self.velocityX-self.speed
        elif key[pygame.K_RIGHT]:
            self.velocityX=self.velocityX+self.speed

        if key[pygame.K_UP]:
            self.velocityY=self.velocityY+self.speed
        elif key[pygame.K_DOWN]:
            self.velocityY=self.velocityY-self.speed
        
    def move(self,deltaTime):
        self.rect.move_ip(self.velocityX*deltaTime,self.velocityY*deltaTime)

        if self.velocityX > 0:
            self.velocityX = self.velocityX-0.1
        elif self.velocityX < 0:
            self.velocityX = self.velocityX+0.1

        if self.velocityY > 0:
            self.velocityY = self.velocityY-0.1
        elif self.velocityY < 0:
            self.velocityY = self.velocityY+0.1