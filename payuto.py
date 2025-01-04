import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
# driver.get("https://www.google.com/recaptcha/api2/demo")
# driver.get("https://www.cloudflare.com/zero-trust/interactive-demo/")
time.sleep(5)
# scr = driver.find_element("xpath",'//*[@id="gatsby-focus-wrapper"]/div/div[3]/div/div/div/div[2]/div/section/form/div[9]/div')
# driver.execute_script("arguments[0].scrollIntoView(true);", scr)
# driver.maximize_window()


driver.switch_to.new_window("tab")

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

def pyau_click(pathimg):
    import pyautogui
    pyautogui.FAILSAFE = True
    pyautogui.useImageNotFoundException()
    
    loop = 0
    while True:
        try:
            locate = pyautogui.locateOnScreen(pathimg,confidence=0.8)
            
            if locate != None:
                # pyautogui.alert('This is the message to display.')
                pyautogui.move(locate)
                pyautogui.click(locate)
                break
            print('image found')
            
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            
        loop+=1
        if loop == 5:break
        
# pyau_click("cloudflar.png")


def pyau():
    pass
    # ele = driver.find_element("xpath", '//div[@class="a4bIc"]')
    # x= ele.location["x"]
    # y= ele.location["y"]
    # print(x, y)

    screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    print(screenWidth, screenHeight)

    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    print(currentMouseX , currentMouseY)

    # pyautogui.moveTo(x, y) # Move the mouse to XY coordinates.

    pyautogui.click()          # Click the mouse.
    # pyautogui.click(x, y)  # Move the mouse to XY coordinates and click it.

    pyautogui.moveTo(r"E:\seleniumBase_\sea.png") # Find where button.png appears on the screen and click it.
    pyautogui.click(r"E:\seleniumBase_\sea.png") # Find where button.png appears on the screen and click it.



    pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
    pyautogui.doubleClick()    # Double click the mouse.
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

    pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

    pyautogui.keyDown('shift') # Press the Shift key down and hold it.
    pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
    pyautogui.keyUp('shift')   # Let go of the Shift key.

    pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

    pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked