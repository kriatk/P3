//Defining all variables
int ir1 = A1;
int ir2 = A0;
int digitalPin = 1;
int value1 = 0;
int value2 = 0;
int i = 0;
int z = 0;
int j = 0;
int y = 0;

char dataString[50] = {0};

float total = 0;
float average = 0;

float AllSpeeds [10];
float Send_To_Rasp_Speed;
int Send_To_Rasp_Material;

int threshold = 800;
float distance_all = 0.182;
float distance_single = 0.0182;

float convspeed = 0;
float convspeed_total = 0;
float time1 = 0;
float time2 = 0;
float time_start = 0;
float time_end = 0;
float elapsedtime = 0;
float elapsedtime_total = 0;

bool W_reached = false;
bool B_reached = false;
bool starter = false;

void setup() {

Serial.begin(9600); //Begin serial monitor
pinMode(ir1, INPUT); //IR1 as input (analog)
pinMode(ir2, INPUT); //IR2 as input (analog)
pinMode(digitalPin, INPUT); //digitalPin as input

}

void loop(){

value2 = analogRead(ir2);
if (value2 < threshold){
  Send_To_Rasp_Material = 1;
}
else{
  Send_To_Rasp_Material = 0;
}

while (digitalPin == HIGH){
  while (i < 10){ //Run for 10 times (5 white & 5 black stripes)
  value1 = analogRead(ir1); //Read value from sensor (Black > 800, White < 800
  if ((i % 2) == 0){ //Turns out true when it turns out as an integer
    if (value1 < threshold && W_reached == false){ //White stripe time start
      if (starter == false){ //Whole paper time start
        time_start = millis();
        starter = true;
      }
      time1 = millis();
      W_reached = true;
    }
    if (value1 > threshold && W_reached == true){ //White stripe over - calculations
      time2 = millis();
      W_reached =false;
      elapsedtime = (time2-time1)/1000;
      convspeed = (distance_single/elapsedtime)*60;
      AllSpeeds[i] = convspeed;
      W_reached = false;
      convspeed = 0;
      elapsedtime = 0;
      time1 = 0;
      time2 = 0;
      i++;
  }
  }
  else{ //Black strip time start
    if (value1 > threshold && B_reached == false){
      time1 = millis();
      B_reached = true;
    }
    if (value1 < threshold && B_reached == true){ //Black stripe over - calculations
      time2 = millis();
      B_reached = false;
      elapsedtime = (time2-time1)/1000;
      convspeed = (distance_single/elapsedtime)*60;
      AllSpeeds[i] = convspeed;
      B_reached = false;
      convspeed = 0;
      elapsedtime = 0;
      time1 = 0;
      time2 = 0;
      i++;
    }
  }
}
}

time_end = millis(); //Whole paper time end

for( j ; j < 10 ; j++){ //Add all numbers in array
   total += AllSpeeds[j];
}

if (y == 0){ //Calculate and print Average_Speed
average = total/10;
Send_To_Rasp_Speed = average;
y++;
}

if (z == 0){ //Calculate and print Total_Speed
elapsedtime_total = (time_end-time_start)/1000;
convspeed_total = (distance_all/elapsedtime_total)*60;
z++;
}

//Starting serial communication to Pi
sprintf(dataString,"%06lX",Send_To_Rasp_Speed); // convert a value to hexa l for long and  
Serial.println(dataString);   // send the data
char dataString[50] = {0};

delay(500);

//Reset all values so ready for new measurements
value1 = 0;
value2 = 0;
i = 0;
z = 0;
j = 0;
y = 0;
total = 0;
average = 0;
AllSpeeds [10];
convspeed = 0;
convspeed_total = 0;
time1 = 0;
time2 = 0;
time_start = 0;
time_end = 0;
elapsedtime = 0;
elapsedtime_total = 0;
starter = false;

}
