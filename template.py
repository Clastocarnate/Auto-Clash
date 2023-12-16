import mss
import cv2
import screeninfo
import time
import pyautogui as pg



def Open(template):
    with mss.mss() as ss:
        screenshot = ss.shot(output='screen.png')
    primary = screeninfo.get_monitors()
    s_width = primary[0].width
    s_height = primary[0].height
    screen = cv2.imread("screen.png", 0)
    screen = cv2.resize(screen, (s_width, s_height))


    h, w = template.shape


    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
            cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


    result = cv2.matchTemplate(screen, template, cv2.TM_SQDIFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = min_loc


    br = (location[0] + w, location[1] + h)
    x = location[0] + w//2
    y = location[1] + h//2
    centre = (x,y)
    pg.click(centre)
    # cv2.rectangle(screen, location, br, 255, 5)
    # cv2.circle(screen,centre,5,(255,255,255),5)
    # cv2.imshow('Match', screen)
    # cv2.waitKey(0)

    # cv2.destroyAllWindows()



primary = screeninfo.get_monitors()
s_width = primary[0].width
s_height = primary[0].height

Barracks = cv2.imread("Assets/Barracks.png", 0)
Train = cv2.imread("Assets/Train_troops.png",0)
cross = cv2.imread("Assets/cross.png",0)
Barbarian = cv2.imread("Assets/Barbarian.png",0)
Mathmaking = cv2.imread("Assets/Matchmaking.png",0)
Deploy = cv2.imread("Assets/Deploy.png",0)
Attack = cv2.imread("Assets/Attack.png",0)
Back = cv2.imread("Assets/Back.png",0)

time.sleep(3)

while True:
    Open(Barracks)
    time.sleep(3)
    Open(Train)
    time.sleep(3)
    for i in range(60):
        Open(Barbarian)
    time.sleep(150)
    Open(cross)
    time.sleep(2)
    pg.press('space')
    time.sleep(1)
    Open(Mathmaking)
    time.sleep(10)
    Open(Attack)
    time.sleep(1)
    for i in range(60):
        Open(Deploy)
    time.sleep(120)
    Open(Back)
    time.sleep(3)
