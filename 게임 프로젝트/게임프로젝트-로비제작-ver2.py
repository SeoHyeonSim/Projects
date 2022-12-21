import pygame
from pygame.event import post
from pygame.version import PygameVersion
import os
import sys
import time

#########################################################################
#기본 초기화 (필수!)
pygame.init() # 초기화 

screen_width = 800
screen_height = 630
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("GAME NAME")

# FPS 설정
clock = pygame.time.Clock()
#########################################################################


current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")
#여기서부터는 스스로! 
# 배경이미지 불러오기
title_backgorund = pygame.image.load(os.path.join(image_path,"background_start.png"))
lobby_background = pygame.image.load(os.path.join(image_path,"Lobby_background.png"))

# title_backgorund = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/background_start.png")
# lobby_background = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/Lobby_background.png")

# 버튼 개체
class Button():
    def __init__(self, image, x_pos, y_pos, text_input, base_color, hover_color):
        self.image = image
        self.x_pos = x_pos
        self.y_pose = y_pos
        self.base_color = base_color
        self.hover_color = hover_color
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pose))
        self.text_input = text_input
        self.text = game_font.render(self.text_input, True, self.base_color)
        if self.image is not None:
            screen.blit(self.image,self.rect)
        self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pose))
        
    def update(self):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = game_font.render(self.text_input, True, self.hover_color)
        else:
            self.text = game_font.render(self.text_input, True, self.base_color)


button_surface = pygame.image.load(os.path.join(image_path,"startbutton.png"))
# button_surface = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/startbutton.png")
button_surface = pygame.transform.scale(button_surface, (250, 80))


#폰트정의
game_font = pygame.font.Font(None, 40)

# 총 시간, 시간계산
# total_time = 10
# start_ticks = pygame.time.get_ticks()


#이벤트 루프

# 시작화면
def startScreen():
        pygame.display.set_caption("StartScreen")
        while True:
            screen.blit(title_backgorund, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,80)
            title = font.render("MiniGame Wonderland",True, (0,0,0))
            Button_Start = Button(button_surface, 400, 450, "Start!","white","yellow")
            Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
            screen.blit(title,(80,100))
            
            for button in [Button_Start,Button_Quit]:
                button.changeColor(Menu_Mouspos)
                button.update()
                
                
            for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Start.checkForInput(Menu_Mouspos):                # Start버튼 눌리면 로비 함수 실행
                        Lobby()
                    if Button_Quit.checkForInput(Menu_Mouspos):                 # quit버튼 눌리면 게임 종료
                        pygame.quit()
                        sys.exit()
                    
                    
                    
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수! 
            pygame.display.update()

# 로비화면
def Lobby():
    pygame.display.set_caption("Lobby")
    
    while True:
        
        Lobby_Mouspos = pygame.mouse.get_pos()
        font = pygame.font.Font(None,30)
        Lobby_TEXT = font.render("Choose the game you want to play!",True, (0,0,0))
        screen.blit(lobby_background, (0,0))
        screen.blit(Lobby_TEXT,(400,550))
        Button_BACK = Button(button_surface, 150, 65, "Back to Title","white","yellow")
        
        Button_BACK.changeColor(Lobby_Mouspos)
        Button_BACK.update()
        
        
        #게임 1 버튼
        Button_Game1 = Button(button_surface, 300, 150, "Game1","white","yellow")        
        Button_Game1.changeColor(Lobby_Mouspos)
        Button_Game1.update()
        
        
        
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:
                    # 창이 닫히는 이벤트가 발생하였는가? 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if Button_BACK.checkForInput(Lobby_Mouspos):
                            startScreen()
                if event.type == pygame.MOUSEBUTTONDOWN:                # Game1버튼 누르면 BallGAme1실행
                        if Button_Game1.checkForInput(Lobby_Mouspos):
                            HowToPlay()
        pygame.display.update()
        
    

# 플레이 방법 함수
def HowToPlay():
    pygame.display.set_caption("Lobby")
    
    while True:
        
        Guide_Mouspos = pygame.mouse.get_pos()
        font = pygame.font.Font(None,30)
        Guide_TEXT = font.render("How To Play",True, (0,0,0))
        screen.blit(lobby_background, (0,0))
        screen.blit(Guide_TEXT,(400,550))
        Button_BACK = Button(button_surface, 150, 200, "Back to Title","white","yellow")
        
        Button_BACK.changeColor(Guide_Mouspos)
        Button_BACK.update()
        
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:
                    # 창이 닫히는 이벤트가 발생하였는가? 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if Button_BACK.checkForInput(Guide_Mouspos):
                            Lobby()
        pygame.display.update()






# 게임 실행
while True:
    
            
            
    
    startScreen()
    
    
