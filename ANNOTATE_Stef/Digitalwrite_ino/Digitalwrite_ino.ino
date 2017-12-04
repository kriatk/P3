
int speedo[2];
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
 
 
}

// the loop routine runs over and over again forever:
void loop() {
  speedo[0]=24;
  speedo[1]=0;
  for (int x=0; x<=1000; x++) {
   Serial.write(speedo, 2);}
  delay(2000);
  speedo[1]=1;
   for (int x=0; x<=1000; x++) {
   Serial.write(speedo, 2);}
}
