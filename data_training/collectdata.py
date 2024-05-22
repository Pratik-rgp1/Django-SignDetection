import cv2
import os

# Define the directory to store the images
img_directory = 'SignImage60x60/'
print(os.getcwd())

# Create the main directory and subdirectories if they don't exist
if not os.path.exists(img_directory):
    os.mkdir(img_directory)
if not os.path.exists(f'{img_directory}/blank'):
    os.mkdir(f'{img_directory}/blank')

# Create subdirectories for each letter and digit
for ascii_code in range(65, 91):
    letter = chr(ascii_code)
    if not os.path.exists(f'{img_directory}/{letter}'):
        os.mkdir(f'{img_directory}/{letter}')

for num in range(10):
    if not os.path.exists(f'{img_directory}/{num}'):
        os.mkdir(f'{img_directory}/{num}')

# Initialize webcam
capture = cv2.VideoCapture(0)
while True:
    ret, img_frame = capture.read()
    img_count = {
        'a': len(os.listdir(img_directory + "/A")),
        'b': len(os.listdir(img_directory + "/B")),
        'c': len(os.listdir(img_directory + "/C")),
        'd': len(os.listdir(img_directory + "/D")),
        'e': len(os.listdir(img_directory + "/E")),
        'f': len(os.listdir(img_directory + "/F")),
        'g': len(os.listdir(img_directory + "/G")),
        'h': len(os.listdir(img_directory + "/H")),
        'i': len(os.listdir(img_directory + "/I")),
        'j': len(os.listdir(img_directory + "/J")),
        'k': len(os.listdir(img_directory + "/K")),
        'l': len(os.listdir(img_directory + "/L")),
        'm': len(os.listdir(img_directory + "/M")),
        'n': len(os.listdir(img_directory + "/N")),
        'o': len(os.listdir(img_directory + "/O")),
        'p': len(os.listdir(img_directory + "/P")),
        'q': len(os.listdir(img_directory + "/Q")),
        'r': len(os.listdir(img_directory + "/R")),
        's': len(os.listdir(img_directory + "/S")),
        't': len(os.listdir(img_directory + "/T")),
        'u': len(os.listdir(img_directory + "/U")),
        'v': len(os.listdir(img_directory + "/V")),
        'w': len(os.listdir(img_directory + "/W")),
        'x': len(os.listdir(img_directory + "/X")),
        'y': len(os.listdir(img_directory + "/Y")),
        'z': len(os.listdir(img_directory + "/Z")),
        'blank': len(os.listdir(img_directory + "/blank")),
        '0': len(os.listdir(img_directory + "/0")),
        '1': len(os.listdir(img_directory + "/1")),
        '2': len(os.listdir(img_directory + "/2")),
        '3': len(os.listdir(img_directory + "/3")),
        '4': len(os.listdir(img_directory + "/4")),
        '5': len(os.listdir(img_directory + "/5")),
        '6': len(os.listdir(img_directory + "/6")),
        '7': len(os.listdir(img_directory + "/7")),
        '8': len(os.listdir(img_directory + "/8")),
        '9': len(os.listdir(img_directory + "/9")),
    }

    rows = img_frame.shape[1]
    cols = img_frame.shape[0]
    cv2.rectangle(img_frame, (0, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("data", img_frame)
    img_frame = img_frame[40:300, 0:300]
    cv2.imshow("ROI", img_frame)
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    img_frame = cv2.resize(img_frame, (60, 60))
    key_press = cv2.waitKey(10)

    if key_press & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(img_directory + 'A/' + str(img_count['a'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(img_directory + 'B/' + str(img_count['b'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(img_directory + 'C/' + str(img_count['c'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(img_directory + 'D/' + str(img_count['d'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(img_directory + 'E/' + str(img_count['e'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(img_directory + 'F/' + str(img_count['f'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(img_directory + 'G/' + str(img_count['g'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(img_directory + 'H/' + str(img_count['h'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(img_directory + 'I/' + str(img_count['i'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(img_directory + 'J/' + str(img_count['j'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(img_directory + 'K/' + str(img_count['k'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(img_directory + 'L/' + str(img_count['l'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(img_directory + 'M/' + str(img_count['m'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(img_directory + 'N/' + str(img_count['n'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(img_directory + 'O/' + str(img_count['o'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(img_directory + 'P/' + str(img_count['p'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(img_directory + 'Q/' + str(img_count['q'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(img_directory + 'R/' + str(img_count['r'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(img_directory + 'S/' + str(img_count['s'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(img_directory + 'T/' + str(img_count['t'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(img_directory + 'U/' + str(img_count['u'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(img_directory + 'V/' + str(img_count['v'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(img_directory + 'W/' + str(img_count['w'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(img_directory + 'X/' + str(img_count['x'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(img_directory + 'Y/' + str(img_count['y'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(img_directory + 'Z/' + str(img_count['z'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(img_directory + 'blank/' + str(img_count['blank'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('0'):
        cv2.imwrite(os.path.join(img_directory + '0/' + str(img_count['0'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('1'):
        cv2.imwrite(os.path.join(img_directory + '1/' + str(img_count['1'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('2'):
        cv2.imwrite(os.path.join(img_directory + '2/' + str(img_count['2'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('3'):
        cv2.imwrite(os.path.join(img_directory + '3/' + str(img_count['3'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('4'):
        cv2.imwrite(os.path.join(img_directory + '4/' + str(img_count['4'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('5'):
        cv2.imwrite(os.path.join(img_directory + '5/' + str(img_count['5'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('6'):
        cv2.imwrite(os.path.join(img_directory + '6/' + str(img_count['6'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('7'):
        cv2.imwrite(os.path.join(img_directory + '7/' + str(img_count['7'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('8'):
        cv2.imwrite(os.path.join(img_directory + '8/' + str(img_count['8'])) + '.jpg', img_frame)
    if key_press & 0xFF == ord('9'):
        cv2.imwrite(os.path.join(img_directory + '9/' + str(img_count['9'])) + '.jpg', img_frame)
