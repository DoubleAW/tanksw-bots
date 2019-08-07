import pyautogui,time
from PIL import ImageGrab

pyautogui.FAILSAFE = True
time.sleep(1)
h = 190
new_h = 0
click_time = time.time()
start_time = time.time()
b_break = False
while True:    
    screen = ImageGrab.grab(bbox=(753,269,1147,714))
    c_break = False
    for y in range(425, 124, -150):
        if c_break == True:
            break
        for x in range(0, 394, 131):
                
            r,g,b = screen.getpixel((x, y))
            if r == 17 and g == 17 and b == 17:

                print(time.time() - start_time)
                pyautogui.click(x + 753, (y + h) + 40)
                c_break = True
                break
            if r == 251 and g == 62 and b == 56:
                time.sleep(3) 
                pyautogui.click(1050, 771)
                c_break = True
                time.sleep(1)
                start_time = time.time() 
                break
    if time.time() - start_time >= 2:
        while True:
            if b_break:
                break
            screen = ImageGrab.grab(bbox=(753, 320, 1147, 361))
            for x in range(0, 394, 131):
                r,g,b = screen.getpixel((x, 10))
                if r == 17 and g == 17 and b == 17:
                    if time.time() - click_time > 3 and new_h < 140:
                        new_h += 10
                        click_time = time.time()
                    pyautogui.click(x + 753,  330 + new_h)

                    break
                if r == 251 and g == 62 and b == 56:
                    time.sleep(3)
                    pyautogui.click(1050, 771)
                    time.sleep(1)
                    start_time = time.time()
                    b_break = True
                    break


        
   
			