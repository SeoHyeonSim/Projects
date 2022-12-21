import pygame
from pygame.event import post
from pygame.version import PygameVersion
import os
import sys
import time
import random
from random import randint
from math import sqrt
#########################################################################
#기본 초기화 (필수!)
pygame.init() # 초기화 




screen_width = 800
screen_height = 630
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("MiniGameNebula")
game_font = pygame.font.Font(None, 40)
current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")



# FPS 설정
clock = pygame.time.Clock()
#########################################################################


current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")
#여기서부터는 스스로! 
# 배경이미지 불러오기
title_backgorund = pygame.image.load(os.path.join(image_path,"background_start.png"))
lobby_background = pygame.image.load(os.path.join(image_path,"Lobby_background.png"))
HTP_background_1 = pygame.image.load(os.path.join(image_path,"HTP.png"))

leftkey = pygame.image.load(os.path.join(image_path,"left.png"))
rightkey = pygame.image.load(os.path.join(image_path,"right.png"))
upkey = pygame.image.load(os.path.join(image_path,"up.png"))
downkey = pygame.image.load(os.path.join(image_path,"down.png"))


###############################################################################################
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

# 버튼 이미지 설정
button_surface = pygame.image.load(os.path.join(image_path,"startbutton.png"))
button_surface = pygame.transform.scale(button_surface, (250, 80))


#폰트정의
game_font = pygame.font.Font(None, 40)
###############################################################################################
# 시작화면
def startScreen():
        pygame.display.set_caption("MiniGameNebula")
        while True:
            screen.blit(title_backgorund, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,80)
            title = font.render("MiniGame Nebula",True, (255,255,255))
            
            Button_Start = Button(button_surface, 400, 450, "Start!","white","yellow")
            
            Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
            
            screen.blit(title,(150,100))
            
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

############################################################

# 로비화면
def Lobby():
        
    while True:
        screen_width = 800
        screen_height = 630
        screen = pygame.display.set_mode((screen_width,screen_height))
        # 로비 레이아웃
        Lobby_Mouspos = pygame.mouse.get_pos()
        font = pygame.font.Font(None,30)
        Lobby_TEXT = font.render("Choose the game you want to play!",True, (0,0,0))
        screen.blit(lobby_background, (0,0))
        screen.blit(Lobby_TEXT,(400,550))
        
        # 메인화면 돌아가기 버튼
        Button_BACK = Button(button_surface, 150, 65, "Back to Title","white","yellow")
        Button_BACK.changeColor(Lobby_Mouspos)
        Button_BACK.update()
        
        
        # 게임 1 버튼     
        
        Button_Game1 = Button(button_surface, 400, 150, "AilenBalls","white","yellow")        
        Button_Game1.changeColor(Lobby_Mouspos)
        Button_Game1.update()
        
        # 게임 2 버튼
        
        Button_Game_2 = Button(button_surface, 400, 300, "SpaceBlock","white","yellow")        
        Button_Game_2.changeColor(Lobby_Mouspos)
        Button_Game_2.update()
        
        Button_Game_3 = Button(button_surface, 400, 450, "MeteorShoot","white","yellow")        
        Button_Game_3.changeColor(Lobby_Mouspos)
        Button_Game_3.update()
        
        
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:
                    # 창이 닫히는 이벤트가 발생하였는가? 
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:                # 돌아가기 버튼 누르면 startscree으로 돌아가라
                        if Button_BACK.checkForInput(Lobby_Mouspos):
                            startScreen()
                if event.type == pygame.MOUSEBUTTONDOWN:                # Game1버튼 누르면 BallGAme1실행
                        if Button_Game1.checkForInput(Lobby_Mouspos):
                            HowToPlay_Ballcrash()
                if event.type == pygame.MOUSEBUTTONDOWN:                # Game2버튼 누르면 게임 2 실행
                        if Button_Game_2.checkForInput(Lobby_Mouspos):
                            HowToPlay_Tetris()
                if event.type == pygame.MOUSEBUTTONDOWN:                # Game2버튼 누르면 게임 2 실행
                        if Button_Game_3.checkForInput(Lobby_Mouspos):
                            HowToPlay_Shooting()
        
        
        
        
        
                
        pygame.display.update()
        
##############################################################

