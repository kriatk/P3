int irSpeed = A0;
int irMat = A1;
bool looped=0;

int n=1;

unsigned long int start;
unsigned long int interval;
unsigned long int Serial_Print;

unsigned long int Material;
float Speed;

char dataString[50] = {0};

long int material(void){
if (analogRead(irMat) < 800){
  Material = 1;
}
else{
  Material = 0;
}
return Material;
}

void Send(unsigned long int Material0, float Speed0){
        
    Serial_Print = Material0 <<16 | int(Speed0*100);
    
    sprintf(dataString,"%06lX",Serial_Print); // convert a value to hexa l for long and  
    Serial.println(dataString);   // send the data
    char dataString[50] = {0};
  }

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200); //Begin serial monitor
pinMode(irSpeed, INPUT); //IR as input (analog)
pinMode(irMat, INPUT); //IR2 as input (analog)


}

void loop() {
  // put your main code here, to run repeatedly:
while (analogRead(irSpeed) >=800 ){//black
Material=material();
if (looped == 1){
  //Send(Material,Speed);
  }
  n++;
  if (n==10000){interval=micros()-start;
  float readings=n*1000/interval;
  Serial.println(readings);
  while(1){}
}
}
if (n==0){start= micros();}

while (analogRead(irSpeed) <800 ){//white
n++;
if (n==10000){interval=micros()-start;
float readings=n*1000/interval;
Serial.println(readings);
while(1){}
}
Material=material();
if (looped == 1){
  //Send(Material,Speed);
  }
}
Serial.println(n);
if (n==10000){interval=micros()-start;
float readings=n*1000/interval;
Serial.println(readings);
while(1){}
}
//Serial.println(micros());
//Serial.println(start);
//Serial.println(interval);

//Speed=1.7*1000000/(interval);
//looped=1;
//
//Serial.println(Speed/1.6667);
//Serial.print("\t");
//if (n == 7){
//Serial.println();
//n=0;
//}
//n=n+1;
//Serial.println(n);
}
