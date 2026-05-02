# RoboControl – Robotic Arm Control System

RoboControl is a full-stack robotic arm control system that allows you to control servo motors in real-time using a web interface, a FastAPI backend, and an ESP32 microcontroller.

---

## Overview

This project connects all layers of a robotic system:

---


You can:
- Control joints using sliders
- Send commands over WiFi
- View real-time logs
- Operate a physical robotic arm

---

## Tech Stack

- Frontend: Next.js, Tailwind CSS
- Backend: FastAPI (Python)
- Hardware: ESP32, Servo Motors
- 3D Visualization: React Three Fiber (optional)

---

## Frontend Setup

### 1. Navigate to frontend directory
```bash
cd frontend
npm install
npm run dev
http://localhost:3000
```

---
## Backend Setup

### 1. Navigate to backend directory
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn requests
uvicorn main:app --reload
http://127.0.0.1:8000
```

---

## Objective and Motivation

- Build a complete end-to-end robotic control system from user interface to physical hardware  
- Learn how frontend, backend, and embedded systems communicate in real-time  
- Enable wireless control of a robotic arm using WiFi instead of wired interfaces  
- Create a scalable architecture that can support multiple joints and future automation  
- Develop a modular system where UI, backend, and hardware can be independently improved  

---

## Key Features

- Real-time control of robotic joints using sliders  
- WiFi-based communication between backend and ESP32  
- REST API for sending movement commands  
- Live activity/log system using WebSockets  
- Expandable architecture for adding more servos or sensors  
- Optional 3D visualization of robotic arm movement  

---

## Components List

### Electronics
- ESP32 Development Board  
- Servo Motors (3 to 6 depending on design)  
- External 5V Power Supply (minimum 3A recommended)  
- Jumper Wires (Male-Male / Male-Female)  
- Breadboard (optional)  
- Capacitor (1000µF recommended for stability)  

### Software
- Node.js (Frontend environment)  
- Python 3.x (Backend environment)  
- Arduino IDE (ESP32 programming)  
- Required Libraries:
  - FastAPI  
  - Uvicorn  
  - Requests  
  - ESP32Servo  
  - ArduinoJson

 ---
 ##Website Picture(Controller)

 <img width="1512" height="982" alt="Screenshot 2026-05-02 at 2 51 29 PM" src="https://github.com/user-attachments/assets/215dec0b-4604-4bab-bab9-813f13850d80" />

 ---
 ##Backend Running
 
<img width="1512" height="982" alt="Screenshot 2026-05-02 at 2 54 22 PM" src="https://github.com/user-attachments/assets/78ad57f0-56a2-490e-b934-a716d905d470" />


---
##Fusion(Design)

<img width="1512" height="982" alt="Screenshot 2026-05-02 at 2 55 47 PM" src="https://github.com/user-attachments/assets/67126eda-4edc-48ed-b961-9dad2dfb33fd" />


<img width="1512" height="982" alt="Screenshot 2026-05-02 at 2 55 24 PM" src="https://github.com/user-attachments/assets/26603752-498c-4daf-a206-234f7d7c681a" />

---
##Circuit Diagram

<img width="3024" height="1964" alt="image" src="https://github.com/user-attachments/assets/0eab004e-2dc7-48fe-b08d-50d19e986c0e" />


---

##Components Table


 | # | Component                | Description                                  | Quantity | Notes |
|---|--------------------------|----------------------------------------------|----------|------|
| 1 | ESP32 Dev Board         | Main microcontroller                         | 1        | WiFi + control logic |
| 2 | Servo Motor (SG90)      | Small joints / lightweight movement          | 3–4      | Good for prototype |
| 3 | Servo Motor (MG996R)    | High torque joints (base/arm)                | 2–3      | Metal gear |
| 4 | Servo Driver (PCA9685)  | Controls multiple servos via I2C             | 1        | Optional but recommended |
| 5 | External Power Supply   | 5V–6V for servos                            | 1        | DO NOT power from ESP32 |
| 6 | Breadboard              | Temporary connections                        | 1        | Optional |
| 7 | Jumper Wires            | Connections                                 | 20+      | Male-Female + Male-Male |
| 8 | Robotic Arm Structure   | 3D printed / laser cut parts                 | 1 set    | From Fusion 360 |
| 9 | Gripper Mechanism       | End effector for picking objects             | 1        | Servo controlled |
|10 | Camera Module (ESP32-CAM)| Live feed / vision                          | 1        | Optional |
|11 | WiFi Router             | Communication between UI & ESP32             | 1        | Required for remote control |
|12 | Capacitors (100µF+)     | Stabilize servo power                        | 2–3      | Prevent resets |
|13 | Resistors               | Basic circuit protection                     | Few      | Optional |
|14 | Switch / Emergency Stop | Safety cutoff                                | 1        | Recommended |



