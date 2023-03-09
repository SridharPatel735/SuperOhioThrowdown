import pygame,random

class GameObject(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)

        self.rand_xd = random.choice([-1,1])
        self.rand_yd = random.choice([-1,1])

    def update(self):
       self.rect = self.rect.move(self.rand_xd*self.speed,self.rand_yd*self.speed)


class Diamond(GameObject):
    def __init__(self,screen_rect):
        rand_x = random.randint(250,screen_rect.width - 300) 
        rand_y = random.randint(100,screen_rect.height - 100)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 5

class Spaceship(GameObject):
    def __init__(self, screen_rect):
        super().__init__(screen_rect.centerx, screen_rect.centery, 'spaceship.png')
        self.speed = 2

class SavedDiamond(GameObject):
    def __init__(self,screen_rect):
        rand_x = random.randint(1250, 1350) 
        rand_y = random.randint(100,screen_rect.height - 100)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 0

class TakenDiamond(GameObject):
    def __init__(self,screen_rect):
        rand_x = random.randint(50,150) 
        rand_y = random.randint(100,screen_rect.height - 100)
        super().__init__(rand_x,rand_y,"diamond.png" )
        self.speed = 0     