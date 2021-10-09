// Entrada analógica A0, A1, A2 são usadas para sensores ldr
// Saídas digitais 2, 3 são usadas para controle de lâmpadas
// Entrada digital 4 é usada para ligar/desligar modo AUTOMÁTICO
// Saídas digitais 5, 6, 7 são usadas para controle de tomadas
// Sensor de aproximação ou infravermelho 8, 9
// Saída digital 10 mostra se o modo automático está acionado
// Entradas digitais 11, 12, 13 são usadas para controle de tomadas
// Acionamento manual das lâmpadas 17, 18 (analógicos usados como digitais)

//Recurso automático e manual a ser ativado
int automatizador = 4;
int sinalizador = 10;

//SAÍDAS
int lampQuarto = 2;
int lampCozinha = 3;


int tomQuarto = 5;
int tomCozinha1 = 6;
int tomCozinha2 = 7;

//Auxiliares
int guarda_estado1 = 0; //modo automático
int guarda_estado2 = 0; //tomada quarto
int guarda_estado3 = 0; //tomada cozinha 2
int guarda_estado4 = 0; //tomada cozinha 2
int guarda_estado5 = 0; //lâmpada quarto
int guarda_estado6 = 0; //lâmpada cozinha
int acenderLQ = 0;
int acenderLC = 0;
int tempoLigado = 20000; //2000 = 10s
int luminosidadeMin = 200; //Equivalente a 20%
int tempo = 0;


//ENTRADAS
int ldrQuarto = A0;
int ldrCozinha = A1;

int sensorQuarto = 8;
int sensorCozinha = 9;

int SwitomQuarto = 11;
int SwitomCozinha1 = 12;
int SwitomCozinha2 = 13;

int SwilampQuarto = 17;
int SwilampCozinha = 18;

//PROGRAMACAO
void setup() {
Serial.begin(9600);

pinMode(automatizador, INPUT);
pinMode(sinalizador, OUTPUT);

pinMode(ldrQuarto, INPUT);
pinMode(ldrCozinha, INPUT);

pinMode(SwitomQuarto, INPUT);
pinMode(SwitomCozinha1, INPUT);
pinMode(SwitomCozinha2, INPUT);
pinMode(SwilampQuarto, INPUT);
pinMode(SwilampCozinha, INPUT);

pinMode(sensorQuarto, INPUT);
pinMode(sensorCozinha, INPUT);


pinMode(lampQuarto, OUTPUT);
pinMode(lampCozinha, OUTPUT);


pinMode(tomQuarto, OUTPUT);
pinMode(tomCozinha1, OUTPUT);
pinMode(tomCozinha2, OUTPUT);

}

