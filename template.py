import mss
import cv2
import screeninfo

# with mss.mss() as ss:
#     screenshot = ss.shot(output='screen.png')

primary = screeninfo.get_monitors()
s_width = primary[0].width
s_height = primary[0].height

# Read and resize the screenshot
screen = cv2.imread("screen.png", 0)
screen = cv2.resize(screen, (s_width, s_height))

# Read the template
template = cv2.imread("Assets/Barracks.png", 0)

# Get template dimensions
h, w = template.shape

# Template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
           cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = screen.copy()
    result = cv2.matchTemplate(img2, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    br = (location[0] + w, location[1] + h)
    x = location[0] + w//2
    y = location[1] + h//2
    centre = (x,y)
    cv2.rectangle(img2, location, br, 255, 5)
    cv2.circle(img2,centre,5,(255,255,255),5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)

cv2.destroyAllWindows()
