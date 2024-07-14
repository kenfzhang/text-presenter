import os
from time import sleep

FRAME_RATE = 60

def render_screen(stuff):
    for i in stuff:
        line = "".join(i)
        print(line)

def create_screen(height, width):
    screen = []
    for i in range(0,height):
        screen.append([])
        for _ in range(0,width):
            screen[i].append(".")
    return screen

def refresh_screen():
    sleep(1/FRAME_RATE)
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop():
    screen = create_screen(10,20)
    while True:
        refresh_screen()
        render_screen(screen)

def main():
    main_loop()

main()
