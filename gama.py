#!/usr/bin/env python3
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

WIDTH = 20
HEIGHT = 10
MAX_SCORE = (WIDTH-2)*(HEIGHT-2)

COLOR_FOOD = 1
COLOR_SNAKE = 2

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    curses.start_color()
    curses.init_pair(COLOR_FOOD, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(COLOR_SNAKE, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Fare olaylarını etkinleştir
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    
    snake = [[4, 4], [4, 3], [4, 2]]
    direction = KEY_RIGHT
    food = [randint(1, HEIGHT-2), randint(1, WIDTH-2)]
    score = 0
    
    while True:
        key = stdscr.getch()
        
        # Dokunma olaylarını kontrol et
        if key == curses.KEY_MOUSE:
            try:
                _, mx, my, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON1_PRESSED:
                    head_y, head_x = snake[0][0], snake[0][1]
                    
                    # Dokunulan yöne göre hareket
                    dx = mx - head_x
                    dy = my - head_y
                    
                    if abs(dx) > abs(dy):
                        new_dir = KEY_RIGHT if dx > 0 else KEY_LEFT
                    else:
                        new_dir = KEY_DOWN if dy > 0 else KEY_UP
                    
                    # Ters yöne engel
                    if (direction, new_dir) not in [(KEY_LEFT, KEY_RIGHT), 
                                                   (KEY_RIGHT, KEY_LEFT),
                                                   (KEY_UP, KEY_DOWN),
                                                   (KEY_DOWN, KEY_UP)]:
                        direction = new_dir
            except:
                pass
        
        # Yılan hareketi
        head = [snake[0][0], snake[0][1]]
        if direction == KEY_UP: head[0] -= 1
        elif direction == KEY_DOWN: head[0] += 1
        elif direction == KEY_LEFT: head[1] -= 1
        elif direction == KEY_RIGHT: head[1] += 1
        
        # Çarpışma kontrolü
        if (head[0] in [0, HEIGHT-1] or 
            head[1] in [0, WIDTH-1] or 
            head in snake):
            break
            
        snake.insert(0, head)
        
        # Yem yeme
        if head == food:
            score += 1
            if score == MAX_SCORE: break
            while True:
                food = [randint(1, HEIGHT-2), randint(1, WIDTH-2)]
                if food not in snake: break
        else:
            snake.pop()
        
        # Çizim
        stdscr.clear()
        stdscr.border(0)
        for y, x in snake:
            stdscr.addch(y, x, 'O', curses.color_pair(COLOR_SNAKE))
        stdscr.addch(food[0], food[1], '@', curses.color_pair(COLOR_FOOD))
        stdscr.addstr(0, 2, f'Skor: {score} ')
        stdscr.refresh()
    
    # Oyun sonu
    stdscr.nodelay(0)
    stdscr.addstr(HEIGHT//2, WIDTH//2-5, 'GAME OVER!')
    stdscr.addstr(HEIGHT//2+1, WIDTH//2-8, f'Skorun: {score}')
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
