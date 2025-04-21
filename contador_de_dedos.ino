// Pines conectados a los segmentos A-G
const int segmentos[7] = {2, 3, 4, 5, 6, 7, 8};

// Dígitos del 0 al 9 para CÁTODO COMÚN
const int digitos[10][7] = {
  // A  B  C  D  E  F  G
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {1, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 0, 1, 1}  // 9
};

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
  }

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char entrada = Serial.read();

    // Solo números del 0 al 5
    if (entrada >= '0' && entrada <= '5') {
      int numero = entrada - '0';
      mostrarNumero(numero);
    }
  }
}

void mostrarNumero(int n) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentos[i], digitos[n][i]);
  }
}


