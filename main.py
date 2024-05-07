import cv2
import pyfirmata
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

# Define the LED control function
def led(fingerUp, *led_pins):
    for pin, state in zip(led_pins, fingerUp):
        pin.write(state)

# Initialize HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Initialize pyFirmata board
board = pyfirmata.Arduino('COM7')

# Define LED pins
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        # Control LEDs based on finger gestures
        led(fingerUp, led_1, led_2, led_3, led_4, led_5)

        # Display finger gesture information on frame
        print(fingerUp)
        count = fingerUp.count(1)
        print(count)
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'off', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        # Add more conditions to display different gestures

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()