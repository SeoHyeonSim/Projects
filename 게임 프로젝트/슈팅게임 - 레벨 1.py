from itertools import count
import pygame
import sys
import os
import random
from time import sleep, time
from pygame.locals import *

pygame.init() # 초기화 

font_shooting = pygame.font.Font(None, 20)

pygame.display.set_caption("GAME NAME")


shooting_screen_width = 500
shooting_screen_height = 630
shooting_screen = pygame.display.set_mode((shooting_screen_width,shooting_screen_height))
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")
smallfont = pygame.font.SysFont(None, 36)
largefont = pygame.font.SysFont(None, 72)

# 게임 오버 텍스트 변수
shooting_gameover_text = largefont.render("Gameover!",True,(225,225,225))
shooting_gameover_rect = shooting_gameover_text.get_rect()                                                                                           #85
shooting_gameover_rect.center = (250, 300)  

# 게임 클리어 텍스트 변수
shooting_gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
shooting_gameclear_rect = shooting_gameover_text.get_rect()                                                                                           #85
shooting_gameclear_rect.center = (250, 300)  

# 그리기 함수
def draw_text(text,font,surface,x,y,main_color):
    text_obj = font.render(text,True,main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj,text_rect)
###############################################################3

# 게임오버 메시지 표시       
def Shooting_gameover_1():
    while True:
        shooting_screen.blit(shooting_gameover_text,shooting_gameover_rect)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
        pygame.display.update()
        pygame.init()
###############################################################3

#게임 클리어 함수
def Shooting_shooting_gameclear_1():
    while True:
        shooting_screen.blit(shooting_gameclear_text,shooting_gameclear_rect)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
        pygame.display.update()
        pygame.init()

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
                'C:/Users/sss/OneDrive/바탕 화면/운석슈팅/images/rock01.png',
                'C:/Users/sss/OneDrive/바탕 화면/운석슈팅/images/rock16.png',
                'C:/Users/sss/OneDrive/바탕 화면/운석슈팅/images/rock25.png',
                'C:/Users/sss/OneDrive/바탕 화면/운석슈팅/images/rock07.png'
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
###################################################################

# 텍스트 그리기 함수
def draw_text(text,font,surface,x,y,main_color):
    text_obj = font.render(text,True,main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj,text_rect)

    
###########################################3
# 운석슈팅 본 게임 함수 
def Shooting_Lv_1():
    pygame.init()
    

    # FPS 설정
    clock = pygame.time.Clock()
    #폰트정의
    font_shooting = pygame.font.Font(None, 30)
    time_font = pygame.font.Font(None,32)
    # 총 시간, 시간계산
    total_time = 60
    start_ticks = pygame.time.get_ticks()

# 게임 오버 텍스트 변수
    shooting_gameover_text = largefont.render("Gameover!",True,(225,225,225))
    shooting_gameover_rect = shooting_gameover_text.get_rect()                                                                                           #85
    shooting_gameover_rect.center = (410, 250)  

    # 게임 클리어 텍스트 변수
    shooting_gameclear_text = largefont.render("Stage Clear!",True,(225,225,225))
    shooting_gameclear_rect = shooting_gameover_text.get_rect()                                                                                           #85
    shooting_gameclear_rect.center = (410, 250) 
    
# 스프라이트 불러오기
    background = pygame.image.load(os.path.join(image_path,"shooting_background.png"))
    
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
            
        dt = clock.tick(60)     # 게임의 프레임 수 설정
            

        for event in pygame.event.get():    # 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
                running = False             # 게임이 진행중이 아님. 

            # 방향키로 전투기 위치 조정
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    fighter.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    fighter.dx +=5
                    
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
                rock = Rock(random.randint(0,shooting_screen_width - 30),0,speed)
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
        draw_text('Life: {}'.format(int(life - count_missed)),font_shooting,shooting_screen, 400,20,(225,225,225))

        
        
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
        Shooting_shooting_gameclear_1()
        


    pygame.display.update()
            
    
    
    pygame.quit()
    
    
        
    
    
    
while True:
    Shooting_Lv_1()
