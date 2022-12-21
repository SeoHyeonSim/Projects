""" tetris.py - Copyright 2016 Kenichiro Tanaka """
import sys
from math import sqrt
from random import randint
import pygame
import os

# 전역 변수




pygame.init()
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


current_path = os.path.dirname(__file__) # 현재파일 위치 반환
image_path = os.path.join(current_path,"images")
Tetris_backgorund = pygame.image.load(os.path.join(image_path,"tetris-background.png"))
error_image = pygame.image.load(os.path.join(image_path,"error.png"))

BLACK = (0,0,0)
pygame.key.set_repeat(30, 30)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 630
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
WIDTH = 15
HEIGHT = 22
INTERVAL_3 = 17
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
        self.fire = count + INTERVAL_3

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
            self.fire = count + INTERVAL_3
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
    
# # 다음에 나올 블록 보여주기
# def draw_next_block():          
#     for y_offset in range(NEXT_BLOCK.size):
#             for x_offset in range(NEXT_BLOCK.size):
#                 index = y_offset * NEXT_BLOCK.size + x_offset
#                 val = NEXT_BLOCK.data[index]
#                 # 블록을 보여줄 자리 설정
#                 f_xpos = 440 + (x_offset) * PIECE_GRID_SIZE
#                 f_ypos = 100 + (y_offset) * PIECE_GRID_SIZE
#                 pygame.draw.rect(screen, COLORS[val],
#                                 (f_xpos, 
#                                 f_ypos, 
#                                 PIECE_SIZE, 
#                                 PIECE_SIZE))
# 점수 표시         
def draw_score(score):
    # 스코어는 6자리로 표기
    score_str = str(score).zfill(6)
    score_image = smallfont.render(score_str, True, (255,255,255))
    screen.blit(score_image, (700, 30))
    pass

# 게임오버 메시지 표시       
def Gameover_screen():
    while True:
        screen.blit(Gameover_text,Gamover_rect)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
        pygame.display.update()
        pygame.init()
        
#게임 클리어 함수
def Gameclear_screen():
    while True:
        screen.blit(Gameclear_text,Gameclear_rect)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                    
        pygame.display.update()
        pygame.init()
###################################################33
# 테트리스 본 게임 함수
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
        
        screen.blit(Tetris_backgorund,(0,0))
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
            if score >= 5000:
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
        
        Gameover_screen()
        pygame.display.update()
        
    # 게임 클리어 메시지
    if Gamewin and not running:
        Gameclear_screen()
        pygame.display.update()
        
    pygame.display.update()


while True:
    Tetris_Lv_3()
