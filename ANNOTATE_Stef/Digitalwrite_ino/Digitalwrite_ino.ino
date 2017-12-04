char dataString[50] = {0};
int a =0; 
float speed0 = 0;
long int final;
void setup() {
Serial.begin(9600);

//Starting serial communication
}
  
void loop() {
  for (a=0;a<1000;a++){// a value increase every loop
            final =0;
            long int speedo= speed0*100;
            speed0=speed0+0.015;
            final = speedo << 8;
            //Serial.println (final);
            final = final | (a%2);
            //Serial.println (speedo);
            //delay(1000);
  sprintf(dataString,"%06lX",final); // convert a value to hexa l for long and  
  Serial.println(dataString);   // send the data
  char dataString[50] = {0};
  }
  delay(2000);
  while(speed0>10){ sprintf(dataString,"%06lX",final); // convert a value to hexa l for long and  
  Serial.println(dataString);}               
}
