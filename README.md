# 🎮 Hill Climb Racing - Hand Gesture Controller

Control your Hill Climb Racing game 🚗 using **hand gestures** and your **webcam**!  
This project uses **Computer Vision** and **Automation** to simulate keyboard key presses based on the number of fingers you show on the camera.

---

## 🛠 Features

- ✋ Detects hand gestures using OpenCV and cvzone.
- 🎮 Controls game acceleration ("Gas") and braking ("Brake") automatically.
- ⚡ Real-time gesture detection.
- 🧠 Smart "Neutral" detection when no action is needed.
- 🎨 Visual feedback with dynamic UI (Gas, Brake, Neutral displayed in colorful circles).

---

## 🏗 Architecture

```plaintext
+-----------------+
|  Webcam Input   |
+-----------------+
         ↓
+-------------------------+
| Frame Capture (OpenCV)  |
+-------------------------+
         ↓
+------------------------------------+
| Hand Detection (cvzone HandModule) |
+------------------------------------+
         ↓
+-----------------------------+
| Finger Count Calculation    |
+-----------------------------+
         ↓
+----------------------------------+
| Gesture Interpretation (Gas/Brake/Neutral) |
+----------------------------------+
         ↓
+----------------------------+
| Simulate Key Press (pyautogui) |
+----------------------------+
         ↓
+---------------------+
| Control Hill Climb   |
| Racing Game 🚗       |
+---------------------+
```


## 📦 Technologies Used

- **Python 3.9+**
- **OpenCV** - Real-time image processing.
- **cvzone** - Simplified hand tracking.
- **pyautogui** - Keyboard automation for game control.
- **HandTrackingModule** (from cvzone) - Finger detection.

---

## 🚀 How to Run the Project

### Clone the Repository:
```bash
git clone https://github.com/aayu12345/HillClimb-HandGesture-Controller.git
```

### Install required Libraries:
```bash
pip install opencv-python cvzone pyautogui
```

### Setup:

1 - Run the script using :
```bash
python HillClimb.py
```
2 - Open Hill Climb Racing on your PC.

3 - Allow webcam access.

4 - Show 5 fingers to accelerate (presses Right Arrow key).

5 - Show 0 fingers (closed fist) to brake (presses Left Arrow key).

6 - Show any other number of fingers to stay Neutral.


