#define sw 37
void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  pinMode(sw,INPUT);
}

void loop() {
  if (Serial1.available()>0) {
    String texto = "";
    char character; 
    
    while (Serial1.available()) {
      character = Serial1.read();
      texto.concat(character);
    }
    if(digitalRead(sw)==true){
    Serial1.print(texto);
    Serial.print(texto);
    }else{
      Serial1.print("error");
    }
    
  }
}
