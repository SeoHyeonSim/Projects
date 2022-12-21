import pygame
from pygame.event import post
from pygame.version import PygameVersion
import os
import sys
import time
from random import randint
from math import sqrt
#########################################################################
#기본 초기화 (필수!)
pygame.init() # 초기화 




screen_width = 800
screen_height = 630
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("GAME NAME")
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
HTP_background_1 = pygame.image.load(os.path.join(image_path,"HTP_1.png"))

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

############################################################

# 로비화면
def Lobby():
    pygame.display.set_caption("Lobby")
    
    while True:
        
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
        
        Button_Game1 = Button(button_surface, 250, 150, "Game1","white","yellow")        
        Button_Game1.changeColor(Lobby_Mouspos)
        Button_Game1.update()
        
        # 게임 2 버튼
        
        Button_Game_2 = Button(button_surface, 520, 150, "Game2","white","yellow")        
        Button_Game_2.changeColor(Lobby_Mouspos)
        Button_Game_2.update()
        
        
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
        
        
        
        
        
                
        pygame.display.update()
        
##############################################################

# 게임방법 함수들
# 공 부수기
def HowToPlay_Ballcrash():
    
        while True:
            screen.blit(HTP_background_1, (0,0))
            Menu_Mouspos = pygame.mouse.get_pos()
            font = pygame.font.Font(None,70)
            title = font.render("How to play Ballcrash",True, (0,0,0))
            Button_Start = Button(button_surface, 700, 550, "Start!","white","yellow")
            Button_Back = Button(button_surface, 100, 550, "Back","white","yellow")
            screen.blit(title,(150,40))
            
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
            title = font.render("How to play Ballcrash",True, (0,0,0))
            Button_Start = Button(button_surface, 700, 550, "Start!","white","yellow")
            Button_Back = Button(button_surface, 100, 550, "Back","white","yellow")
            screen.blit(title,(150,40))
            
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
    backgorund = pygame.image.load(os.path.join(image_path,"background.png"))

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
        pygame.image.load(os.path.join(image_path,"ball1.png")),
        pygame.image.load(os.path.join(image_path,"ball2.png")),
        pygame.image.load(os.path.join(image_path,"ball3.png")),
        pygame.image.load(os.path.join(image_path,"ball4.png"))
            
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
            
        screen.blit(character, (character_x_pos,character_y_pos))
        screen.blit(stage,(0,screen_height-stage_height))
            
            
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
    backgorund = pygame.image.load(os.path.join(image_path,"background.png"))

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
        pygame.image.load(os.path.join(image_path,"ball1.png")),
        pygame.image.load(os.path.join(image_path,"ball2.png")),
        pygame.image.load(os.path.join(image_path,"ball3.png")),
        pygame.image.load(os.path.join(image_path,"ball4.png"))
            
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
            
        screen.blit(character, (character_x_pos,character_y_pos))
        screen.blit(stage,(0,screen_height-stage_height))
        
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
    backgorund = pygame.image.load(os.path.join(image_path,"background.png"))

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
        pygame.image.load(os.path.join(image_path,"ball1.png")),
        pygame.image.load(os.path.join(image_path,"ball2.png")),
        pygame.image.load(os.path.join(image_path,"ball3.png")),
        pygame.image.load(os.path.join(image_path,"ball4.png"))
            
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
            
        screen.blit(character, (character_x_pos,character_y_pos))
        screen.blit(stage,(0,screen_height-stage_height))
            
            
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
Gamover_rect = Gameover_text.get_rect()                                                                                           #85
Gamover_rect.center = (410, 250)  

# 게임 클리어 텍스트 변수
Gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
Gameclear_rect = Gameover_text.get_rect()                                                                                           #85
Gameclear_rect.center = (410, 250) 

# 배경 설정

Tetris_background_1 = pygame.image.load(os.path.join(image_path,"tetris-background.png"))
Tetris_background_2 = pygame.image.load(os.path.join(image_path,"tetris-background_2.png"))
Tetris_background_3 = pygame.image.load(os.path.join(image_path,"tetris-background_3.png"))
error_image = pygame.image.load(os.path.join(image_path,"error.png"))

BLACK = (0,0,0)
pygame.key.set_repeat(30, 30)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 630
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
WIDTH = 15
HEIGHT = 22
INTERVAL_1 = 40
INTERVAL_2 = 30
INTERVAL_3 = 15
# TODO : FILED값을 채운다.
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
        # 아래로 충돌?
        erased = 0
        if check_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    index = y_offset * self.size + x_offset
                    val = BLOCK.data[index]
                    if 0 <= self.ypos+y_offset < HEIGHT and \
                    0 <= self.xpos+x_offset < WIDTH and val != 0:
                            FIELD[self.ypos+y_offset][self.xpos+x_offset] = val ## 값을 채우고, erase_line()을 통해 삭제되도록 한다.

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
                f_xpos = 440 + (x_offset) * PIECE_GRID_SIZE
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
    pass

# 게임오버 메시지 표시 
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
def Gameclear_screen_1():
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
def Gameclear_screen_2():
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
def Gameclear_screen_3():
    while True:
        screen.blit(Gameclear_text,Gameclear_rect)
        
        result_text = game_font.render("Continue?",True, (255,255,255))
        result_text_rect = result_text.get_rect(center = (int(screen_width/2), int((screen_height/3)*1.5)))
        screen.blit(result_text,result_text_rect)
        
        Gameover_MosPos = pygame.mouse.get_pos()
        Button_Quit = Button(button_surface, 400, 550, "Back","white","yellow")


        for button in [Button_Quit]:
            button.changeColor(Gameover_MosPos)
            button.update()
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Button_Quit.checkForInput(Gameover_MosPos):                 # quit버튼 눌리면 게임 종료

                        Lobby()
                    
                    
        pygame.display.update()
        pygame.init()
####################################################33
# 테트리스 본 게임 함수
# 레벨 1
def Tetris_Lv_1():
    pygame.init()
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
        
        Tetris_Gameover_1()
        
        
    # 게임 클리어 메시지
    if Gamewin and not running:
        Gameclear_screen_1()
        
    pygame.display.update()
# 레벨 2
def Tetris_Lv_2():
    pygame.init()
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
            if score >= 1600:
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
        Gameclear_screen_2()
        pygame.display.update()
        
    pygame.display.update()
# 레벨 3
def Tetris_Lv_3():
    pygame.init()
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
        screen.blit(error_image,(440,100))
        
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
            if score >= 2800:
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

        # # 다음 블록 그리기
        # draw_next_block()
        
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
        Gameclear_screen_3()
        pygame.display.update()
        
    pygame.display.update()
######################################################################33
## 게임 실행
while True:
    
            
            
    
    startScreen()
    
    
