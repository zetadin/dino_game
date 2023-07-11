from curses import wrapper
import curses

def main(stdscr):

    def draw(y,x, what):
        for i,line in enumerate(what.split('\n')):
            stdscr.addstr(y+i, x, line)
            
    # sprite
    dino_sprite = "🦖"
    cacti_sprites = ["🌵", "🌵\n🌵", "🪨"]
    
    # variables
    ground_level=10
    screen_height, screen_width = stdscr.getmaxyx()
    score = 0
    cactus_start = 43
    wait = 0.2
    dino_height = 0
    
    # show everything on screen
    stdscr.clear()
    # draw ground
    draw(ground_level, 0, "⎺"*screen_width)
    # draw dino
    draw(ground_level-1-dino_height, 1, dino_sprite)
    # draw cacti
    draw(ground_level-2, cactus_start-score, cacti_sprites[1])
    
    stdscr.getkey() # wait for a key press before exiting
    stdscr.nodelay(True)
    
    import time
    while(True):
        # show everything on screen
        stdscr.clear()
        # draw ground
        draw(ground_level, 0, "⎺"*screen_width)
        # draw dino
        draw(ground_level-1-dino_height, 1, dino_sprite)
        # draw cacti
        draw(ground_level-2, cactus_start-score, cacti_sprites[1])
        
        # draw score
        draw(ground_level-6, 10, f"score: {score}")
        
        if(cactus_start-score==1 and dino_height == 0):
            draw(ground_level-5, 10, "GAME OVER!")
            stdscr.nodelay(False)
            stdscr.getkey() # wait for a key press before exiting
            break
                    
        score+=1
        dino_height=0
        wait*=0.99
        stdscr.refresh()
        time.sleep(wait)
        try:
            k=stdscr.getkey()
            if(k==' '):
                #jump
                dino_height=1
        except curses.error as e:
            pass
        
wrapper(main)


