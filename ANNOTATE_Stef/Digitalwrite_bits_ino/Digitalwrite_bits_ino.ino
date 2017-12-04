char dataString[50] = {0};
int a =0; 
float speed0 = 10.34;
void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  for (a=0;a<500;a++){// a value increase every loop
   long int final =0;
            delay(1000);
            long int speedo= speed0*100;
            final = speedo << 8;
            //Serial.println (final);
            delay(1000);
            final = final | (a%2);
            //Serial.println (final);
            delay(1000);
  sprintf(dataString,"%06lX",final); // convert a value to hexa 
  Serial.println(dataString);   // send the data
  char dataString[50] = {0};
  }                  // give the loop some break
}