# 게임방법 함수들
# 공 부수기
def HowToPlay_Ballcrash():
    
        while True:
            screen.blit(HTP_background_1, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,70)
            font_korean = pygame.font.SysFont('malgungothic', 17)

            title = font.render("How to play AilenBalls",True, (0,0,0))
            Button_Start = Button(button_surface, 700, 550, "Start!","white","yellow")
            Button_Back = Button(button_surface, 100, 550, "Back","white","yellow")
            
            leftkey = pygame.image.load(os.path.join(image_path,"left.png"))
            leftkey = pygame.transform.scale(leftkey,(50,50))
            rightkey = pygame.image.load(os.path.join(image_path,"right.png"))
            rightkey = pygame.transform.scale(rightkey,(50,50))
            spacekey = pygame.image.load(os.path.join(image_path,"space.png"))
            spacekey = pygame.transform.scale(spacekey,(150,50))
            
            blackscreen = pygame.image.load(os.path.join(image_path,"blackscreen.png"))
            blackscreen = pygame.transform.scale(blackscreen,(260,280))
            
            weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
            weapon = pygame.transform.scale(weapon,(17,150))
            character = pygame.image.load(os.path.join(image_path,"character.png"))
            ailen = pygame.image.load(os.path.join(image_path,"ball1-4.png"))
            
            text1 = smallfont.render("Move Left",True,(255,255,255))
            text2 = smallfont.render("Move Right",True,(255,255,255))
            text3 = smallfont.render("Fire Laser",True,(255,255,255))
            
            text4 = font_korean.render("공중에서 움직이는 외계인을 레이저로 모두 격추하면 게임 클리어!",True,(255,255,255))
            text5 = font_korean.render("TIP : 작은 외계인은 레이저를 옆으로 빗겨 쏘면 편합니다!",True,(255,255,255))

            
            screen.blit(title,(150,25))
            

            screen.blit(text1,(60,140))
            screen.blit(text2,(60,210))
            screen.blit(text3,(60,290))
            screen.blit(text4,(60,400))
            screen.blit(text5,(60,440))
            
            screen.blit(leftkey,(250,130))
            screen.blit(rightkey,(250,200))
            screen.blit(spacekey,(200,270))
            
            screen.blit(blackscreen,(500,105))
            screen.blit(weapon,(650,165))
            screen.blit(character,(640,295))
            screen.blit(weapon,(615,135))
            screen.blit(weapon,(580,115))
            
            screen.blit(ailen,(555,180))

            
            for button in [Button_Start,Button_Back]:
                button.changeColor(Menu_Mouspos)
                button.update()
                
                
            for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Start.checkForInput(Menu_Mouspos):                # Start버튼 눌리면 로비 함수 실행
                        BallGame_LV_1()
                    if Button_Back.checkForInput(Menu_Mouspos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                    
                    
                    
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수! 
            pygame.display.update()

# 테트리스
def HowToPlay_Tetris():
    
        while True:
            screen.blit(HTP_background_1, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,70)
            font_korean = pygame.font.SysFont('malgungothic', 16)

            title = font.render("How to play SpaceBlock",True, (0,0,0))
            Button_Start = Button(button_surface, 700, 550, "Start!","white","yellow")
            Button_Back = Button(button_surface, 100, 550, "Back","white","yellow")
            
            text1 = smallfont.render("Move Left",True,(255,255,255))
            text2 = smallfont.render("Move Right",True,(255,255,255))
            text3 = smallfont.render("Rotate Block",True,(255,255,255))
            text4 = smallfont.render("Block Down",True,(255,255,255))
            text5 = font_korean.render("P .S : 레벨 재시작, 다음 레벨로 넘어갈 시 블록이 자동으로 내려오지 않는 버그가 있습니다. ",True,(255,255,255))
            text6 = font_korean.render("첫 블록을 직접 내려주면 정상 작동합니다. ",True,(255,255,255))
            
            text7 = font_korean.render("내려오는 블록을 움직여서 한 줄이 채워지면 제거! ",True,(255,255,255))
            text8 = font_korean.render("블록이 맨 위까지 차오르면 게임 오버! ",True,(255,255,255))

            
            
            leftkey = pygame.image.load(os.path.join(image_path,"left.png"))
            leftkey = pygame.transform.scale(leftkey,(50,50))
            rightkey = pygame.image.load(os.path.join(image_path,"right.png"))
            rightkey = pygame.transform.scale(rightkey,(50,50))
            upkey = pygame.image.load(os.path.join(image_path,"up.png"))
            upkey = pygame.transform.scale(upkey,(50,50))
            downkey = pygame.image.load(os.path.join(image_path,"down.png"))
            downkey = pygame.transform.scale(downkey,(50,50))
            

            
            screen.blit(title,(125,25))
            screen.blit(text1,(110,130))
            screen.blit(text2,(110,190))
            screen.blit(text3,(110,250))
            screen.blit(text4,(110,310))
            screen.blit(text5,(60,380))
            screen.blit(text6,(105,430))
            
            screen.blit(text7,(400,200))
            screen.blit(text8,(400,250))
            
            screen.blit(leftkey,(300,110))
            screen.blit(rightkey,(300,170))
            screen.blit(upkey,(300,230))
            screen.blit(downkey,(300,290))
            
            for button in [Button_Start,Button_Back]:
                button.changeColor(Menu_Mouspos)
                button.update()
                
                
            for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Start.checkForInput(Menu_Mouspos):                # Start버튼 눌리면 로비 함수 실행
                        Tetris_Lv_1()
                    if Button_Back.checkForInput(Menu_Mouspos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                    
                    
                    
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수! 
            pygame.display.update()

# 슈팅게임   
def HowToPlay_Shooting():
    
        while True:
            screen.blit(HTP_background_1, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,70)
            font_korean = pygame.font.SysFont('malgungothic', 16)
            title = font.render("How to play MeteorShoot",True, (0,0,0))
            Button_Start = Button(button_surface, 700, 550, "Start!","white","yellow")
            Button_Back = Button(button_surface, 100, 550, "Back","white","yellow")
            

            
            leftkey = pygame.image.load(os.path.join(image_path,"left.png"))
            leftkey = pygame.transform.scale(leftkey,(50,50))
            rightkey = pygame.image.load(os.path.join(image_path,"right.png"))
            rightkey = pygame.transform.scale(rightkey,(50,50))
            spacekey = pygame.image.load(os.path.join(image_path,"space.png"))
            spacekey = pygame.transform.scale(spacekey,(150,50))
            
            screen.blit(title,(110,25))
            
            
            screen.blit(leftkey,(250,130))
            screen.blit(rightkey,(250,200))
            screen.blit(spacekey,(210,270))
                        
            text1 = smallfont.render("Move Left",True,(255,255,255))
            text2 = smallfont.render("Move Right",True,(255,255,255))
            text3 = smallfont.render("Fire Missile",True,(255,255,255))
            
            text4 = font_korean.render("위에서 내려오는 운석을 미사일로 파괴!",True,(255,255,255))
            text5 = font_korean.render("정해진 시간동안 생존하면 성공!",True,(255,255,255))
            
            text6 = font_korean.render("LEVEL 3에서 등장하는 탈출포드는 파괴하면 즉시 게임오버!",True,(255,255,255))
            
            pod = pygame.image.load(os.path.join(image_path,"pod.png"))
            
            screen.blit(text1,(60,140))
            screen.blit(text2,(60,210))
            screen.blit(text3,(60,290))
            
            screen.blit(text4,(480,300))
            screen.blit(text5,(480,350))
            
            rock1 = pygame.image.load(os.path.join(image_path,"rock01.png"))
            rock2 = pygame.image.load(os.path.join(image_path,"rock07.png"))
            rock3 = pygame.image.load(os.path.join(image_path,"rock25.png"))
            rock4 = pygame.image.load(os.path.join(image_path,"rock16.png"))
            rock5 = pygame.image.load(os.path.join(image_path,"rock14.png"))
            
            mark = pygame.image.load(os.path.join(image_path,"mark.png"))
            
            screen.blit(rock1,(480,150))
            screen.blit(rock2,(580,150))
            screen.blit(rock3,(680,170))
            screen.blit(rock4,(480,220))
            screen.blit(rock5,(590,200))
            
            
            
            screen.blit(pod,(60,410))
            screen.blit(text6,(100,420))
            
            for button in [Button_Start,Button_Back]:
                button.changeColor(Menu_Mouspos)
                button.update()
                
                
            for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Start.checkForInput(Menu_Mouspos):                # Start버튼 눌리면 로비 함수 실행
                        Shooting_Lv_1()
                    if Button_Back.checkForInput(Menu_Mouspos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                    
                    
                    
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수! 
            pygame.display.update()

######################################################3
# 공부수기 # 
# 게임오버 함수

#BallGame
# 레벨1
def GAMEOVER1(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_LV_1()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        pygame.time.delay(1000)
                        Lobby()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        pygame.display.update()
        pygame.init()
# 레벨2
def GAMEOVER2(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_Lv_2()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        pygame.time.delay(1000)
                        Lobby()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        pygame.display.update()
        pygame.init()
# 레벨3
def GAMEOVER3(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_Lv_3()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        pygame.time.delay(1000)
                        Lobby()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        pygame.display.update()
        pygame.init()

###############################################################
# 게임 성공 창 함수 

# BallGame
# 레벨1
def Win_BallGame1(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        game_font = pygame.font.Font(None, 40)
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        
        Win_BallGame1_text = game_font.render("You Win!",True,(255,255,255))
        screen.blit(Win_BallGame1_text, (340,250)) 
        
        
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Next_Level = Button(button_surface, 400, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Next_Level,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Next_Level.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_Lv_2()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                        
                        
                pygame.init()
                pygame.display.update()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        
        pygame.display.update()
        pygame.init()
# 레벨2
def Win_BallGame2(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        game_font = pygame.font.Font(None, 40)
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        
        Youwin_text = game_font.render("You Win!",True,(255,255,255))
        screen.blit(Youwin_text, (340,250)) 
        
        
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Next_Level = Button(button_surface, 400, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Next_Level,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Next_Level.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_Lv_3()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                        
                        
                pygame.init()
                pygame.display.update()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        
        pygame.display.update()
        pygame.init()
# 레벨3
def Win_BallGame3(game_result):              # 위에서 받은 game_result 값을 받아 실행됨
    while True:
        game_font = pygame.font.Font(None, 40)
        
        # 게임 종료 메세지 정의 - game_result에 따라서 출력됨
        msg = game_font.render(game_result,True,(255,255,255) )             
        msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/3)))
        screen.blit(msg, msg_rect)                                                                  # game_result 값 화면에 출력
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        
        Youwin_text = game_font.render("You Win!",True,(255,255,255))
        screen.blit(Youwin_text, (340,250)) 
        
        
        pygame.display.update()
        
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Replay = Button(button_surface, 400, 450, "Replay","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")
        
            
        for button in [Button_Replay,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
            
            
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Replay.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        pygame.time.delay(1000)
                        
                        BallGame_Lv_3()
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                        
                        
                pygame.init()
                pygame.display.update()
                    
                    
        
            # 게임화면 다시 그리기. 계속 호출되어야 함! 필수!
        
        pygame.display.update()
        pygame.init()


################################################################
## 공부수기 게임 함수 

# 레벨 1
def BallGame_LV_1():
    
    pygame.init()
    

    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    game_font = pygame.font.Font(None, 40)


    
    current_path = os.path.dirname(__file__) # 현재파일 위치 반환
    image_path = os.path.join(current_path,"images")

        

        #배경, 
    backgorund = pygame.image.load(os.path.join(image_path,"background_1.png"))

        #스테이지
    stage = pygame.image.load(os.path.join(image_path,"stage.png"))
    stage_size = stage.get_rect().size
    stage_height = stage_size[1]



    #캐릭터
    character = pygame.image.load(os.path.join(image_path,"character.png"))
    character_size = character.get_rect().size 
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2 )
    character_y_pos = screen_height - (character_height*1.7)

        # 이동할 좌표 
    character_to_x_LEFT = 0
    character_to_x_RIGHT = 0


        # 이동 속도
    character_speed = 7  

        # 무기 만들기
    weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
    weapon_size = weapon.get_rect().size
    weapon_width = weapon_size[0]

        #무기는 한번에 여러 발 발사 가능 

    weapons = []

        #무기 속도
    weapon_speed = 10

        # 공 만들기 (4개 크기 따로 처리)

    ball_images = [
        pygame.image.load(os.path.join(image_path,"ball1-1.png")),
        pygame.image.load(os.path.join(image_path,"ball1-2.png")),
        pygame.image.load(os.path.join(image_path,"ball1-3.png")),
        pygame.image.load(os.path.join(image_path,"ball1-4.png"))
            
        ]
        # 공 크기에 따른 최초 스피드
    ball_speed_y = [-18,-15,-12,-9]         # index 0 1 2 3 해당 값

        #공들
    balls = []
    balls.append({
        "pos_x" : 50,           # 공 x 좌표
        "pos_y" : 50,           # 공 y 좌표
        "img_idx" : 0,          # 공의 이미지 인덱스
        "to_x": 3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
        "to_y": -6,             # y축 이동방향
        "init_speed_y": ball_speed_y[0] })

    # 사라질 무기와 공 정보
    weapon_remove = -1
    ball_remove = -1

    game_font = pygame.font.Font(None, 40)

        
    total_time  = 100
    start_ticks = pygame.time.get_ticks()
        
    game_result = "GAME OVER" # 게임 종료 - 공에 맞음/ 타임아웃/ 모든 공 없앰
        
        
    running = True
    Gameover = False
    while running:
            
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:        # 키가 눌렸는지 확인, 왼쪽, 오른쪽, 위, 아래로 
                if event.key == pygame.K_LEFT:
                    character_to_x_LEFT -= character_speed
                elif event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT += character_speed
                elif event.key == pygame.K_SPACE:   #무기발사
                    weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos, weapon_y_pos])
                    

            if event.type == pygame.KEYUP:      # 키를 뗐는제 확인, 움직이지 않음.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_LEFT = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT= 0
                    
        # 캐릭터 위치 정의
        character_x_pos += character_to_x_LEFT + character_to_x_RIGHT           

            # 가로,세로 경계값 처리
        if character_x_pos <0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
            
        # 무기 위치 조정
        weapons = [[w[0],w[1] - weapon_speed] for w in weapons]  # 무기 위치 위로 올리기
            #천장에 닿은 무기 없애기
        weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]  # 무기가 천장에 닿지 않음

        # 공 위치 정의
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
                
            ball_size = ball_images[ball_img_idx].get_rect().size
            ball_width = ball_size[0]
            ball_height = ball_size[1]
                
                # 가로 벽에 닿았을 시 공 이동 위치 변경 (튕김)
            if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1
                    
                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
            if ball_pos_y >= screen_height - stage_height - ball_height:
                ball_val["to_y"] = ball_val["init_speed_y"]
            else:       # 그 외의 모든 경우에는 속도 증가, -값이였다가 어느정도에서 +가 되므로, 포물선
                ball_val["to_y"] += 0.5
                    
            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]
        # 충돌처리
        # 1. 캐릭터와 공 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos
            
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
            
            # 공 rect 업데이트
            ball_rect = ball_images[ball_img_idx].get_rect()
            ball_rect.left = ball_pos_x
            ball_rect.top= ball_pos_y
            # 공에 닿으면 게임 종료
            if character_rect.colliderect(ball_rect):
                    
                running = False
                Gameover = True
                break

        # 2. 공과 무기들 충돌 처리
            for weapon_idx, weapon_val in enumerate(weapons):
                weapon_x_pos = weapon_val[0]
                weapon_y_pos = weapon_val[1]
                
                
                # 무기 rect 정보 업데이트
                weapon_rect = weapon.get_rect()
                weapon_rect.left = weapon_x_pos
                weapon_rect.top = weapon_y_pos
                    
                if weapon_rect.colliderect(ball_rect):
                    weapon_remove = weapon_idx
                    ball_remove = ball_idx
                    
                        
                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                    if ball_img_idx < 3:
                            # 현재 공 크기 정보 가져오기
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1] 
                            
                            # 나뉘진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width = small_ball_rect.size[0]
                        small_ball_height = small_ball_rect.size[1]
                            
                            
                            # 왼쪽으로 튕겨나가는 작은 공 
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x": -3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })
                        
                        #     # 오른쪽으로 튕겨나가는 작은 공
                        # balls.append(
                        #     {
                        #     "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                        #     "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                        #     "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                        #     "to_x":  3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                        #     "to_y": -15,             # y축 이동방향
                        #     "init_speed_y": ball_speed_y[ball_img_idx + 1] })

                    break
            else: # 계속 게임을 진행
                continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
            break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출
                # 무기와 충돌한 공과 무기 없애기
                
        if ball_remove > -1:
            del balls[ball_remove]          # 그 위치의 공이 지워짐
            ball_remove = -1
                    
        if weapon_remove > -1:
            del weapons[weapon_remove]
            weapon_remove = -1
                
            # 모든 공을 없앤 경우 게임 성공
        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False
            Gameover = False
            

        #화면에 그리기
            
            # 배경 출력, 캐릭터 출력
        screen.blit(backgorund, (0,0))
            
            
        for weapon_x_pos, weapon_y_pos in weapons:
            screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
                
        for idx, val in enumerate(balls):
            ball_pos_x = val["pos_x"]
            ball_pos_y = val["pos_y"]
            ball_img_idx = val["img_idx"]
            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
            
        
        screen.blit(stage,(0,screen_height-stage_height))
        screen.blit(character, (character_x_pos,character_y_pos))
            
            # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        screen.blit(timer, (10,10))
        # 시간 초과했다면
        if total_time - elapsed_time <= 0:
            game_result = "Time Over"
            running = False
            Gameover = True
            pygame.init()
            break
            
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()


        # 게임 종료 출력
    if running != True and Gameover :
        pygame.time.delay(2000)     # 2초 대기
        GAMEOVER1(game_result)       # 게임오버 함수 실행
        
        
        # 미션 성공 
    elif running != True:
        pygame.time.delay(2000)     # 2초 대기
        Win_BallGame1(game_result)         # 게임 성공 함수 실행
    pygame.display.update()

#################################
# 레벨 2
def BallGame_Lv_2():
    pygame.init()
    

    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    game_font = pygame.font.Font(None, 40)


    



        
    current_path = os.path.dirname(__file__) # 현재파일 위치 반환
    image_path = os.path.join(current_path,"images")

    

        #배경, 
    backgorund = pygame.image.load(os.path.join(image_path,"background_2.png"))

        #스테이지
    stage = pygame.image.load(os.path.join(image_path,"stage.png"))
    stage_size = stage.get_rect().size
    stage_height = stage_size[1]


    wall1 = pygame.image.load(os.path.join(image_path,"wall.png"))
    wall1_size = wall1.get_rect().size
    wall1_width = wall1_size[0]
    wall1_height = wall1_size[1]
    
    wall2 = pygame.image.load(os.path.join(image_path,"wall.png"))
    wall2_size = wall2.get_rect().size
    wall2_width = wall2_size[0]
    wall2_height = wall2_size[1]
    

    #캐릭터
    character = pygame.image.load(os.path.join(image_path,"character.png")).convert_alpha()
    character_size = character.get_rect()
    character_size = character.get_rect().size 
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2 )
    character_y_pos = screen_height - (character_height*1.7)
    

        # 이동할 좌표 
    character_to_x_LEFT = 0
    character_to_x_RIGHT = 0

        # 이동 속도
    character_speed = 7  




        # 무기 만들기
    weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
    weapon_size = weapon.get_rect().size
    weapon_width = weapon_size[0]

        #무기는 한번에 여러 발 발사 가능 

    weapons = []

        #무기 속도
    weapon_speed = 10

        # 공 만들기 (4개 크기 따로 처리)

    ball_images = [
        pygame.image.load(os.path.join(image_path,"ball2-1.png")),
        pygame.image.load(os.path.join(image_path,"ball2-2.png")),
        pygame.image.load(os.path.join(image_path,"ball2-3.png")),
        pygame.image.load(os.path.join(image_path,"ball2-4.png"))
            
        ]
        # 공 크기에 따른 최초 스피드
    ball_speed_y = [-18,-15,-12,-9]         # index 0 1 2 3 해당 값

        #공들
    balls = []
    balls.append({
        "pos_x" :  120,           # 공 x 좌표
        "pos_y" : 50,           # 공 y 좌표
        "img_idx" : 0,          # 공의 이미지 인덱스
        "to_x": 3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
        "to_y": -6,             # y축 이동방향
        "init_speed_y": ball_speed_y[0] })

    # 사라질 무기와 공 정보
    weapon_remove = -1
    ball_remove = -1

    game_font = pygame.font.Font(None, 40)

        
    total_time  = 100
    start_ticks = pygame.time.get_ticks()
        
    game_result = "GAME OVER" # 게임 종료 - 공에 맞음/ 타임아웃/ 모든 공 없앰
        
        
    running = True
    Gameover = False



    while running:
        
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:        # 키가 눌렸는지 확인, 왼쪽, 오른쪽, 위, 아래로 
                if event.key == pygame.K_LEFT:
                    character_to_x_LEFT -= character_speed
                elif event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT += character_speed
                elif event.key == pygame.K_SPACE:   #무기발사
                    weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos, weapon_y_pos])
                    

            if event.type == pygame.KEYUP:      # 키를 뗐는제 확인, 움직이지 않음.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_LEFT = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT= 0
                    
        # 캐릭터 위치 정의
        character_x_pos += character_to_x_LEFT + character_to_x_RIGHT           
            # 가로,세로 경계값 처리
        if character_x_pos <0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
            
        # 무기 위치 조정
        weapons = [[w[0],w[1] - weapon_speed] for w in weapons]  # 무기 위치 위로 올리기
            #천장에 닿은 무기 없애기
        weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]  # 무기가 천장에 닿지 않음

        # 공 위치 정의
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
                
            ball_size = ball_images[ball_img_idx].get_rect().size
            ball_width = ball_size[0]
            ball_height = ball_size[1]
                
                # 가로 벽에 닿았을 시 공 이동 위치 변경 (튕김)
            if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1

            
                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
            if ball_pos_y >= screen_height - stage_height - ball_height:
                ball_val["to_y"] = ball_val["init_speed_y"]
                
            if ball_pos_x >= screen_width - wall1_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1
                
            if ball_pos_x <= wall2_width:
                ball_val["to_x"] = ball_val["to_x"] * -1
            
            # # 장애물 1 y축에 닿으면 튕김
            # if ball_pos_y >= screen_height - obstacle_img_height - stage_height- ball_height:
            #     ball_val["to_y"] = ball_val["init_speed_y"]
                
            
            else:       # 그 외의 모든 경우에는 속도 증가, -값이였다가 어느정도에서 +가 되므로, 포물선
                ball_val["to_y"] += 0.5
                    
            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]
        # 충돌처리
        
        
        
        
        
        
        
        
        
        # 1. 캐릭터와 공 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos
            
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
            
            # 공 rect 업데이트
            ball_rect = ball_images[ball_img_idx].get_rect()
            ball_rect.left = ball_pos_x
            ball_rect.top= ball_pos_y
            # 공에 닿으면 게임 종료
            if character_rect.colliderect(ball_rect):
                    
                running = False
                Gameover = True
                break
            
            
        # 2. 공과 무기들 충돌 처리
            for weapon_idx, weapon_val in enumerate(weapons):
                weapon_x_pos = weapon_val[0]
                weapon_y_pos = weapon_val[1]
                
                
                # 무기 rect 정보 업데이트
                weapon_rect = weapon.get_rect()
                weapon_rect.left = weapon_x_pos
                weapon_rect.top = weapon_y_pos
                    
                if weapon_rect.colliderect(ball_rect):
                    weapon_remove = weapon_idx
                    ball_remove = ball_idx
                    
                        
                    # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                        
                    # 처음 1번은 공이 2개로 쪼개짐
                    if ball_img_idx < 1:
                            # 현재 공 크기 정보 가져오기
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1] 
                            
                            # 나뉘진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width = small_ball_rect.size[0]
                        small_ball_height = small_ball_rect.size[1]
                            
                            
                            # 왼쪽으로 튕겨나가는 작은 공 
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x": -3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })
                        
                            # 오른쪽으로 튕겨나가는 작은 공
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x":  3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })
                        
                        
                        
                    # 이후는 그냥 작아지기만 하다가 사라짐
                    elif ball_img_idx < 3:
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1] 
                            
                            # 나뉘진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width = small_ball_rect.size[0]
                        small_ball_height = small_ball_rect.size[1]
                            
                            
                            # 왼쪽으로 튕겨나가는 작은 공 
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x": -3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })
                        break

                    break
            else: # 계속 게임을 진행
                continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
            break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출
                # 무기와 충돌한 공과 무기 없애기
                
        if ball_remove > -1:
            del balls[ball_remove]          # 그 위치의 공이 지워짐
            ball_remove = -1
                    
        if weapon_remove > -1:
            del weapons[weapon_remove]
            weapon_remove = -1
                
            # 모든 공을 없앤 경우 게임 성공
        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False
            









        #화면에 그리기
            
            # 배경 출력, 캐릭터 출력
        screen.blit(backgorund, (0,0))
        
            
            
        for weapon_x_pos, weapon_y_pos in weapons:
            screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
                
        for idx, val in enumerate(balls):
            ball_pos_x = val["pos_x"]
            ball_pos_y = val["pos_y"]
            ball_img_idx = val["img_idx"]
            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
            
        
        screen.blit(stage,(0,screen_height-stage_height))
        screen.blit(character, (character_x_pos,character_y_pos))
        
        screen.blit(wall1,(screen_width-wall1_width,0))
        screen.blit(wall2,(0,0))

            
            # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        screen.blit(timer, (10,10))
        # 시간 초과했다면
        if total_time - elapsed_time <= 0:
            game_result = "Time Over"
            running = False
            Gameover = True
            
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()

        # 게임 종료 출력
    if running != True and Gameover :
        pygame.time.delay(2000)     # 2초 대기
        GAMEOVER2(game_result)       # 게임오버 함수 실행
    
    
    elif running != True:
        pygame.time.delay(2000)       # 2초 대기
        Win_BallGame2(game_result)           # 게임 성공 함수 실행
    pygame.display.update()

