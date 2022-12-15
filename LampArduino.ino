bool on = false;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    String data = Serial.readString();
    if (data.equals("1")){
      on = true;
    }
    else if (data.equals("0")) {
      on = false;
    }
    Serial.write("received");
  }

  if (on) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
  delay(1);
}