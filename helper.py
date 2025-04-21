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
        self.previousPosition = self.rect.copy()
    
    def update(self,key,deltaTime,collided=False,collidedObject=None):
        pygame.draw.rect(self.container, self.colour, self.rect)
        # self.container.blit(self.image, self.rect)
    
    def reset(self):
        self.rect = self.previousPosition.copy()
        self.x=self.previousPosition.x
        self.y=self.previousPosition.y
        pygame.draw.rect(self.container, self.colour, self.rect)

    def collides(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_point(self, x, y):
        return self.rect.collidepoint(int(x), int(y)) 

class Player(Interactable):
    def __init__(self, container, x, y, width, height, colour, speed,velocityX,velocityY,subItems=[]):
        super().__init__(container, x, y, width, height, colour, subItems)
        self.speed = speed
        self.velocityX = velocityX
        self.velocityY = velocityY

    def update(self,key,deltaTime,collided=False,collidedObject=None):
        if not collided:
            self.readInputs(key)
            self.move(deltaTime)

            pygame.draw.rect(self.container, self.colour, self.rect)
        else:
            self.readInputs(key)
            self.moveX(deltaTime)
            if self.collides(collidedObject):
                self.reset()
            self.moveY(deltaTime)
            if self.collides(collidedObject):
                self.reset()
            pygame.draw.rect(self.container, self.colour, self.rect)
            
        # self.container.blit(self.image, self.rect)
    def reset(self):
        self.velocityX=0
        self.velocityY=0
        return super().reset()
    
    def readInputsGradual(self,key):
        if key[pygame.K_LEFT]:
            self.velocityX=self.velocityX-self.speed
        elif key[pygame.K_RIGHT]:
            self.velocityX=self.velocityX+self.speed

        if key[pygame.K_UP]:
            self.velocityY=self.velocityY-self.speed
        elif key[pygame.K_DOWN]:
            self.velocityY=self.velocityY+self.speed

    def readInputs(self,key):
        if key[pygame.K_LEFT]:
            self.velocityX=-1*self.speed
        elif key[pygame.K_RIGHT]:
            self.velocityX=+self.speed
        else:
            self.velocityX=0

        if key[pygame.K_UP]:
            self.velocityY=-self.speed
        elif key[pygame.K_DOWN]:
            self.velocityY=+self.speed
        else:
            self.velocityY=0
        
        
    def moveGradual(self,deltaTime):
        self.previousPosition = self.rect.copy()

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

        self.x+=self.velocityX*deltaTime
        self.y+=self.velocityY*deltaTime
        self.rect=pygame.Rect(int(self.x),int(self.y),self.width,self.height)

        if self.velocityX > 0:
            self.velocityX = self.velocityX-max(self.speed*0.9,0.1*self.velocityX)
        elif self.velocityX < 0:
            self.velocityX = self.velocityX+max(self.speed*0.9,0.1*self.velocityX)

        if self.velocityY > 0:
            self.velocityY = self.velocityY-max(self.speed*0.9,0.1*self.velocityY)
        elif self.velocityY < 0:
            self.velocityY = self.velocityY+max(self.speed*0.9,0.1*self.velocityY)

    def move(self,deltaTime):
        self.moveX(deltaTime)
        self.moveY(deltaTime)
    def moveX(self,deltaTime):
        self.previousPosition = self.rect.copy()
        self.x+=self.velocityX*deltaTime
        self.rect=pygame.Rect(int(self.x),int(self.y),self.width,self.height)
    def moveY(self,deltaTime):
        self.previousPosition = self.rect.copy()
        self.y+=self.velocityY*deltaTime
        self.rect=pygame.Rect(int(self.x),int(self.y),self.width,self.height)


