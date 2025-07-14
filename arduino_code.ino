int relayPin = 8;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();
    if (input == '1') {
      digitalWrite(relayPin, HIGH);
    } else if (input == '0') {
      digitalWrite(relayPin, LOW);
    }
  }
}