######################################
# 레벨 3
def BallGame_Lv_3():
    pygame.init()
    

    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    game_font = pygame.font.Font(None, 40)
        
    current_path = os.path.dirname(__file__) # 현재파일 위치 반환
    image_path = os.path.join(current_path,"images")

        #배경, 
    backgorund = pygame.image.load(os.path.join(image_path,"background_3.png"))

        #스테이지
    stage = pygame.image.load(os.path.join(image_path,"stage.png"))
    stage_size = stage.get_rect().size
    stage_height = stage_size[1]

    #캐릭터
    character = pygame.image.load(os.path.join(image_path,"character.png"))
    character_size = character.get_rect().size 
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2 )
    character_y_pos = screen_height - (character_height*1.7)

        # 이동할 좌표 
    character_to_x_LEFT = 0
    character_to_x_RIGHT = 0

        # 이동 속도
    character_speed = 7  
    
        # 무기 만들기
    weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
    weapon_size = weapon.get_rect().size
    weapon_width = weapon_size[0]

        #무기는 한번에 여러 발 발사 가능 

    weapons = []

        #무기 속도
    weapon_speed = 10

        # 공 만들기 (4개 크기 따로 처리)

    ball_images = [
        pygame.image.load(os.path.join(image_path,"ball3-1.png")),
        pygame.image.load(os.path.join(image_path,"ball3-2.png")),
        pygame.image.load(os.path.join(image_path,"ball3-3.png")),
        pygame.image.load(os.path.join(image_path,"ball3-4.png"))
            
        ]
        # 공 크기에 따른 최초 스피드
    ball_speed_y = [-18,-15,-12,-9]         # index 0 1 2 3 해당 값

        #공들
    balls = []
    balls.append({
        "pos_x" : 50,           # 공 x 좌표
        "pos_y" : 50,           # 공 y 좌표
        "img_idx" : 0,          # 공의 이미지 인덱스
        "to_x": 3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
        "to_y": -6,             # y축 이동방향
        "init_speed_y": ball_speed_y[0] })

    # 사라질 무기와 공 정보
    weapon_remove = -1
    ball_remove = -1

    game_font = pygame.font.Font(None, 40)

        
    total_time  = 100
    start_ticks = pygame.time.get_ticks()
        
    game_result = "GAME OVER" # 게임 종료 - 공에 맞음/ 타임아웃/ 모든 공 없앰
        
        
    running = True
    Gameover = False
    
    while running:
        
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False            # 게임이 진행중이 아님. 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:        # 키가 눌렸는지 확인, 왼쪽, 오른쪽, 위, 아래로 
                if event.key == pygame.K_LEFT:
                    character_to_x_LEFT -= character_speed
                elif event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT += character_speed
                elif event.key == pygame.K_SPACE:   #무기발사
                    weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos, weapon_y_pos])
                    

            if event.type == pygame.KEYUP:      # 키를 뗐는제 확인, 움직이지 않음.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_LEFT = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT= 0
                    
        # 캐릭터 위치 정의
        character_x_pos += character_to_x_LEFT + character_to_x_RIGHT           
        
            # 가로,세로 경계값 처리
        if character_x_pos <0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
            
        # 무기 위치 조정
        weapons = [[w[0],w[1] - weapon_speed] for w in weapons]  # 무기 위치 위로 올리기
            #천장에 닿은 무기 없애기
        weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]  # 무기가 천장에 닿지 않음

        # 공 위치 정의
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
                
            ball_size = ball_images[ball_img_idx].get_rect().size
            ball_width = ball_size[0]
            ball_height = ball_size[1]
                
                # 가로 벽에 닿았을 시 공 이동 위치 변경 (튕김)
            if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1
                    
                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
            if ball_pos_y >= screen_height - stage_height - ball_height:
                ball_val["to_y"] = ball_val["init_speed_y"]
            else:       # 그 외의 모든 경우에는 속도 증가, -값이였다가 어느정도에서 +가 되므로, 포물선
                ball_val["to_y"] += 0.5
                    
            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]
        # 충돌처리
        # 1. 캐릭터와 공 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos
            
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]
            
            # 공 rect 업데이트
            ball_rect = ball_images[ball_img_idx].get_rect()
            ball_rect.left = ball_pos_x
            ball_rect.top= ball_pos_y
            # 공에 닿으면 게임 종료
            if character_rect.colliderect(ball_rect):
                    
                running = False
                Gameover = True
                break
                
        # 2. 공과 무기들 충돌 처리
            for weapon_idx, weapon_val in enumerate(weapons):
                weapon_x_pos = weapon_val[0]
                weapon_y_pos = weapon_val[1]
                
                
                # 무기 rect 정보 업데이트
                weapon_rect = weapon.get_rect()
                weapon_rect.left = weapon_x_pos
                weapon_rect.top = weapon_y_pos
                    
                if weapon_rect.colliderect(ball_rect):
                    weapon_remove = weapon_idx
                    ball_remove = ball_idx
                    
                        
                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                    if ball_img_idx < 3:
                            # 현재 공 크기 정보 가져오기
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1] 
                            
                            # 나뉘진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width = small_ball_rect.size[0]
                        small_ball_height = small_ball_rect.size[1]
                            
                            
                            # 왼쪽으로 튕겨나가는 작은 공 
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x": -3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })
                        
                            # 오른쪽으로 튕겨나가는 작은 공
                        balls.append(
                            {
                            "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2) ,           # 공 x 좌표
                            "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height/ 2),           # 공 y 좌표
                            "img_idx" : ball_img_idx + 1,          # 공의 이미지 인덱스
                            "to_x":  3,              # x축 이동방향 -3은 왼쪽, 3은 오른쪽 
                            "to_y": -15,             # y축 이동방향
                            "init_speed_y": ball_speed_y[ball_img_idx + 1] })

                    break
            else: # 계속 게임을 진행
                continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
            break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출
                # 무기와 충돌한 공과 무기 없애기
                
        if ball_remove > -1:
            del balls[ball_remove]          # 그 위치의 공이 지워짐
            ball_remove = -1
                    
        if weapon_remove > -1:
            del weapons[weapon_remove]
            weapon_remove = -1
                
            # 모든 공을 없앤 경우 게임 성공
        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False

        #화면에 그리기
            
            # 배경 출력, 캐릭터 출력
        screen.blit(backgorund, (0,0))
            
            
        for weapon_x_pos, weapon_y_pos in weapons:
            screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
                
        for idx, val in enumerate(balls):
            ball_pos_x = val["pos_x"]
            ball_pos_y = val["pos_y"]
            ball_img_idx = val["img_idx"]
            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
            
        
        screen.blit(stage,(0,screen_height-stage_height))
        screen.blit(character, (character_x_pos,character_y_pos))
            
            
            # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        screen.blit(timer, (10,10))
        # 시간 초과했다면
        if total_time - elapsed_time <= 0:
            game_result = "Time Over"
            running = False
            Gameover = True
            pygame.init()
            break
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()


        # 게임 종료 출력
    if running != True and Gameover :
        pygame.time.delay(2000)     # 2초 대기
        GAMEOVER3(game_result)       # 게임오버 함수 실행
    
    
    elif running != True:
        pygame.time.delay(2000)       # 2초 대기
        Win_BallGame3(game_result)           # 게임 성공 함수 실행
        
        
        
    pygame.display.update()

