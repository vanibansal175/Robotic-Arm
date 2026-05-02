from fastapi import APIRouter
from routes.logs import broadcast_log
import requests


router = APIRouter(prefix="/actions")
ESP32_URL = "http://10.81.11.75 /move"  

joint_state = {
    "base": 0,
    "shoulder": 0,
    "elbow": 0,
    "wristTilt": 0,
    "wristRotation": 0,
    "gripper": 0,
}


@router.post("/home")

async def go_home():
    await broadcast_log("Moving to Home position","info")
    return {"status":"home"}


@router.post("/ready")

async def ready():
    await broadcast_log("Robot is Ready", "success")
    return {"status":"ready"}


@router.post("/pick")

async def pick():
    await broadcast_log("Pick command executed", "success")
    return {"status":"pick"}


@router.post("/place")
async def place():
    await broadcast_log("Place command executed", "success")
    return {"status":"place"}



@router.post("/stop")

async def stop():
    await broadcast_log("Emergency STOP triggered", "error")
    return {"status":"stopped"}


@router.post("/move")
async def move_joint(data: dict):

    joint = data.get("joint")
    value = data.get("value")

    if joint not in joint_state:
        print("Invalid joint:", joint)
        return {"error": "Invalid joint"}

    joint_state[joint] = value

    print("Received:", joint, value)

    await broadcast_log(f"{joint} moved to {value}", "info")

    try:
        requests.post(
            ESP32_URL,
            json={joint: value},
            timeout=0.5
        )
    except Exception as e:
        print("ESP32 not reachable:", e)

    return {"status": "ok"}
