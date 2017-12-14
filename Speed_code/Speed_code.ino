int irMat = 0;
int pinMat = A1;
int irSpeed = 0;
int pinSpeed = A0;
int counter = 0;
unsigned long time_start = 0;
unsigned long time_end = 0;
int mat_ir_value;

float sp[6];
float Speed = 0.0;
float distance = 1.71;
float average_speed = 0.0;

bool recording = false;
bool count = false;
bool mat_flow = false;

char dataString[50] = {0};
unsigned long int Serial_Print;
int Material0 = 0;


void Send(unsigned long int Material0, float Speed0){
        
    Serial_Print = Material0 <<16 | int(Speed0*100);
    
    sprintf(dataString,"%06lX",Serial_Print); // convert a value to hexa l for long and  
    Serial.println(dataString);   // send the data
    char dataString[50] = {0};
  }

void setup() {
  pinMode(pinSpeed, INPUT);
  pinMode(pinMat, INPUT);

  Serial.begin(115200);
}

void loop() {
    if (analogRead(pinSpeed) < 800 && recording == false) {
    time_start = micros();
    recording = true;
    } 

    if (analogRead(pinSpeed) > 800 && recording == true) {
    time_end = micros();
    recording = false;
    count = true;
    }

  mat_ir_value = analogRead(pinMat);
  if (mat_ir_value < 800){
      Material0 = 1;
      }
      else{
      Material0 = 0;  
      }
  
  if (count == true) {
    Speed = distance * 1000000 / ((time_end - time_start));
    sp[counter] = Speed;
    counter++;
 
    //Serial.println(Speed);    
    count = false;    

      if (counter == 7){
        average_speed = (sp[0]+sp[1]+sp[2]+sp[3]+sp[4]+sp[5]+sp[6])/7;
        counter = 0;
        //Serial.println(average_speed/1.666667);
      }       
    }
  Send(Material0, average_speed);
  }
