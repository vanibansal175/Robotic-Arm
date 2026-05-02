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


