# Hand Tracking Object Control Demo

This project was my **first time learning OpenCV and real-time hand tracking**.

The goal of this project was simple: use hand tracking to detect the position and motion of a hand, then use that input to control an object in **2D space**. It started as an experiment to understand how computer vision can turn human movement into interactive controls.

More than anything, this project was a learning milestone for me. It helped me understand how webcam input, landmark detection, gesture logic, and object movement can all work together in one real-time system.

---

## Demo Video

Add your demo video here.

[![Watch the demo](./images/demo-thumbnail.png)](PASTE_VIDEO_LINK_HERE)

Or use a direct link:

[Watch the demo](PASTE_VIDEO_LINK_HERE)

---

## What this project is

This is a computer vision demo that tracks a user’s hand through a webcam and uses that movement to control an object on screen.

The system uses hand landmarks to:

- detect the hand in real time
- track finger positions
- measure pinch gestures
- estimate hand rotation
- move and rotate a 2D object based on those gestures

In this demo, the tracked hand controls a circular object in 2D space, allowing me to experiment with gesture-based interaction.

---

## Why I built this

This project was mainly built as a way for me to learn:

- how OpenCV works in real-time applications
- how to use MediaPipe hand landmarks
- how gesture detection can be turned into interactive controls
- how computer vision systems process and react to movement frame by frame

At the time, I wanted to understand the basics of hand tracking and object control before trying anything more creative.

This project gave me that foundation.

---

## What it does

The system captures live webcam input and processes each frame to detect a hand.

Once a hand is detected, it:

- draws the hand landmarks on screen
- tracks the thumb and index finger positions
- detects when the fingers come close together as a pinch
- uses that pinch gesture to interact with the object
- calculates hand rotation and applies that movement to the object

The result is a simple but interactive demo where a tracked hand can influence the position and angle of a visual object in real time.

---
## Demo Video

Watch the demo here: [IMG_9132.mov](./Demo/IMG_9132.mov)

## Tech stack

This project was built with:

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **PyAutoGUI**

### Main libraries used

- **OpenCV** for webcam capture, frame processing, drawing, and display
- **MediaPipe** for hand landmark detection and tracking
- **NumPy** for vector math and geometric calculations
- **math** for distance and angle calculations

---

## How it works

### 1. Webcam capture
The program opens the webcam and continuously reads live frames.

### 2. Hand detection
Each frame is converted into RGB and passed into MediaPipe Hands, which returns hand landmarks if a hand is visible.

### 3. Landmark extraction
The detected hand landmarks are converted into pixel coordinates so they can be used for gesture and movement logic.

### 4. Pinch detection
The distance between the thumb tip and index finger tip is measured. If the fingers are close enough, the system treats that as a pinch gesture.

### 5. Rotation logic
The program computes the angle between hand landmark vectors to estimate rotational movement and uses that to rotate the object.

### 6. 2D object control
A ball-like object is drawn on screen, and its state changes based on the tracked hand gestures and movement.

---

## What I learned

This project taught me a lot about how real-time vision systems actually work.

Some of the biggest things I learned were:

- how to process webcam frames continuously in Python
- how hand landmarks can be used as structured input instead of raw pixels
- how to detect gestures using simple geometric logic
- how to translate human motion into object movement in a visual interface
- how to debug noisy real-time systems where movement is not always perfectly stable

Most importantly, this was the project that helped me go from just hearing about OpenCV to actually building something interactive with it.

---

## Why this project mattered to me

This project was important because it was my first real hands-on step into computer vision.

Before this, hand tracking and gesture control felt abstract. After building this, I started to understand how those systems are actually put together.

It also directly helped me build another project later: **Finger Music**.

A lot of what I learned here about landmark tracking, gesture detection, and mapping finger motion into system behavior became the foundation for that later repo.

So while this project is a smaller demo, it was a very important stepping stone.

---

## Connection to my later project

This project directly influenced and helped me build **Finger Music**, another repo based on what I learned here.

In this demo, I learned the core building blocks:

- hand landmark detection
- real-time gesture tracking
- mapping finger positions to digital behavior
- handling live webcam interaction

Those same concepts later became the base for building more creative interaction systems.

This repo was the practice ground that made that possible.

---

## Running the project locally

### Prerequisites

Make sure you have Python installed, then install the required packages:

```bash
pip install opencv-python mediapipe numpy pyautogui
