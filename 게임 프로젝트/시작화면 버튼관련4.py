import pygame
import sys

pygame.init() # 초기화 

screen_width = 800
screen_height = 630
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("GAME NAME")

backgorund = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/background_start.png")

game_font = pygame.font.Font(None, 40)

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pose = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pose))
        self.text_input = text_input
        self.text = game_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pose))
        
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = game_font.render(self.text_input, True, "yellow")
        else:
            self.text = game_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("startbutton.png")
button_surface = pygame.transform.scale(button_surface, (300, 110))

button = Button(button_surface, 400, 500, "Start!")

def startScreen():

        screen.blit(backgorund, (0,0))
        font = pygame.font.Font(None,80)
        title = font.render("MiniGame Wonderland",True, (0,0,0))
            
        screen.blit(title,(80,100))





running = True
start = True
while running:
    
            
            
    startScreen()

    
    
    

    
    for event in pygame.event.get():    # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            button.checkForInput(pygame.mouse.get_pos())

    button.update()
    button.changeColor(pygame.mouse.get_pos())
# 게임화면 다시 그리기. 계속 호출되어야 함! 필수!    
    pygame.display.update()    
    
