from pico2d import *


TUK_WIDTH , TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground=load_image('TUK_GROUND.png')
character = load_image('pngwing.com.png')

x,y=TUK_WIDTH//2,TUK_HEIGHT//2

running = True
dir=0
dir2=0
left_right=0
division=True
def handle_events():
    global running, dir,dir2,left_right,division
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                left_right = 1
                division = True
            elif event.key == SDLK_LEFT:
                dir -= 1
                left_right = 0
                division = True
            elif event.key == SDLK_UP:
                dir2 += 1
                division = False
            elif event.key == SDLK_DOWN:
                dir2 -= 1
                division = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1



frame=0
frame2=0
while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if division:
        if dir==-1:
            character.clip_draw(128 * frame, 0, 128, 128, x, y)
        if dir==1:
            character.clip_composite_draw(128*frame, 0,128, 128, 0,'h',x, y,128,128)
        if dir==0:
            if left_right==0:
                character.clip_draw(0, 128*9, 128, 128, x, y)
            if left_right == 1:
                character.clip_composite_draw(0, 128*9,128, 128, 0,'h',x, y,128,128)
    else:
        if dir2==-1:
            if left_right == 0:
                character.clip_draw(128 * frame, 0, 128, 128, x, y)
            if left_right == 1:
                character.clip_composite_draw(128*frame, 0,128, 128, 0,'h',x, y,128,128)
        if dir2==1:
            character.clip_draw(128*frame2, 128*4,128, 128,x, y)
        if dir2 == 0:
            if left_right == 0:
                character.clip_draw(0, 128 * 9, 128, 128, x, y)
            if left_right == 1:
                character.clip_composite_draw(0, 128 * 9, 128, 128, 0, 'h', x, y, 128, 128)
    update_canvas()
    handle_events()
    if running==False:
        break
    frame = (frame + 1) % 10
    frame2 = (frame2 + 1) % 8
    x += dir * 10
    y += dir2 * 10
    delay(0.05)









