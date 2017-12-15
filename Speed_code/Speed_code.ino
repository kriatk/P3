
// Define pins
#define pinMat A1
#define pinSpeed A0

//Initialize material variables
int irMat = 0; // analog reading value
int Material = 0; //material state

//Initialize speed calculation variables
unsigned long time_start = 0;
unsigned long time_end = 0;
float Speed = 0.0;
float distance = 1.71;
float average_speed = 0.0;
float sp[6];
int pointer = 1;

// Initialize boolean flags
bool recording = false;
bool mat_flow = false;
bool count = false;

//Initialize serial communication variables
char dataString[50] = {0};
unsigned long int Serial_Print;


void Send(int Material0, float Speed0){
        
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

  irMat = analogRead(pinMat);
  if (irMat < 800){
      Material = 1;
      }
      else{
      Material = 0;  
      }
  
  if (count == true) {
    Speed = distance * 1000000 / ((time_end - time_start));
    sp[pointer] = Speed;
    pointer++;
 
    //Serial.println(Speed);    
    count = false;    

      if (pointer == 7){
        average_speed = (sp[0]+sp[1]+sp[2]+sp[3]+sp[4]+sp[5]+sp[6])/7;
        pointer = 0;
        sp[6] = {0};
      }       
    }
  Send(Material, average_speed);
  }
