import pyautogui, time
import sys
from PIL import ImageGrab
DEBUG = True
YELLOW = (248, 231, 30)
RED = (255, 21, 67)
BLUE = (19, 177, 251)
GREEN = (68, 195, 116)

def dprint(*args, **kwargs):
    if DEBUG == True:
        for ar in args:
            print(ar)

def color_locs():
    screen = ImageGrab.grab(bbox=(826,609,1072,854))
    up = (77, 10)
    left = (1, 30)
    right = (240, 30)
    down = (77, 230)
    a = [up, left, down, right]
    for i in range(0, 4):
        r,g,b = screen.getpixel((a[i][0], a[i][1]))
        if (r,g,b) == YELLOW:
            yellowt = i
        elif (r,g,b) == RED:
            redt = i
        elif (r,g,b) == GREEN:
            greent = i
        elif (r,g,b) == BLUE:
            bluet = i
        else:
            dprint(f'Color at {a[i]} not found')
            sys.exit(-1)
    return redt, bluet, greent, yellowt


cent = (15, 20)
red_click, blue_click, green_click, yellow_click = color_locs()
rotate = lambda clicks: [x - clicks if x - clicks > 0 else (x - clicks) % 4 for x in [red_click, blue_click, green_click, yellow_click]]
while True:
    screen = ImageGrab.grab(bbox=(933,271,964,595))
    for i in range(20, 5, -1):
        cr, cg, cb = screen.getpixel((15, i))
        orb_loc = (cr, cg, cb)
        if orb_loc != RED and orb_loc != GREEN and orb_loc != YELLOW and orb_loc != BLUE:
            if orb_loc != (255, 255, 255):
                dprint(orb_loc)    
            continue
        dprint(f'red_click: {red_click}\nblue_click: {blue_click}\ngreen_click: {green_click}\nyellow_click:{yellow_click}\n\n')
        if orb_loc == RED:
            dprint('orb == red\n')
            pyautogui.click(950, 681, red_click)
            red_click, blue_click, green_click, yellow_click = rotate(red_click)
            break
        elif orb_loc == BLUE:
            dprint('orb == blue\n')
            pyautogui.click(950, 681, blue_click)
            red_click, blue_click, green_click, yellow_click = rotate(blue_click)
            break
        elif orb_loc == GREEN:
            dprint('orb == green\n')
            pyautogui.click(950, 681, green_click)
            red_click, blue_click, green_click, yellow_click = rotate(green_click)
            break
        elif orb_loc == YELLOW:
            dprint('orb == yellow\n')
            pyautogui.click(950, 681, yellow_click)
            red_click, blue_click, green_click, yellow_click = rotate(yellow_click)
            break
        else:
            dprint(f'dafuq: {orb_loc}')
            break
