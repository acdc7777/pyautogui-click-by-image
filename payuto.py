import pyautogui
pyautogui.FAILSAFE = True
pyautogui.useImageNotFoundException()

def pyau_click(pathimg):
    loop = 0
    while True:
        try:
            locate = pyautogui.locateOnScreen(pathimg,confidence=0.8)
            
            if locate != None:
                pyautogui.move(locate)
                pyautogui.click(locate)
                break
            print('image found')
            
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            
        loop+=1
        if loop == 5:break