#########################################
## 테트리스 게임 함수 
smallfont = pygame.font.SysFont(None, 36)
largefont = pygame.font.SysFont(None, 72)

# 게임 오버 텍스트 변수
Gameover_text = largefont.render("Gameover!",True,(225,225,225))
Gamover_rect = Gameover_text.get_rect()                                                                                          
Gamover_rect.center = (410, 250)  

# 게임 클리어 텍스트 변수
Gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
Gameclear_rect = Gameover_text.get_rect()                                                                                          
Gameclear_rect.center = (410, 250) 

# 배경 설정

Tetris_background_1 = pygame.image.load(os.path.join(image_path,"tetris_background_1.png"))
Tetris_background_2 = pygame.image.load(os.path.join(image_path,"tetris_background_2.png"))
Tetris_background_3 = pygame.image.load(os.path.join(image_path,"tetris_background_3.png"))
error_image = pygame.image.load(os.path.join(image_path,"error.png"))

next_text = smallfont.render("NEXT",True,(255,255,0))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 630
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WIDTH = 15
HEIGHT = 22
INTERVAL_1 = 30
INTERVAL_2 = 15
INTERVAL_3 = 2
FIELD = []
COLORS = ((0, 0, 0), (255, 165, 0), (0, 0, 255), (0, 255, 255), \
            (0, 255, 0), (255, 0, 255), (255, 255, 0), (255, 0, 0), (128, 128, 128))
BLOCK = None
NEXT_BLOCK = None
PIECE_SIZE = 24 # 24 x 24
PIECE_GRID_SIZE = PIECE_SIZE+1 
BLOCK_DATA = (
    (
        (0, 0, 1, \
        1, 1, 1, \
        0, 0, 0),
        (0, 1, 0, \
        0, 1, 0, \
        0, 1, 1),
        (0, 0, 0, \
        1, 1, 1, \
        1, 0, 0),
        (1, 1, 0, \
        0, 1, 0, \
        0, 1, 0),
    ), (
        (2, 0, 0, \
        2, 2, 2, \
        0, 0, 0),
        (0, 2, 2, \
        0, 2, 0, \
        0, 2, 0),
        (0, 0, 0, \
        2, 2, 2, \
        0, 0, 2),
        (0, 2, 0, \
        0, 2, 0, \
        2, 2, 0)
    ), (
        (0, 3, 0, \
        3, 3, 3, \
        0, 0, 0),
        (0, 3, 0, \
        0, 3, 3, \
        0, 3, 0),
        (0, 0, 0, \
        3, 3, 3, \
        0, 3, 0),
        (0, 3, 0, \
        3, 3, 0, \
        0, 3, 0)
    ), (
        (4, 4, 0, \
        0, 4, 4, \
        0, 0, 0),
        (0, 0, 4, \
        0, 4, 4, \
        0, 4, 0),
        (0, 0, 0, \
        4, 4, 0, \
        0, 4, 4),
        (0, 4, 0, \
        4, 4, 0, \
        4, 0, 0)
    ), (
        (0, 5, 5, \
        5, 5, 0, \
        0, 0, 0),
        (0, 5, 0, \
        0, 5, 5, \
        0, 0, 5),
        (0, 0, 0, \
        0, 5, 5, \
        5, 5, 0),
        (5, 0, 0, \
        5, 5, 0, \
        0, 5, 0)
    ), (
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6)
    ), (
        (0, 7, 0, 0, \
        0, 7, 0, 0, \
        0, 7, 0, 0, \
        0, 7, 0, 0),
        (0, 0, 0, 0, \
        7, 7, 7, 7, \
        0, 0, 0, 0, \
        0, 0, 0, 0),
        (0, 0, 7, 0, \
        0, 0, 7, 0, \
        0, 0, 7, 0, \
        0, 0, 7, 0),
        (0, 0, 0, 0, \
        0, 0, 0, 0, \
        7, 7, 7, 7, \
        0, 0, 0, 0)
    )
)
# 블록 클래스 설정
class Block:
    def __init__(self, count):
        self.turn =randint(0,3) # 다양한 모양이 나오게 변경하기 
        self.type = BLOCK_DATA[randint(0,6)]   
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        self.fire = count + INTERVAL_1

    def update(self, count):
        # 블록 상태 갱신
        erased = 0
        if check_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    index = y_offset * self.size + x_offset
                    val = BLOCK.data[index]
                    if 0 <= self.ypos+y_offset < HEIGHT and \
                    0 <= self.xpos+x_offset < WIDTH and val != 0:
                            FIELD[self.ypos+y_offset][self.xpos+x_offset] = val # 값을 채우고, erase_line()을 통해 삭제되도록 한다.

            erased = line_clear()
            go_next_block(count)

        if self.fire < count:
            self.fire = count + INTERVAL_1
            self.ypos += 1
        return erased
    
# 블록 그리기 함수 정의
    def draw(self):
        for y_offset in range(self.size):
            for x_offset in range(self.size):
                index = y_offset * self.size + x_offset
                val = self.data[index]
                if 0 <= y_offset + self.ypos < HEIGHT and\
                    0 <= x_offset + self.xpos < WIDTH and val != 0:
                        f_xpos = PIECE_GRID_SIZE + (x_offset + self.xpos) * PIECE_GRID_SIZE
                        f_ypos = PIECE_GRID_SIZE + (y_offset + self.ypos) * PIECE_GRID_SIZE
                        pygame.draw.rect(screen, COLORS[val],
                                    (f_xpos, 
                                    f_ypos, 
                                    PIECE_SIZE, 
                                    PIECE_SIZE))

##############################################################
# 한 줄이 모두 차면 지우고, 개수를 반환
def line_clear():           
        erased = 0
        ypos = HEIGHT - 2
        print(FIELD[ypos])
        while ypos >=0:
            if all(FIELD[ypos]) == True:        # 모든 줄이 체워지면
                del FIELD[ypos]                 # 그 행을 지우고 빈 줄을 넣음
                FIELD.insert(0, [8, 0,0,0,0,0,0,0,0,0,0,0,0,0 ,8])
                erased += 1
            else:
                ypos -= 1
        return erased
##############################################################

################################################
# 블록생성, 다음 블록 전환
def go_next_block(count):
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

# 블록이 벽, 땅에 충돌 확인. 닿으면 그 자리에 정지                 
def check_overlapped(xpos, ypos, turn):
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            index = y_offset * BLOCK.size + x_offset
            val = data[index]
            
            if 0 <= xpos+x_offset < WIDTH and \
                    0 <= ypos+y_offset < HEIGHT:
                    if val != 0 and \
                        FIELD[ypos+y_offset][xpos+x_offset] != 0:
                        return True

# 필드 세팅
def set_game_field():
    for i in range(HEIGHT-1):
            FIELD.insert(0, [8, 0,0,0,0,0,0,0,0,0,0,0,0,0 ,8])  
        
    FIELD.insert(HEIGHT-1, [8, 8,8,8,8,8,8,8,8,8,8,8,8,8 ,8])

# 필드 그리기 
def draw_game_field():
    
    for y_offset in range(HEIGHT):
            for x_offset in range(WIDTH):
                val = FIELD[y_offset][x_offset]
                color = COLORS[val]
                pygame.draw.rect(screen, 
                                color,
                                (PIECE_GRID_SIZE + x_offset*PIECE_GRID_SIZE, 
                                PIECE_GRID_SIZE + y_offset*PIECE_GRID_SIZE , 
                                PIECE_SIZE , 
                                PIECE_SIZE ))


