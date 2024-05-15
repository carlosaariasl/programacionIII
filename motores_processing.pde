import processing.serial.*;

Serial puerto;
PButton botonVelocidad1;
PButton botonVelocidad2;
PButton botonParar;

void setup() {
  size(300, 200);
  puerto = new Serial(this, Serial.list()[0], 9600);
  botonVelocidad1 = new PButton("Velocidad 1", 50, 50, 200, 40);
  botonVelocidad2 = new PButton("Velocidad 2", 50, 100, 200, 40);
  botonParar = new PButton("Parar", 50, 150, 200, 40);
}

void draw() {
  background(200);
  botonVelocidad1.display();
  botonVelocidad2.display();
  botonParar.display();
}

void mousePressed() {
  if (botonVelocidad1.isClicked(mouseX, mouseY)) {
    puerto.write('1');
  } else if (botonVelocidad2.isClicked(mouseX, mouseY)) {
    puerto.write('2');
  } else if (botonParar.isClicked(mouseX, mouseY)) {
    puerto.write('0');
  }
}

class PButton {
  String label;
  int x, y, w, h;

  PButton(String label, int x, int y, int w, int h) {
    this.label = label;
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  void display() {
    fill(255);
    rect(x, y, w, h);
    fill(0);
    textAlign(CENTER, CENTER);
    text(label, x + w/2, y + h/2);
  }

  boolean isClicked(int mx, int my) {
    return mx > x && mx < x + w && my > y && my < y + h;
  }
}
