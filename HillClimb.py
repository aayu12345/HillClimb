import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui

# Define the custom function
def putTextInCircle(img, text, center, radius, textColor, circleColor, thickness=4):
    # Draw the circle
    cv2.circle(img, center, radius, circleColor, -1)
    
    # Get the text size
    text_size,baseline= cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    
    # Calculate the text position to center it in the circle
    text_x = center[0] - text_size[0] // 2
    text_y = center[1] + text_size[1] // 2 -baseline //2
    
    # Draw the text inside the circle
    cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 2)

# Initialize video capture
cap = cv2.VideoCapture(1)  # Use 0 for the default camera
detector = HandDetector(detectionCon=0.6, maxHands=1)

while True:
    # Capture frame from camera
    success, img = cap.read()
    if not success:
        break

    # Detect hands and find landmarks
    hands, img = detector.findHands(img)
    
    if hands:
        # Get the landmark list
        lmlst = hands[0]['lmList']
        # Count fingers
        fingers = detector.fingersUp(hands[0])
        finger_count = fingers.count(1)
        
        # Determine action based on the number of fingers up
        if finger_count == 5:
            pyautogui.keyDown('right') 
            pyautogui.keyUp('left') # Press the gas
            putTextInCircle(img, 'GAS!', (100, 100), 90, (0,0,0), (255, 165, 0))
        elif finger_count == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')  # Press the brake
            putTextInCircle(img, 'BRAKE!', (100, 100), 90, (0,0,0), (0, 0, 255))
        else:
            pyautogui.keyUp('right')   # Release the gas
            pyautogui.keyUp('left')  # Release the brake
            putTextInCircle(img, 'NEUTRAL', (100, 100), 90, (0,0,0), (0, 255, 255))

    # Display the image
    cv2.imshow("Hill Climb Racing Controller", img)
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
