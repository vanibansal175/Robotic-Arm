# RoboControl – robotic arm control system

RoboControl is a full-stack robotic arm control system that allows real time control of a robotic arm using a web interface(that i build), FastAPI backend and ESP32 microcontroller.

# My Objective to build it ?

the main idea behind this project was to understand how software and hardware communicate together in an actual robotics system. instead of only making the robotic arm mechanically, i also wanted to build the complete control architecture behind it.

---

# overview

So lets see how i connected different system together ?

- frontend for controlling the arm
- backend for handling requests
- ESP32 for communicating with hardware
- servo motors for physical movement

the whole system works on wi-fi communication which makes it completely wireless and easy to handle.

---

# what this project can do ?

- control robotic joints using sliders (Frontend)
- send movement commands through WiFi (Common wi-fi)
- monitor live logs and activity (FastApi Backend)
- move actual physical robotic arm in real time

One thing that i make sure is that i make the project modular which helps in development of the model easy in future.
---

# tech stack

### frontend
- Next.js
- Tailwind CSS

### backend
- FastAPI (Python)

### hardware
- ESP32 Development Board
- Servo Motors


---

# frontend setup


```bash
cd frontend
npm install
npm run dev
http://localhost:3000
```

---

# backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn requests
uvicorn main:app --reload
http://0.0.0.0:8000
```

Note - Please run the backend on 0.0.0.0:8000 port because i have setup the cors according to thois only.

---

# objective and motivation

So as io stated that i build this to understand how we can integrate different sectors together.

during this project i learned:

- communication between frontend backend and hardware
- how REST APIs work in robotics ( this is most interesting)
- realtime data transfer using WiFi
- handling servo motor movement through ESP32
- designing scalable architecture for robotics systems

i didn't wanted to only make a robotic arm that moves. i wanted to understand the actual system behind it. 

---

# key features

- realtime robotic arm control
- wireless communication using WiFi
- REST API based architecture (all movents are under one api actions... all 6 movements)
- live logs using websockets(httpx requests)
- 3D visualization (Center robotic arm on web can move)

---

# components used

## electronics

- ESP32 Development Board
- Servo Motors
- 5V external power supply
- jumper wires
- 1000µF capacitor for stability

---

## software

- Node.js
- Python 3.x
- Arduino IDE

### required libraries

- FastAPI
- Uvicorn
- Requests
- ESP32Servo
- ArduinoJson

---

# final thoughts

this project was not only about robotics but also about learning how complete systems are built. 

from frontend to backend to embedded hardware everything is connected together.

this is very interesting project for me because it gave me much more learning than i thought.


there were many small problems during development like WiFi delays servo jitter and backend communication bugs but solving those issues helped me understand robotics systems in much more practical way and i learned a lot.

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


 | # | Component                 | Description                                  | Quantity | Notes | Approx Cost (INR) |
|---|---------------------------|----------------------------------------------|----------|----------------------------|------------------|
| 1 | ESP32 Dev Board           | Main microcontroller                         | 1        | WiFi + control logic       | ₹500 |
| 2 | Servo Motor (SG90)        | Small joints / lightweight movement          | 4        | Good for prototype         | ₹480 |
| 3 | Servo Motor (MG996R)      | High torque joints (base/arm)                | 3        | Metal gear                 | ₹1350 |
| 4 | Servo Driver (PCA9685)    | Controls multiple servos via I2C             | 1        | Optional but recommended   | ₹250 |
| 5 | External Power Supply     | 5V–6V for servos                             | 1        | DO NOT power from ESP32    | ₹400 |
| 6 | Breadboard                | Temporary connections                        | 1        | Optional                   | ₹120 |
| 7 | Jumper Wires              | Connections                                  | 20+      | Male-Female + Male-Male    | ₹150 |
| 8 | Robotic Arm Structure     | 3D printed / laser cut parts                 | 1 set    | From Fusion 360            | ₹1800 |
| 9 | Gripper Mechanism         | End effector for picking objects             | 1        | Servo controlled           | ₹350 |
|10 | Camera Module (ESP32-CAM) | Live feed / vision                           | 1        | Optional                   | ₹650 |
|12 | Capacitors (100µF+)       | Stabilize servo power                        | 3        | Prevent resets             | ₹50 |
|13 | Resistors                 | Basic circuit protection                     | Few      | Optional                   | ₹30 |
|14 | Switch / Emergency Stop   | Safety cutoff                                | 1        | Recommended                | ₹80 |

---

## Total Estimated Cost
**~ ₹4,930**




