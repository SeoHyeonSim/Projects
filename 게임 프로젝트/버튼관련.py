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
    start = True
    while start:
        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False 
                sys.exit()
            

        screen.blit(backgorund, (0,0))
        Button(startScreen_start, 405, 250, 150, 80, startScreen_start_click, 380, 235, game)
        Button(startScreen_explain, 405, 350, 150, 80, startScreen_explain_click, 380, 335, explain)
        Button(startScreen_finish, 405, 450, 150, 80, startScreen_finish_click, 380, 435, finishgame)

        font = pygame.font.Font(None,80)
        title = font.render("MiniGame Wonderland",True, (0,0,0))

        screen.blit(title,(80,100))
        
        pygame.display.update()  


class Button():
    def __init__(self, x, y, width, height, img_act , x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action is not None:  # 마우스가 버튼안에서 클릭되었을 때
                time.sleep(0.2)
                action()
        else:
            screen.blit(img_in, (x, y))

running = True
while running:
    
            
            
    
    startScreen()
    
    
    

    
    
    



# 게임화면 다시 그리기. 계속 호출되어야 함! 필수!    
    pygame.display.update()    
    


