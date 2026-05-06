#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>

// ===== WIFI =====
const char* ssid = "biswajit";
const char* password = "12345678";

// 👉 PUT ESP32 DEV IP HERE
String serverUrl = "http://192.168.1.200/fall";

// ===== CAMERA PINS (AI Thinker) =====
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

// ===== SETUP =====
void setup() {
  Serial.begin(115200);

  // WiFi connect
  WiFi.begin(ssid, password);
  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ WiFi Connected");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  // ===== CAMERA CONFIG =====
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;

  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  // ✅ Stable settings
  config.frame_size = FRAMESIZE_QQVGA;
  config.jpeg_quality = 30;
  config.fb_count = 1;
  config.grab_mode = CAMERA_GRAB_LATEST;

  // Init camera
  if (esp_camera_init(&config) != ESP_OK) {
    Serial.println("❌ Camera Init Failed");
    return;
  }

  Serial.println("✅ Camera Ready");
}

// ===== LOOP =====
void loop() {

  // 📸 Capture frame
  camera_fb_t * fb = esp_camera_fb_get();

  if (!fb) {
    Serial.println("❌ Capture Failed");
    return;
  }

  esp_camera_fb_return(fb);

  // 🔥 FALL DETECTION (DEMO)
  int value = random(0, 100);

  Serial.print("Value: ");
  Serial.println(value);

  if (value > 70) {
    Serial.println("🚨 FALL DETECTED!");

    sendFallAlert();
    delay(10000); // prevent spam
  }

  delay(2000);
}

// ===== SEND ALERT =====
void sendFallAlert() {

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi lost, reconnecting...");
    WiFi.begin(ssid, password);
    return;
  }

  HTTPClient http;

  http.begin(serverUrl);
  int code = http.GET();

  Serial.print("Alert Sent: ");
  Serial.println(code);

  http.end();
}