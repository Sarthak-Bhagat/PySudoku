# GUIv2.py
# GUI.py
import pygame as pg
from Sudoku import BuildGrid, grid,sb
import time, os, sys
pg.font.init()
start = time.time()

board = grid
solved_board = sb
#print(solved_board)  #Enable for Solution
#board = solved_board #Enable to see final screen
GRAY = [128,128,128]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
WEIRD_YELLOW = [255, 255, 153]
font = pg.font.SysFont(None, 45)
size = [540, 540]
fps = 60
pos = None
strikes = 0

def Draw(screen,pos,strikes):
    pg.init()
    width = size[0]/9
    screen.fill(WHITE)
    print_time(screen)
    Strike(screen,strikes)
    for i in range(1,9):
        if i % 3 == 0 and i != 0:
            thick = 4
        else:
            thick = 1
        pg.draw.line(screen,BLACK,(0, i*size[0]/9), (size[1], i*size[0]/9), thick)
        pg.draw.line(screen,BLACK,(i*size[0]/9, 0), (i*size[0]/9,size[0]) , thick)
    if pos != None: 
        pg.draw.rect(screen, RED,((pos[0]*width)+5 , (pos[1]*width)+5, (size[0]/9 - 9 ), (size[1]/9 - 9 )), 4)
    pg.draw.line(screen,BLACK,(0, 540), (540, 540), 4)
    """ small_font = pg.font.SysFont(None, 45)
    text = small_font.render(str(turn)+'\'s turn', True, BLACK)  
    text_rect = text.get_rect()
    screen.blit(text, (210,620,text_rect[2],text_rect[3]))  """  
    for i in range(9):
        for j in range(9):
            if board[j][i] != 0:
                x_loc = i * (size[0]/9)
                x_loc = x_loc + size[0]/18
                y_loc = j * (size[0]/9)
                y_loc = y_loc + size[0]/18
                text = font.render(str(board[int(j)][int(i)]), True, BLACK) 
                text_rect = text.get_rect()    
                text_rect.centerx = x_loc    
                text_rect.centery = y_loc   
                screen.blit(text, (text_rect[0], text_rect[1], (size[0]/3 - 9 ), (size[1]/3 - 9 )))


def select(pos,screen,strikes):
    pg.init()
    width = size[0]/9
    x = (pos[0] // width) 
    y = (pos[1] // width)
    if board[int(y)][int(x)] != 0:
        main(strikes)
    if pos != None:
        Draw(screen,(x,y),strikes)
    while True:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[1] < 600:
                    Draw(screen,(x,y),strikes)
                    select(mouse_pos,screen,strikes)
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit
                return False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    key = 1
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_2:
                    key = 2
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_3:
                    key = 3
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_4:
                    key = 4
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_5:
                    key = 5
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_6:
                    key = 6
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_7:
                    key = 7
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_8:
                    key = 8
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_9:
                    key = 9
                    Sketch(pos,key,screen,(x,y),strikes)
                if event.key == pg.K_RETURN and key != None:
                    Write((x,y),screen,pos,key,strikes)
        pg.display.update()
    pos = None  

def Write(a,screen,pos,key,strikes):
    x = int(a[1])
    y = int(a[0])
    print(strikes)
    if key == solved_board[x][y]:
        board[x][y] = key
        Draw(screen,pos,strikes)
    else:
        main(strikes+1)

def format_time():
    font1 = pg.font.SysFont(None, 45)
    play_time = round(time.time() - start)
    sec = play_time % 60 
    hr = (play_time//3600)% 24
    min = (play_time//60) % 60
    if play_time < 60:
        play = font1.render('Time: '+f'{sec:02d}', True, BLACK)
    elif min < 60:
        play = font1.render('Time: '+(str(min)+':'+f'{sec:02d}'), True, BLACK)
    else:
        play = font1.render('Time: '+(str(hr)+':'+str(min)+':'+f'{sec:02d}'), True, BLACK)
    
    
    return play

def print_time(screen):
    play_rect = format_time().get_rect()
    play_rect.centerx = 470
    play_rect.centery = 570
    screen.blit(format_time(),play_rect)

def Sketch(pos,key,screen,a,strikes):
    pg.init()
    width = size[0]/9
    Draw(screen,(a[0],a[1]),strikes)
    text = font.render(str(key), True, GRAY) 
    text_rect = text.get_rect()    
    text_rect.centerx = pos[0]    
    text_rect.centery = pos[1]    
    screen.blit(text, (a[0]*width + (width/2 - text.get_width()/2), a[1]*width + (width/2 - text.get_height()/2)))

def Strike(screen,strikes):
    font1 = pg.font.SysFont(None, 20)
    if strikes < 10:
        strike = 'X'*strikes
        play = font.render('Strikes: '+strike, True, BLACK)
    else:
        play = font1.render('Stopped Counting Strikes Since You\'re so bad', True, BLACK)
    play_rect = play.get_rect()
    play_rect.left = 10
    play_rect.centery = 570
    screen.blit(play,play_rect)

def main(strikes):
    os.environ['SDL_VIDEO_CENTERED'] = 'True'
    screen = pg.display.set_mode([540, 600])
    screen.convert()
    pg.display.set_caption('Sudoku') #pylint: disable=undefined-variable
    pg.init()
    while True:
        Draw(screen,None,strikes)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                return False

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[1] < 540:
                    select(mouse_pos,screen,strikes)
            if check(board) != False:
                    Game_Over()
                    return False

        pg.display.update()
    pg.quit()
    sys.exit()

def Game_Over():
    screen1 = pg.display.set_mode([300, 300])
    pg.init()
    time_taken = format_time()
    while True:
        for event in pg.event.get():
            screen1.fill(WHITE)

            time_taken_rect = time_taken.get_rect()
            time_taken_rect.centerx= screen1.get_rect().centerx/2
            time_taken_rect.centery= screen1.get_rect().centery/3+50
            screen1.blit(time_taken, time_taken_rect)
            pg.display.update()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                return False
        

def check(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def Game():
    main(strikes)

Game()