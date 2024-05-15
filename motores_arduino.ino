class Motor {
  private:
    int pin1;
    int pin2;
    int enablePin;
  public:
    Motor(int p1, int p2, int en) {
      pin1 = p1;
      pin2 = p2;
      enablePin = en;
      pinMode(pin1, OUTPUT);
      pinMode(pin2, OUTPUT);
      pinMode(enablePin, OUTPUT);
    }

    void mover(int velocidad) {
      analogWrite(enablePin, velocidad);
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, LOW);
    }

    void parar() {
      analogWrite(enablePin, 0);
      digitalWrite(pin1, LOW);
      digitalWrite(pin2, LOW);
    }

    void velocidad1() {
      mover(100);
    }

    void velocidad2() {
      mover(200);
    }
};

Motor motor(8, 9, 10); // Pines de control y PWM

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == '1') {
      motor.velocidad1();
    } else if (comando == '2') {
      motor.velocidad2();
    } else if (comando == '0') {
      motor.parar();
    }
  }
}
