import time
#import spidev
current_milli_time = lambda: int(round(time.time() * 1000)) #reausable to get miliseconds

#default actuator values for the driver - all OFF
Actuators =    [0x96, 0x5F,0xFF,0xFF, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00]
speed_conv = 17 # conveyor speed in cm/s
material_length = 110 #total material lenght
material_running = True #conveyor is on
actuated = False #none of the actuators is ON
timeout = 25 #define how long you want the actuator to be ON in milliseconds


#assumed error positions. error[x, y] = [e
# x is position from material side (1 cm being 1 actuator)
# y is postion from start of material
error_x = [2, 6, 10, 1, 5]
error_y = [50, 75, 25, 100, 110]

time_start = time.time() #time at start, material assuming to start at y = 0

#function to find which solenoid to actuate depending on how far error is from the edge on x axis
#inputs: cm, state (1 is ON)
def actuation(cm,state) :
    byte1 = 27-2*(12-cm)
    byte2 = 26-2*(12-cm)
    if state is 0:
        Actuators[byte1] = 0x00
        Actuators[byte2] = 0x00
    elif state is 1:
        Actuators[byte1] = 0xFF
        Actuators[byte2] = 0xFF

#function to calculate material y position at our device.
#input: speed of the conveyor
#return: rounded number in cm
def current_y(velocity):
    time_now = time.time()
    y =  velocity * (time_now - time_start)
    y = int(round(y))
    return y

while (material_running):
    #constantly calculate y of globall material lenght at our device location
    y = current_y(speed_conv)
    print("y = ", y)

    #constantly check if at the current y position, there was any error recorded
    if y in error_y:
        #if there is, find out the index position in the list
        index = error_y.index(y)
        print("index = ", index)

        #use this index position to find out the x position of the error form error_x list
        #change the actuator array to to make the corresponding actuator ON
        actuation(error_x[index], 1)

        #flag to record that one of the actuators is active
        actuated = True
        #save the index, becasue actuator needs to be manually deactivated later
        actuation_index = index
        actuation_time = current_milli_time()

    if actuated:
        #calculate how long since the actuator activation
        timer = current_milli_time() - actuation_time
        print("Timer = ", timer)

        #if it reaches timout, turn off the actuator
        if timer >= timeout:
            actuation(actuation_index, 0)
            actuated = False
            print("Actuated = False")

#   write to the driver
#   spi.writebytes(Actuators)

    #not really needed, just an automatic stop
    if y >= material_length and not actuated:
        material_running = False

    #not needed, but full speed floods the console
    time.sleep(0.005)
