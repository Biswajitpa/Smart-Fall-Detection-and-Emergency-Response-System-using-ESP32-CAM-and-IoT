#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// ===== WIFI =====
const char* ssid = "biswajit";
const char* password = "12345678";

WebServer server(80);

// ===== OLED =====
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// ===== MOTOR =====
#define M1 12
#define M2 13
#define M3 14
#define M4 27

// ===== SENSORS =====
#define TRIG 5
#define ECHO 18

#define SOUND_SENSOR 35   // 🔊 Digital sound (DO)
#define PIR_SENSOR 32     // 👣 Motion
#define PROX_SENSOR 33    // 📍 Proximity
#define PULSE_PIN 34      // ❤️ Pulse sensor

// ===== BUZZER =====
#define BUZZER 4

// ===== HEART RATE =====
int threshold = 1800;
unsigned long lastBeatTime = 0;
int bpm = 0;

// ===== MOTOR STOP =====
void stopMotors() {
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
  digitalWrite(M3, LOW);
  digitalWrite(M4, LOW);
}

// ===== FALL RECEIVED =====
void handleFall() {
  Serial.println("🚨 FALL RECEIVED!");

  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("FALL ALERT!");
  display.display();

  digitalWrite(M1, HIGH);
  digitalWrite(M2, HIGH);
  digitalWrite(M3, HIGH);
  digitalWrite(M4, HIGH);
  digitalWrite(BUZZER, HIGH);

  delay(5000);

  stopMotors();
  digitalWrite(BUZZER, LOW);

  server.send(200, "text/plain", "OK");
}

// ===== SETUP =====
void setup() {
  Serial.begin(115200);

  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(M3, OUTPUT);
  pinMode(M4, OUTPUT);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(SOUND_SENSOR, INPUT);
  pinMode(PIR_SENSOR, INPUT);
  pinMode(PROX_SENSOR, INPUT_PULLUP);
  pinMode(PULSE_PIN, INPUT);

  pinMode(BUZZER, OUTPUT);

  stopMotors();

  // OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED Failed");
  }
  display.setTextSize(1);
  display.setTextColor(WHITE);

  // WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("WiFi Connected");
  display.println(WiFi.localIP());
  display.display();

  server.on("/fall", handleFall);
  server.begin();
}

// ===== LOOP =====
void loop() {

  server.handleClient();

  // ===== ULTRASONIC =====
  long duration = pulseIn(ECHO, HIGH, 30000);
  int distance = duration * 0.034 / 2;

  // ===== 🔊 DIGITAL SOUND =====
  int sound = digitalRead(SOUND_SENSOR);
  String soundStatus = (sound == HIGH) ? "NOISE" : "SILENT";

  // ===== OTHER SENSORS =====
  int motion = digitalRead(PIR_SENSOR);
  int prox = digitalRead(PROX_SENSOR);
  bool objectDetected = (prox == LOW);

  // ===== ❤️ HEART RATE =====
  int pulse = analogRead(PULSE_PIN);

  if (pulse > threshold && millis() - lastBeatTime > 250) {
    unsigned long currentTime = millis();
    unsigned long interval = currentTime - lastBeatTime;

    lastBeatTime = currentTime;

    if (interval > 0) {
      bpm = 60000 / interval;
    }
  }

  // ===== SERIAL =====
  Serial.print("Dist:");
  Serial.print(distance);

  Serial.print(" Sound:");
  Serial.print(soundStatus);

  Serial.print(" Motion:");
  Serial.print(motion);

  Serial.print(" Prox:");
  Serial.print(objectDetected);

  Serial.print(" BPM:");
  Serial.println(bpm);

  // ===== OLED =====
  display.clearDisplay();
  display.setCursor(0, 0);

  display.print("D:");
  display.println(distance);

  display.print("Sound:");
  display.println(soundStatus);

  display.print("Motion:");
  display.println(motion);

  display.print("Prox:");
  display.println(objectDetected ? "NEAR" : "FAR");

  display.print("HR:");
  display.println(bpm);

  display.display();

  delay(300);
}