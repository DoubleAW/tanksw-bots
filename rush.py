import pyautogui,time
from PIL import ImageGrab

up = (197, 412)
left = (123, 412)
right = (260, 412)
down = (197, 550)
cent = (197, 75)
time.sleep(1)
a = [up, left, down, right]
while True:
    screen = ImageGrab.grab(bbox=(753,269,1147,899))
    
    cr, cg, cb = screen.getpixel((cent))
    print(cr, cg, cb)
    if cr == 255 and cg == 255 and cb == 255:
        continue
    for i in range(0, 4):
        print(i)
        r,g,b = screen.getpixel((a[i][0], a[i][1]))
        if cr == r and cg == g and cb == b:
            pyautogui.click(197 + 753, 412 + 269, i)
            break
