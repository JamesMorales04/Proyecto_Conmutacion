void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String texto = "";
    char character;

    while (Serial.available()>0) {
      character = Serial.read();
      texto.concat(character);
    }
    Serial1.print(texto);
  }

    if (Serial1.available()) {
    String texto = "";
    char character;

    while (Serial1.available()>0) {
      character = Serial1.read();
      texto.concat(character);
    }
    Serial.print(texto);
  }

}
