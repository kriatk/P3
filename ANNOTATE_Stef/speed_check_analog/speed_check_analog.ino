int irSpeed = A0;
int irMat = A1;
bool looped=0;

int n=1;

unsigned long int start;
unsigned long int interval;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200); //Begin serial monitor
pinMode(irSpeed, INPUT); //IR as input (analog)
pinMode(irMat, INPUT); //IR2 as input (analog)


}

void loop() {
  // put your main code here, to run repeatedly:
  if (n==0){start= micros();}
if (analogRead(irSpeed) >=800 ){
  n++;
  if (n==10000){interval=micros()-start;
  float readings=n*1000/interval;
  Serial.println(readings);
  while(1){}
  }
  
  

}
}
