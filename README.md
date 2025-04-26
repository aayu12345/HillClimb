# 🎮 Hill Climb Racing - Hand Gesture Controller

Control your Hill Climb Racing game 🚗 using **hand gestures** and your **webcam**!  
This project uses **Computer Vision** and **Automation** to simulate keyboard key presses based on the number of fingers you show on the camera.

---

## 🛠 Features

- ✋ Detects hand gestures using OpenCV and cvzone.
- 🎮 Controls game acceleration ("Gas") and braking ("Brake") automatically.
- ⚡ Real-time gesture detection.
- 🧠 Smart "Neutral" detection when no action is needed.
- 🎨 Visual feedback with dynamic UI (gas, brake, neutral shown inside colorful circles).

---

## 🏗 Project Architecture



## 🏗 Project Architecture

```mermaid
flowchart TD
    A[Webcam Input] --> B[Frame Capture (OpenCV)]
    B --> C[Hand Detection (cvzone HandTrackingModule)]
    C --> D[Finger Count Calculation]
    D --> E[Gesture Interpretation (Gas / Brake / Neutral)]
    E --> F[Simulate Key Press (pyautogui)]
    F --> G[Control Hill Climb Racing Game 🚗]



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
cd HillClimb-HandGesture-Controller


