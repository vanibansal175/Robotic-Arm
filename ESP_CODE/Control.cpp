#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>
#include <ESP32Servo.h> ✅


const char* ssid = "wi-fi";
const char* password = "123456780";

WebServer server(80);

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;

const int BASE_PIN = 13;
const int SHOULDER_PIN = 12;
const int ELBOW_PIN = 14;

int clampAngle(int v) { return max(0, min(180, v)); }

void handleMove() {
  if (!server.hasArg("plain")) {
    server.send(400, "text/plain", "No body");
    return;
  }

  String body = server.arg("plain");

  StaticJsonDocument<200> doc;
  DeserializationError err = deserializeJson(doc, body);
  if (err) {
    server.send(400, "text/plain", "Bad JSON");
    return;
  }

  if (doc.containsKey("base")) {
    int v = clampAngle(doc["base"]);
    baseServo.write(v);
  }
  if (doc.containsKey("shoulder")) {
    int v = clampAngle(doc["shoulder"]);
    shoulderServo.write(v);
  }
  if (doc.containsKey("elbow")) {
    int v = clampAngle(doc["elbow"]);
    elbowServo.write(v);
  }

  server.send(200, "application/json", "{\"status\":\"ok\"}");
}

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(400);
    Serial.print(".");
  }
  Serial.println("\nConnected!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  baseServo.attach(BASE_PIN);
  shoulderServo.attach(SHOULDER_PIN);
  elbowServo.attach(ELBOW_PIN);

  server.on("/move", HTTP_POST, handleMove);
  server.begin();
}

void loop() {
  server.handleClient();
}