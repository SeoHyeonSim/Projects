import pygame
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



#여기서부터는 스스로! 
# 배경이미지 불러오기
backgorund = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/background_start.png")








# 스프라이트 불러오기
# character = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/pygame/character.png")
# character_size = character.get_rect().size 
# character_width = character_size[0]
# character_height = character_size[1]
# character_x_pos = (screen_width / 2) - (character_width / 2 )
# character_y_pos = screen_height - character_height

# 이동할 좌표 
# to_x = 0
# to_y = 0

# 이동 속도
# character_speed = 0.5

# 장애물
# obstacle = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/pygame/obstacle.png")
# obstacle_size = obstacle.get_rect().size 
# obstacle_width = obstacle_size[0]
# obstacle_height = obstacle_size[1]
# obstacle_x_pos = (screen_width / 2) - (obstacle_width / 2 )
# obtacle_y_pos = (screen_height / 2) - (obstacle_height / 2)


#폰트정의
game_font = pygame.font.Font(None, 40)

# 총 시간, 시간계산
# total_time = 10
# start_ticks = pygame.time.get_ticks()


#이벤트 루프
def startScreen():
        screen.blit(backgorund, (0,0))
        font = pygame.font.Font(None,80)
        title = font.render("MiniGame Wonderland",True, (0,0,0))
            
        screen.blit(title,(80,100))

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

button_surface = pygame.image.load("C:/Users/sss/OneDrive/바탕 화면/게임 프로젝트/startbutton.png")
button_surface = pygame.transform.scale(button_surface, (300, 110))

button1 = Button(button_surface, 400, 500, "Start!")
button2 = Button(button_surface, 400, 300, "Hello!")

def startScreen():

        screen.blit(backgorund, (0,0))
        font = pygame.font.Font(None,80)
        title = font.render("MiniGame Wonderland",True, (0,0,0))
            
        screen.blit(title,(80,100))


startscreen = True
running = True
while running:
    
            
            
    
    startScreen()
    
    
    

    
    for event in pygame.event.get():    # 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
            running = False
            
            
            
        # 버튼 함수 - 마우스 올라가면 색 변하기
        # 1번(시작)버튼
        if event.type == pygame.MOUSEBUTTONUP:
            button1.checkForInput(pygame.mouse.get_pos())
        
        # 2번 버튼
        if event.type == pygame.MOUSEBUTTONUP:
            button1.checkForInput(pygame.mouse.get_pos()) 
            
    button1.update()
    button1.changeColor(pygame.mouse.get_pos())
    
    button2.update()
    button2.changeColor(pygame.mouse.get_pos())
    
    
    
# running = True    # 게임이 진행중인가? 
# while running:
#     dt = clock.tick(60)     # 게임의 프레임 수 설정
    
#     for event in pygame.event.get():    # 이벤트가 발생하였는가?
#         if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
#             running = False              # 게임이 진행중이 아님. 

#         if event.type == pygame.KEYDOWN:        # 키가 눌렸는지 확인, 왼쪽, 오른쪽, 위, 아래로 
#             if event.key == pygame.K_LEFT:
#                 to_x -= character_speed
#             elif event.key == pygame.K_RIGHT:
#                 to_x += character_speed 
#             elif event.key == pygame.K_UP:
#                 to_y -= character_speed
#             elif event.key == pygame.K_DOWN:
#                 to_y += character_speed
#         if event.type == pygame.KEYUP:      # 키를 뗐는제 확인, 움직이지 않음.
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 to_x = 0
#             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                 to_y = 0
            
#     character_x_pos += to_x * dt
#     character_y_pos += to_y * dt

# # 가로,세로 경계값 처리
#     if character_x_pos <0:
#         character_x_pos = 0
#     elif character_x_pos > screen_width - character_width:
#         character_x_pos = screen_width - character_width
        
#     if character_y_pos <0:
#         character_y_pos = 0
#     elif character_y_pos > screen_height - character_height:
#         character_y_pos = screen_height - character_height
    
# # 충돌처리
#     character_rect = character.get_rect()
#     character_rect.left = character_x_pos
#     character_rect.top = character_y_pos
    
#     obstacle_rect = obstacle.get_rect()
#     obstacle_rect.left = obstacle_x_pos
#     obstacle_rect.top = obtacle_y_pos
    
#     if character_rect.colliderect(obstacle_rect):
#         print("충돌")
#         running = False
        
#     screen.blit(backgorund, (0,0))
#     screen.blit(obstacle, (obstacle_x_pos,obtacle_y_pos))
#     screen.blit(character, (character_x_pos,character_y_pos))
    
    
#     # 타이머 - 시간 경과(초단위 표시)
#     elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000
#     timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
#     screen.blit(timer,(10,10))
#     if total_time - elapsed_time <= 0:
#         print("Time Out")
#         running = False


# 게임화면 다시 그리기. 계속 호출되어야 함! 필수!    
    pygame.display.update()    
    

# pygame.time.delay(2000)
# pygame.quit()