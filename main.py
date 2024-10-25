import pyautogui
import time

cookieX, cookieY = 287, 540
upgradeX, upgradeY = 1630, 260

# move to cookie
pyautogui.moveTo(cookieX, cookieY, 1)
time.sleep(0.1)

# click 16 times (15 + 1, to enter window)
for i in range(16):
    pyautogui.click()

while True:
    shopX, shopY = 1760, 980
    
    pyautogui.moveTo(upgradeX, upgradeY, 0.25)
    time.sleep(0.01)
    pyautogui.click()

    for i in range(11):
        # move to building
        pyautogui.moveTo(shopX, shopY, 0.25)
        #time.sleep(0.26)
        pyautogui.click()
        shopY = shopY - 60

    

    # click cookie 100 times
    pyautogui.moveTo(cookieX, cookieY, 1)
    time.sleep(1)
    for i in range(100):
        pyautogui.click()



#click for 30 seconds
#startTime = time.time()
    #while time.time() - startTime < 30:
        #pyautogui.click()