void loop() {

tempo = millis();
//Ligar ou desligar modo automático
  if ((tempo%2000 == 0) || (tempo==10)){
    Serial.println("===========================");
 if (guarda_estado1 == 0){
   Serial.println("Modo AUTOMATICO acionado");
     Serial.println("===========================");}
 if (guarda_estado1 == 1){
   Serial.println("Modo MANUAL acionado");
       Serial.println("===========================");
}
    
 if(digitalRead(lampQuarto)==HIGH){
   Serial.println("Lampada 1 esta ACESA");}
 if(digitalRead(lampQuarto)==LOW){
   Serial.println("Lampada 1 esta APAGADA");}  
 if(digitalRead(lampCozinha)==HIGH){
   Serial.println("Lampada 2 esta ACESA");}
 if(digitalRead(lampCozinha)==LOW){
   Serial.println("Lampada 2 esta APAGADA");} 
if(digitalRead(tomCozinha2)==HIGH){
   Serial.println("Tomada 1 esta LIGADA");}
if(digitalRead(tomCozinha2)==LOW){
   Serial.println("Tomada 1 esta DESLIGADA");}
if(digitalRead(tomCozinha1)==HIGH){
   Serial.println("Tomada 2 esta LIGADA");}
if(digitalRead(tomCozinha1)==LOW){
   Serial.println("Tomada 2 esta DESLIGADA");}
if(digitalRead(tomQuarto)==HIGH){
   Serial.println("Tomada 3 esta LIGADA");}
if(digitalRead(tomQuarto)==LOW){
   Serial.println("Tomada 3 esta DESLIGADA");}
 
  }
    
if (digitalRead(automatizador) == HIGH) {  
delay(200);
if (guarda_estado1 == 0){
  guarda_estado1 = 1;
}
else{
  guarda_estado1 = 0;
}

}

//Acionadores no modo manual
if (guarda_estado1 == 1) {

digitalWrite(sinalizador, LOW);
  


if(acenderLQ != 0){
  digitalWrite(lampQuarto, LOW);
  acenderLQ = 0;}
 
if(acenderLC != 0){
  digitalWrite(lampCozinha, LOW);
  acenderLC = 0;}

  

//Acionador Tomada Quarto
if (digitalRead(SwitomQuarto) == HIGH) {  
delay(100);
if (guarda_estado2 == 0){
  guarda_estado2 = 1;
}
else{
  guarda_estado2 = 0;
}
}
if (guarda_estado2 == 0){
  digitalWrite(tomQuarto, HIGH);
}
if (guarda_estado2 == 1) {
   digitalWrite(tomQuarto, LOW);
}

//Acionador Tomada 1 da cozinha
if (digitalRead(SwitomCozinha1) == HIGH) {  
delay(100);
if (guarda_estado3 == 0){
  guarda_estado3 = 1;
}
else{
  guarda_estado3 = 0;
}
}
if (guarda_estado3 == 0){
  digitalWrite(tomCozinha1, HIGH);
}
if (guarda_estado3 == 1) {
   digitalWrite(tomCozinha1, LOW);
}

//Acionador Tomada 2 da cozinha
if (digitalRead(SwitomCozinha2) == HIGH) {  
delay(100);
if (guarda_estado4 == 0){
  guarda_estado4 = 1;
}
else{
  guarda_estado4 = 0;
}
}
if (guarda_estado4 == 0){
  digitalWrite(tomCozinha2, HIGH);
}
if (guarda_estado4 == 1) {
   digitalWrite(tomCozinha2, LOW);
}

//Acionador Lâmpada Quarto
if (digitalRead(SwilampQuarto) == HIGH) {  
delay(100);
if (guarda_estado5 == 0){
  guarda_estado5 = 1;
}
else{
  guarda_estado5 = 0;
}

if (guarda_estado5 == 0){
  digitalWrite(lampQuarto, HIGH);
}
if (guarda_estado5 == 1) {
   digitalWrite(lampQuarto, LOW);
   acenderLQ = 0;
}
  }



//Acionador Lâmpada Cozinha
if (digitalRead(SwilampCozinha) == HIGH) {  
delay(100);
if (guarda_estado6 == 0){
  guarda_estado6 = 1;
}
else{
  guarda_estado6 = 0;
}

if (guarda_estado6 == 0){
  digitalWrite(lampCozinha, HIGH);
}
if (guarda_estado6 == 1) {
   digitalWrite(lampCozinha, LOW);
   acenderLC = 0;
}
  }

}

//Modo automático acionado
if (guarda_estado1 == 0){
digitalWrite(sinalizador, HIGH);


//Lógica para contar tempo - Lâmpada quarto
if ((acenderLQ > 0) && (acenderLQ < tempoLigado))
{
  acenderLQ = acenderLQ + 1;
  if (acenderLQ == tempoLigado)
{
  acenderLQ = 0;
}
  if (acenderLQ == 0)
{
  digitalWrite (lampQuarto, LOW);
}
} 
if (acenderLQ == 0)
{
  digitalWrite (lampQuarto, LOW);}

//Lógica para contar tempo - Lâmpada cozinha
if ((acenderLC > 0) && (acenderLC < tempoLigado))
{
  acenderLC = acenderLC + 1;
  if (acenderLC == tempoLigado)
{
  acenderLC = 0;
}
  if (acenderLC == 0)
{
  digitalWrite (lampCozinha, LOW);
}
}
 if (acenderLC == 0)
{
  digitalWrite (lampCozinha, LOW);
}

//Lógica para acionamento - Lâmpada quarto
if(analogRead(ldrQuarto) <= luminosidadeMin)
  {
    if (digitalRead(sensorQuarto))
    {
      acenderLQ = acenderLQ + 1;
      if (acenderLQ > 0)
      {
        digitalWrite(lampQuarto, HIGH);
      }
      }
    }

//Lógica para acionamento - Lâmpada cozinha
if(analogRead(ldrCozinha) <= luminosidadeMin)
  {
    if (digitalRead(sensorCozinha))
    {
      acenderLC = acenderLC + 1;
      if (acenderLC > 0)
      {
        digitalWrite(lampCozinha, HIGH);
      }
      }
  
//Acionador Tomada Quarto
if (digitalRead(SwitomQuarto) == HIGH) {  
delay(100);
if (guarda_estado2 == 0){
  guarda_estado2 = 1;
}
else{
  guarda_estado2 = 0;
}
}
if (guarda_estado2 == 0){
  digitalWrite(tomQuarto, HIGH);
}
if (guarda_estado2 == 1) {
   digitalWrite(tomQuarto, LOW);
}

//Acionador Tomada 1 da cozinha
if (digitalRead(SwitomCozinha1) == HIGH) {  
delay(100);
if (guarda_estado3 == 0){
  guarda_estado3 = 1;
}
else{
  guarda_estado3 = 0;
}
}
if (guarda_estado3 == 0){
  digitalWrite(tomCozinha1, HIGH);
}
if (guarda_estado3 == 1) {
   digitalWrite(tomCozinha1, LOW);
}

//Acionador Tomada 2 da cozinha
if (digitalRead(SwitomCozinha2) == HIGH) {  
  delay(100);
if (guarda_estado4 == 0){
    guarda_estado4 = 1;
}
else{
  guarda_estado4 = 0;
}
}
if (guarda_estado4 == 0){
  digitalWrite(tomCozinha2, HIGH);
}
if (guarda_estado4 == 1) {
   digitalWrite(tomCozinha2, LOW);
}
}
}
}
