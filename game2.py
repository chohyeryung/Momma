import pygame

pygame.init() #초기화 반드시 필요함

#창크기
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("아이에게 좋은것만 먹이세요")

#배경이미지 불러오기
background = pygame.image.load("D:\Momma\Background.png")

#이벤트 루프 없으면 창 바로 꺼짐
running = True

while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는지
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 실행되었는지
            running = False

    # screen.fill(()) RGB컬러로도 화면 채우기 가능
    screen.blit(background, (0,0))
    pygame.display.update() #화면을 계속해서 호출해야 함

#py게임 종료
pygame.quit()