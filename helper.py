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
        self.prevX = self.x
        self.prevY = self.y
        self.prevWidth = self.width
        self.prevHeight = self.height
    
    def update(self,key,deltaTime,objects):
        pygame.draw.rect(self.container, self.colour, self.rect)
        # self.container.blit(self.image, self.rect)
    
    def reset(self):
        self.rect = pygame.Rect(self.prevX, self.prevY, self.prevWidth, self.prevHeight)
        self.x=self.prevX        
        self.y=self.prevY
        self.width=self.prevWidth
        self.height=self.prevHeight
        pygame.draw.rect(self.container, self.colour, self.rect)

    def collides(self, other):
        return self.rect.colliderect(other.rect)
    
    def collides_all(self, objects):
        for obj in objects:
            if obj!=self:
                if self.rect.colliderect(obj.rect):
                    return True
        return False
    
    def collides_point(self, x, y):
        return self.rect.collidepoint(int(x), int(y)) 

class Player(Interactable):
    def __init__(self, container, x, y, width, height, colour, speed,velocityX,velocityY,subItems=[]):
        super().__init__(container, x, y, width, height, colour, subItems)
        self.speed = speed
        self.velocityX = velocityX
        self.velocityY = velocityY
        # TODO: Float-To-Int conversion for X and Y

    def update(self,key,deltaTime,objects):
            self.readInputs(key)
            self.moveX(deltaTime)
            if self.collides_all(objects):
                self.resetX()
            self.moveY(deltaTime)
            if self.collides_all(objects):
                self.resetY()
            pygame.draw.rect(self.container, self.colour, self.rect)
            
            
        # self.container.blit(self.image, self.rect)
    def reset(self):
        return super().reset()
    
    def resetX(self):
        self.velocityX=0
        self.x=self.prevX
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def resetY(self):
        self.velocityY=0
        self.y=self.prevY
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    
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

        if key[pygame.K_SPACE]:
            pygame.draw.rect(self.container, (0,0,255), self.previousPosition)
        
        
    def moveGradual(self,deltaTime):
        self.previousPosition = pygame.Rect(self.prevX, self.prevY, self.prevWidth, self.prevHeight)

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
        self.prevX=self.x
        self.x+=self.velocityX*deltaTime
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def moveY(self,deltaTime):
        self.prevY=self.y
        self.y+=self.velocityY*deltaTime
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)