# 현재 블록 그리기
def draw_current_block():
    BLOCK.draw()
    
# 다음에 나올 블록 보여주기
def draw_next_block():          
    for y_offset in range(NEXT_BLOCK.size):
            for x_offset in range(NEXT_BLOCK.size):
                index = y_offset * NEXT_BLOCK.size + x_offset
                val = NEXT_BLOCK.data[index]
                # 블록을 보여줄 자리 설정
                f_xpos = 470 + (x_offset) * PIECE_GRID_SIZE
                f_ypos = 100 + (y_offset) * PIECE_GRID_SIZE
                pygame.draw.rect(screen, COLORS[val],
                                (f_xpos, 
                                f_ypos, 
                                PIECE_SIZE, 
                                PIECE_SIZE))
# 점수 표시         
def draw_score(score):
    # 스코어는 6자리로 표기
    score_str = str(score).zfill(6)
    score_image = smallfont.render(score_str, True, (255,255,255))
    screen.blit(score_image, (700, 30))
    screen.blit(next_text,(470,70))

# 테트리스 게임오버 함수
# 레벨 1 게임오버      
def Tetris_Gameover_1():
    while True:
        
        screen.blit(Gameover_text,Gamover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Tetris_Lv_1()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()
        
# 레벨 2 게임오버
def Tetris_Gameover_2():
    while True:
        screen.blit(Gameover_text,Gamover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Tetris_Lv_2()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()

# 레벨 3 게임오버
def Tetris_Gameover_3():
    while True:
        screen.blit(Gameover_text,Gamover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Tetris_Lv_3()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()

#############################################################################################3
#게임 클리어 함수
# 레벨 1 클리어
def Tetris_Gameclear_1():
    while True:
        screen.blit(Gameclear_text,Gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 400, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Tetris_Lv_2()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 2 클리어
def Tetris_Gameclear_2():
    while True:
        screen.blit(Gameclear_text,Gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue_2 = Button(button_surface, 400, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 400, 550, "Quit","white","yellow")


        for button in [Button_Continue_2,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue_2.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Tetris_Lv_3()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 3 클리어
def Tetris_Gameclear_3():
    while True:
        screen.blit(Gameclear_text,Gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Quit = Button(button_surface, 400, 550, "Back","white","yellow")
        Button_Replay = Button(button_surface, 400, 450, "Replay","white","yellow")

        for button in [Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
        for button in [Button_Replay]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Replay.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Tetris_Lv_3()
                
                    if Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()
####################################################33
# 테트리스 본 게임 함수
# 레벨 1
def Tetris_Lv_1():
    pygame.init()
    pygame.key.set_repeat(30, 30)
    global INTERVAL_1
    count = 0
    score = 0
    running = True
    Gameover = False
    Gamewin = False
    go_next_block(INTERVAL_1)

    set_game_field()

    while running:
        clock.tick(10)
        screen.blit(Tetris_background_1,(0,0))

        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
            elif event.type == pygame.KEYUP:
                key = None
#########################################################################
# 점수 체크 - 행이 지워지면 200점씩 더함
        if not Gameover:                
            count += 5
            if count % 1000 == 0:
                INTERVAL_1 = max(1, INTERVAL_1 - 2)
            erased = BLOCK.update(count)

            if erased > 0:
                score += (2 ** erased) * 100
# 목표 점수 달성 시 게임 클리어
            if score >= 600:
                running = False
                Gamewin = True
#########################################################################

# 게임오버 체크
# filled > 2 블록이 맨 위까지 쌓였을 경우 게임 오버 
            filled = 0
            for cell in FIELD[0]:
                if cell != 0:
                    filled +=1
                if filled > 2:
                    Gameover = True
                    running = False
                    break
#########################################################################
            

            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == pygame.K_UP:
                next_t = (next_t + 1) % 4
            elif key == pygame.K_RIGHT:
                next_x += 1
            elif key == pygame.K_LEFT:
                next_x -= 1
            elif key == pygame.K_DOWN:
                next_y += 1

            if not check_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        # 게임필드 그리기
        draw_game_field()

        # 낙하 중인 블록 그리기
        draw_current_block()

        # 다음 블록 그리기
        draw_next_block()
        
        # 점수 나타내기
        draw_score(score)
        
        
        
        pygame.display.update()
    pygame.display.update()
    
    # 게임 오버 메시지 
    if Gameover and not running:
        
        Tetris_Gameover_1()
        
        
    # 게임 클리어 메시지
    if Gamewin and not running:
        Tetris_Gameclear_1()
        
    pygame.display.update()
# 레벨 2
def Tetris_Lv_2():
    pygame.init()
    pygame.key.set_repeat(30, 30)
    global INTERVAL_2
    count = 0
    score = 0
    running = True
    Gameover = False
    Gamewin = False
    go_next_block(INTERVAL_2)

    set_game_field()

    while running and not Gameover:
        clock.tick(10)
        screen.blit(Tetris_background_2,(0,0))

        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
            elif event.type == pygame.KEYUP:
                key = None
#########################################################################
# 점수 체크 - 행이 지워지면 200점씩 더함
        if not Gameover:                
            count += 5
            if count % 1000 == 0:
                INTERVAL_2 = max(1, INTERVAL_2 - 2)
            erased = BLOCK.update(count)

            if erased > 0:
                score += (2 ** erased) * 100
# 목표 점수 달성 시 게임 클리어
            if score >= 1000:
                running = False
                Gamewin = True
#########################################################################

# 게임오버 체크
# filled > 2 블록이 맨 위까지 쌓였을 경우 게임 오버 
            filled = 0
            for cell in FIELD[0]:
                if cell != 0:
                    filled +=1
                if filled > 2:
                    Gameover = True
                    running = False
                    break
#########################################################################
            

            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == pygame.K_UP:
                next_t = (next_t + 1) % 4
            elif key == pygame.K_RIGHT:
                next_x += 1
            elif key == pygame.K_LEFT:
                next_x -= 1
            elif key == pygame.K_DOWN:
                next_y += 1

            if not check_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        # 게임필드 그리기
        draw_game_field()

        # 낙하 중인 블록 그리기
        draw_current_block()

        # 다음 블록 그리기
        draw_next_block()
        
        # 점수 나타내기
        draw_score(score)
        
        
        
        pygame.display.update()
    pygame.display.update()
    
    # 게임 오버 메시지 
    if Gameover and not running:
        
        Tetris_Gameover_2()
        pygame.display.update()
        
    # 게임 클리어 메시지
    if Gamewin and not running:
        Tetris_Gameclear_2()
        pygame.display.update()
        
    pygame.display.update()
# 레벨 3
def Tetris_Lv_3():
    pygame.init()
    pygame.key.set_repeat(30, 30)
    global INTERVAL_3
    count = 0
    score = 0
    running = True
    Gameover = False
    Gamewin = False
    go_next_block(INTERVAL_3)

    set_game_field()

    while running and not Gameover:
        clock.tick(10)
        
        screen.blit(Tetris_background_3,(0,0))
        screen.blit(error_image,(470,100))
        
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
            elif event.type == pygame.KEYUP:
                key = None
#########################################################################
# 점수 체크 - 행이 지워지면 200점씩 더함
        if not Gameover:                
            count += 5
            if count % 1000 == 0:
                INTERVAL_3 = max(1, INTERVAL_3 - 2)
            erased = BLOCK.update(count)

            if erased > 0:
                score += (2 ** erased) * 100
# 목표 점수 달성 시 게임 클리어
            if score >= 1400:
                running = False
                Gamewin = True
#########################################################################

# 게임오버 체크
# filled > 2 블록이 맨 위까지 쌓였을 경우 게임 오버 
            filled = 0
            for cell in FIELD[0]:
                if cell != 0:
                    filled +=1
                if filled > 2:
                    Gameover = True
                    running = False
                    break
#########################################################################
            

            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == pygame.K_UP:
                next_t = (next_t + 1) % 4
            elif key == pygame.K_RIGHT:
                next_x += 1
            elif key == pygame.K_LEFT:
                next_x -= 1
            elif key == pygame.K_DOWN:
                next_y += 1

            if not check_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        # 게임필드 그리기
        draw_game_field()

        # 낙하 중인 블록 그리기
        draw_current_block()
        
        # 점수 나타내기
        draw_score(score)
        
        
        
        pygame.display.update()
    pygame.display.update()
    
    # 게임 오버 메시지 
    if Gameover and not running:
        
        Tetris_Gameover_3()
        pygame.display.update()
        
    # 게임 클리어 메시지
    if Gamewin and not running:
        Tetris_Gameclear_3()
        pygame.display.update()
        
    pygame.display.update()

######################################################################33

## 슈팅 게임
#############################################################3
# 게임 관련 변수
shooting_screen_width = 500
shooting_screen_height = 630
current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")
smallfont = pygame.font.SysFont(None, 36)
largefont = pygame.font.SysFont(None, 72)

# 게임 오버 텍스트 변수
shooting_gameover_text = largefont.render("Gameover!",True,(225,225,225))
shooting_gameover_rect = shooting_gameover_text.get_rect()                                                                                          
shooting_gameover_rect.center = (250, 250)  

# 게임 클리어 텍스트 변수
shooting_gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
shooting_gameclear_rect = shooting_gameover_text.get_rect()                                                                                          
shooting_gameclear_rect.center = (250, 250) 
# 게임 관련 함수

# 그리기 함수
def draw_text(text,font,surface,x,y,main_color):
    text_obj = font.render(text,True,main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj,text_rect)


# 전투기 #
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super(Fighter,self).__init__()
        self.image = pygame.image.load(os.path.join(image_path,"fighter.png"))
        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]
        self.rect.x = (shooting_screen_width / 2) - (self.width / 2 )
        self.rect.y = shooting_screen_height - (self.height*2)
        self.dx = 0
        self.dy = 0
    def update(self):
                # 이동할 좌표 
        self.rect.x += self.dx
        
        if self.rect.x < 0 or self.rect.x + self.rect.width > shooting_screen_width:
            self.rect.x -= self.dx
    
    def draw(self,shooting_screen):
        shooting_screen.blit(self.image,self.rect)
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite

##############################################################3
    # 미사일 만들기
class Missile(pygame.sprite.Sprite):
    def __init__(self, xpos,ypos,speed):
        super(Missile,self).__init__()
        self.image = pygame.image.load(os.path.join(image_path,"missile.png"))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.speed = speed
            
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y + self.rect.height < 0 :
            self.kill()
            
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite
    def draw(self,shooting_screen):
        shooting_screen.blit(self.image,self.rect)
    
# 운석 # 
class Rock(pygame.sprite.Sprite):
        def __init__(self, xpos,ypos,speed):
            super(Rock,self).__init__()
            # 적 이미지 설정
            rock_images = [
                'C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/images/rock01.png',
                'C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/images/rock16.png',
                'C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/images/rock25.png',
                'C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/images/rock07.png',
                'C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/images/rock14.png'
                ]        
                # 적 이미지 랜덤 설정
            self.image = pygame.image.load(random.choice(rock_images))                
                
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos
            self.speed = speed
                
            # 적 움직임. 위에서 내려오니 y 값을 speed만큼 설정. (추후 x축 수정?)
        def update(self):
            self.rect.y += self.speed
                
        # 운석(적)이 화면 밖 (여기선 y축) 으로 나가면 적용 - 없애기 + 데미지
        def out_of_shooting_screen(self):
            if self.rect.y > shooting_screen_height:
                return True
        def draw(self,shooting_screen):
            shooting_screen.blit(self.image,self.rect)

# 탈출포드 - 파괴하면 안됨
class EscapePod(pygame.sprite.Sprite):
        def __init__(self, xpos,ypos,speed):
            super(EscapePod,self).__init__()
            # 적 이미지 설정

            self.image = pygame.image.load(os.path.join(image_path,"pod.png"))
            
                
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos
            self.speed = speed
                
            # 적 움직임. 위에서 내려오니 y 값을 speed만큼 설정. (추후 x축 수정?)
        def update(self):
            self.rect.y += self.speed
                
        # 운석(적)이 화면 밖 (여기선 y축) 으로 나가면 적용 ( 없애기 + 데미지 )
        def out_of_shooting_screen(self):
            if self.rect.y > shooting_screen_height:
                return True
        def draw(self,shooting_screen):
            shooting_screen.blit(self.image,self.rect) 
###################################################################

# 슈팅 게임오버 함수
# 레벨 1
def Shooting_gameover_1():
    while True:
    
        screen.blit(shooting_gameover_text,shooting_gameover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 250, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 250, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Shooting_Lv_1()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        
                        Lobby()
                        
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 2 
def Shooting_gameover_2():
    while True:
    
        screen.blit(shooting_gameover_text,shooting_gameover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 250, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 250, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Shooting_Lv_2()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        
                        Lobby()
                        
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 3
def Shooting_gameover_3():
    while True:
    
        screen.blit(shooting_gameover_text,shooting_gameover_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 250, 450, "Continue","white","yellow")
        Button_Quit = Button(button_surface, 250, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Shooting_Lv_3()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        
                        
                        Lobby()
                        
                    
                    
        pygame.display.update()
        pygame.init()

# 슈팅게임 클리어 함수 
# 레벨 1
def Shooting_gameclear_1():
    while True:
        screen.blit(shooting_gameclear_text,shooting_gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 250, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 250, 550, "Quit","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Shooting_Lv_2()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                        
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 2
def Shooting_gameclear_2():
    while True:
        screen.blit(shooting_gameclear_text,shooting_gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Continue = Button(button_surface, 250, 450, "Next Level","white","yellow")
        Button_Quit = Button(button_surface, 250, 550, "Back","white","yellow")


        for button in [Button_Continue,Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Continue.checkForInput(Gameover_MosPos):                # Continue버튼 눌리면  함수 실행
                        Shooting_Lv_3()
                        
                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                        
                    
                    
        pygame.display.update()
        pygame.init()
# 레벨 3
def Shooting_gameclear_3():
    while True:
        screen.blit(shooting_gameclear_text,shooting_gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(shooting_screen_width/2), int((shooting_screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Quit = Button(button_surface, 250, 550, "Quit","white","yellow")
        Button_Replay = Button(button_surface, 250, 450, "Replay","white","yellow")


        for button in [Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
            
        for button in [Button_Replay]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Replay.checkForInput(Gameover_MosPos):                

                        Shooting_Lv_3()

                    elif Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료
                        Lobby()
                        

                    
        pygame.display.update()
        pygame.init()
#############################################################3
# 슈팅 게임 본 게임 함수 
# 운석슈팅 본 게임 함수 
# 레벨 1
def Shooting_Lv_1():
    
    shooting_screen_width = 500
    shooting_screen_height = 630
    shooting_screen = pygame.display.set_mode((shooting_screen_width,shooting_screen_height))
    # 게임 오버 텍스트 변수
    shooting_gameover_text = largefont.render("Gameover!",True,(225,225,225))
    shooting_gameover_rect = shooting_gameover_text.get_rect()                                                                                          
    shooting_gameover_rect.center = (250, 300)  

    # 게임 클리어 텍스트 변수
    shooting_gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
    shooting_gameclear_rect = shooting_gameover_text.get_rect()                                                                                          
    shooting_gameclear_rect.center = (250, 300)  
    
    #폰트정의
    font_shooting = pygame.font.Font(None, 30)
    time_font = pygame.font.Font(None,32)
    # 총 시간, 시간계산
    total_time = 60
    start_ticks = pygame.time.get_ticks()
    
    

# 게임 오버 텍스트 변수
    shooting_gameover_text = largefont.render("Gameover!",True,(225,225,225))
    shooting_gameover_rect = shooting_gameover_text.get_rect()                                                                                          
    shooting_gameover_rect.center = (410, 250)  

    # 게임 클리어 텍스트 변수
    shooting_gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
    shooting_gameclear_rect = shooting_gameover_text.get_rect()                                                                                          
    shooting_gameclear_rect.center = (410, 250) 
    
# 스프라이트 불러오기
    background = pygame.image.load(os.path.join(image_path,"shooting_background_1.png"))
    
    fighter = Fighter()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group() 
            

# 확률
    occur_prob= 70
    shot_count = 0
    count_missed = 0
    life = 3
        
        
    running = True
    Gameover = False
    shooting_gameclear = False
    
##########################################################
# 게임 실행부분
    while running and not Gameover:
            
        dt = clock.tick(70)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 

            # 방향키로 전투기 위치 조정
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 6
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 6                    
                # 스페이스로 미사일 발사
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx,fighter.rect.centery,10)
                    missiles.add(missile)
                    
            # 키를 뗐을 때 
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    fighter.dx =0
        
                    
###############################################################################
# 운석 생성 부분    
        occur_of_rock = 1 + int(shot_count / 300)
        min_rock_speed = 1
        max_rock_speed = 3   
        
        # 운석생성
        if random.randint(1,occur_prob) == 1:
            for i in range(occur_of_rock):
                speed = random.randint(min_rock_speed,max_rock_speed)
                rock = Rock(random.randint(0,shooting_screen_width - 50),0,speed)
                rocks.add(rock)
        pygame.display.update()

#####################################################################
# 충돌처리 #
        for missile in missiles:
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                
                shot_count += 1
                
        for rock in rocks:
            if rock.out_of_shooting_screen():
                rock.kill()
                count_missed += 1

##################################################################################
        #화면에 그리기
            
        # 배경 출력
        shooting_screen.blit(background, (0,0))
        
        # 경과 시간 표시
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = time_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        shooting_screen.blit(timer, (10,10))
        
        # 몇개의 적을 파괴했는지 표시 (얘들은 추후 라이프로 교체)
        # 몇개의 적을 놓쳤는지 표시
        draw_text('Life: {}'.format(int(life - count_missed)),font_shooting,shooting_screen, 450,20,(225,225,225))

        
        
        # 전투기 출력
        fighter.update()
        fighter.draw(shooting_screen)
        # 미사일 출력
        missiles.update()
        missiles.draw(shooting_screen)
        # 운석 출력
        rocks.update()
        rocks.draw(shooting_screen)
        pygame.display.update()
        
##########################################################################3
# 게임 종료 조건 설정
        if fighter.collide(rocks) or count_missed >= 3:
            running = False
            Gameover = True
        
        elif total_time - elapsed_time <= 0:
            running = False
            shooting_gameclear = True

        

        
        
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()


    # 게임 오버 메시지 
    if Gameover:
        
        Shooting_gameover_1()
        
        
    # 게임 클리어 메시지
    if shooting_gameclear:
        Shooting_gameclear_1()
        


    pygame.display.update()
            
    
    
    pygame.quit()
    
# 레벨 2
def Shooting_Lv_2():
    pygame.init()
    
    shooting_screen_width = 500
    shooting_screen_height = 630
    shooting_screen = pygame.display.set_mode((shooting_screen_width,shooting_screen_height))
    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    font_shooting = pygame.font.Font(None, 30)
    time_font = pygame.font.Font(None,32)
    # 총 시간, 시간계산
    total_time = 60
    start_ticks = pygame.time.get_ticks()

# 게임 오버 텍스트 변수
    Gameover_text = largefont.render("Gameover!",True,(225,225,225))
    Gamover_rect = Gameover_text.get_rect()                                                                                          
    Gamover_rect.center = (410, 250)  

    # 게임 클리어 텍스트 변수
    Gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
    Gameclear_rect = Gameover_text.get_rect()                                                                                          
    Gameclear_rect.center = (410, 250) 
    
# 스프라이트 불러오기
    background = pygame.image.load(os.path.join(image_path,"shooting_background_2.png"))
    
    fighter = Fighter()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group() 
            

# 확률
    occur_prob= 50
    shot_count = 0
    count_missed = 0
    life = 3
        
        
    running = True
    Gameover = False
    Gameclear = False
    
##########################################################
# 게임 실행부분
    while running and not Gameover:
            
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 

            # 방향키로 전투기 위치 조정
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 6
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 6
                    
                # 스페이스로 미사일 발사
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx,fighter.rect.centery,10)
                    missiles.add(missile)
                    
            # 키를 뗐을 때 
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    fighter.dx =0
                
                    
###############################################################################
# 운석 생성 부분    
        occur_of_rock = 1 + int(shot_count / 300)
        min_rock_speed = 2
        max_rock_speed = 3   
        
        # 운석생성
        if random.randint(1,occur_prob) == 1:
            for i in range(occur_of_rock):
                speed = random.randint(min_rock_speed,max_rock_speed)
                rock = Rock(random.randint(0,shooting_screen_width - 50),0,speed)
                rocks.add(rock)
                

#####################################################################
# 충돌처리 #
        for missile in missiles:
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                shot_count += 1
                
        for rock in rocks:
            if rock.out_of_shooting_screen():
                rock.kill()
                count_missed += 1

##################################################################################
        #화면에 그리기
            
        # 배경 출력
        shooting_screen.blit(background, (0,0))
        
        # 경과 시간 표시
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = time_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        shooting_screen.blit(timer, (10,10))
        
        # 몇개의 적을 파괴했는지 표시 (얘들은 추후 라이프로 교체)
        # 몇개의 적을 놓쳤는지 표시
        draw_text('Life: {}'.format(int(life - count_missed)),font_shooting,shooting_screen, 450,20,(225,225,225))

        
        
        # 전투기 출력
        fighter.update()
        fighter.draw(shooting_screen)
        # 미사일 출력
        missiles.update()
        missiles.draw(shooting_screen)
        # 운석 출력
        rocks.update()
        rocks.draw(shooting_screen)
        pygame.display.update()
        
##########################################################################3
# 게임 종료 조건 설정
        if fighter.collide(rocks) or count_missed >= 3:
            running = False
            Gameover = True
        
        elif total_time - elapsed_time <= 0:
            running = False
            Gameclear = True

        

        
        
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()


    # 게임 오버 메시지 
    if Gameover:
        
        Shooting_gameover_2()
        
        
    # 게임 클리어 메시지
    if Gameclear:
        Shooting_gameclear_2()
        


    pygame.display.update()
            
    
    
    pygame.quit()
# 레벨 3
def Shooting_Lv_3():
    pygame.init()
    shooting_screen_width = 500
    shooting_screen_height = 630
    shooting_screen = pygame.display.set_mode((shooting_screen_width,shooting_screen_height))

    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    font_shooting = pygame.font.Font(None, 30)
    time_font = pygame.font.Font(None,32)
    # 총 시간, 시간계산
    total_time = 100
    start_ticks = pygame.time.get_ticks()

# 게임 오버 텍스트 변수
    Gameover_text = largefont.render("Gameover!",True,(225,225,225))
    Gamover_rect = Gameover_text.get_rect()                                                                                          
    Gamover_rect.center = (410, 250)  

    # 게임 클리어 텍스트 변수
    Gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
    Gameclear_rect = Gameover_text.get_rect()                                                                                          
    Gameclear_rect.center = (410, 250) 
    
# 스프라이트 불러오기
    background = pygame.image.load(os.path.join(image_path,"shooting_background_3.png"))
    
    fighter = Fighter()
    missiles = pygame.sprite.Group()
    rocks = pygame.sprite.Group() 
    pods = pygame.sprite.Group()
            

# 확률
    occur_prob= 70
    pod_prob = 120
    shot_count = 0
    count_missed = 0
    life = 3
        
        
    running = True
    Gameover = False
    Gameclear = False
    
##########################################################
# 게임 실행부분
    while running and not Gameover:
            
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 

            # 방향키로 전투기 위치 조정
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 7
                elif event.key == pygame.K_RIGHT:
                    fighter.dx += 7
                    
                # 스페이스로 미사일 발사
                elif event.key == pygame.K_SPACE:
                    missile = Missile(fighter.rect.centerx,fighter.rect.centery,10)
                    missiles.add(missile)
                    
            # 키를 뗐을 때 
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    fighter.dx =0
                
                    
###############################################################################
# 운석 생성 부분    
        occur_of_rock = 1 + int(shot_count / 300)
        min_rock_speed = 2
        max_rock_speed = 3   
        
        
        # 운석생성
        if random.randint(1,occur_prob) == 1:
            for i in range(occur_of_rock):
                speed = random.randint(min_rock_speed,max_rock_speed)
                rock = Rock(random.randint(0,shooting_screen_width - 50),0,speed)
                rocks.add(rock)
                
        # 부술수 없는 운석 생성
        if random.randint(1,pod_prob) == 1:
            for i in range(occur_of_rock):
                speed = 4
                pod = EscapePod(random.randint(0,shooting_screen_width - 50),0,speed)
                pods.add(pod)
            
                

#####################################################################
# 미사일 충돌처리 #
        for missile in missiles:
        # 미사일과 운석
            rock = missile.collide(rocks)
            if rock:
                missile.kill()
                rock.kill()
                shot_count += 1
                
        # 미사일과 부수면 안되는 운석 - 부술 시 게임오버 
            pod = missile.collide(pods)
            if pod:
                missile.kill()
                pod.kill()
                running = False
                Gameover = True
                
                
                
                
# 운석이 밖으로 나가면 지우기
        for rock in rocks:
            if rock.out_of_shooting_screen():
                rock.kill()
                count_missed += 1
# 부수면 안되는 운석은 그냥 보내기
        for pod in pods:
            if pod.out_of_shooting_screen():
                pod.kill()
                
##################################################################################
        #화면에 그리기
            
        # 배경 출력
        shooting_screen.blit(background, (0,0))
        
        # 경과 시간 표시
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #밀리세컨드 - 세컨드 변환
        timer = time_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
        shooting_screen.blit(timer, (10,10))
        
        # 몇개의 적을 파괴했는지 표시 (얘들은 추후 라이프로 교체)
        # 몇개의 적을 놓쳤는지 표시
        draw_text('Life: {}'.format(int(life - count_missed)),font_shooting,shooting_screen, 450,20,(225,225,225))

        
        
        # 전투기 출력
        fighter.update()
        fighter.draw(shooting_screen)
        # 미사일 출력
        missiles.update()
        missiles.draw(shooting_screen)
        # 운석 출력
        rocks.update()
        rocks.draw(shooting_screen)
        # 부술수 없는 운석 출력
        pods.update()
        pods.draw(shooting_screen)
        
        pygame.display.update()
        
##########################################################################3
# 게임 종료 조건 설정
        if fighter.collide(rocks) or count_missed >= 3:
            running = False
            Gameover = True
        
        
        
        elif total_time - elapsed_time <= 0:
            running = False
            Gameclear = True

        

        
        
        # 게임화면 다시 그리기. 계속 호출되어야 함! 필수    
        pygame.display.update()


    # 게임 오버 메시지 
    if Gameover:
        
        Shooting_gameover_3()
        
        
    # 게임 클리어 메시지
    if Gameclear:
        Shooting_gameclear_3()
        


    pygame.display.update()
            
    
    
    pygame.quit()
#################################################################################
## 게임 실행
while True:
    
            
            
    
    startScreen()
    
    
