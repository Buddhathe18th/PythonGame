import pygame

class Interactable:
    def __init__(self, container,x, y, width, height, colour, subItems=[]):
        self.container = container
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(x, y, width, height)
        self.subItems = subItems
    
    def update(self,key,deltaTime):
        pygame.draw.rect(self.container, self.colour, self.rect)
        # self.container.blit(self.image, self.rect)
        
    
    # def draw(self, screen):
    #     pass

    def collides(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_point(self, x, y):
        return self.rect.collidepoint(x, y) 

class Player(Interactable):
    def __init__(self, container, x, y, width, height, colour, speed,velocityX,velocityY,subItems=[]):
        super().__init__(container, x, y, width, height, colour, subItems)
        self.speed = speed
        self.velocityX = velocityX
        self.velocityY = velocityY

    def update(self,key,deltaTime):
        self.readInputs(key)
        self.move(deltaTime)
        pygame.draw.rect(self.container, self.colour, self.rect)
        # self.container.blit(self.image, self.rect)
    
    def readInputs(self,key):
        if key[pygame.K_LEFT]:
            self.velocityX=self.velocityX-self.speed
        elif key[pygame.K_RIGHT]:
            self.velocityX=self.velocityX+self.speed

        if key[pygame.K_UP]:
            self.velocityY=self.velocityY-self.speed
        elif key[pygame.K_DOWN]:
            self.velocityY=self.velocityY+self.speed

        
        
    def move(self,deltaTime):

        # If our speed is too high, we want to cap it
        maxSpeed = 2

        if self.velocityX > maxSpeed:
            self.velocityX = maxSpeed
        elif self.velocityX < -maxSpeed:
            self.velocityX = -maxSpeed

        if self.velocityY > maxSpeed:
            self.velocityY = maxSpeed
        elif self.velocityY < -maxSpeed:
            self.velocityY = -maxSpeed

        self.rect.move_ip(self.velocityX*deltaTime,self.velocityY*deltaTime)

        if self.velocityX > 0:
            self.velocityX = self.velocityX-max(self.speed*0.9,0.1*self.velocityX)
        elif self.velocityX < 0:
            self.velocityX = self.velocityX+max(self.speed*0.9,0.1*self.velocityX)

        if self.velocityY > 0:
            self.velocityY = self.velocityY-max(self.speed*0.9,0.1*self.velocityY)
        elif self.velocityY < 0:
            self.velocityY = self.velocityY+max(self.speed*0.9,0.1*self.velocityY)