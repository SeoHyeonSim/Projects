import pygame
import sys
import os


pygame.init() # 초기화 

game_font = pygame.font.Font(None, 40)
screen_width = 800
screen_height = 630
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("GAME NAME")




# 공부수기 게임 함수 
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


    #     # 게임 종료 출력
    # if running != True and Gameover :
    #     pygame.time.delay(2000)     # 2초 대기
    #     GAMEOVER(game_result)       # 게임오버 함수 실행
    # elif running != True:
    #     pygame.time.delay(2000)
    #     YouWin(game_result)
    # pygame.display.update()


    # 게임 종료 출력
    msg = game_font.render(game_result,True,(255,255,255) )
    msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))
    screen.blit(msg, msg_rect)
    pygame.display.update()
            
    pygame.time.delay(2000)
    
    
    pygame.quit()
    
    
        
    
    
    
while True:
    BallGame_LV_1()
