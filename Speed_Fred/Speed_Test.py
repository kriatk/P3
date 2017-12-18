import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir('C:\\Users\Stefan_Na\PycharmProjects\MOE\P3\Speed_Fred')
print(os.getcwd())


# filenames:Name of text file coerced with +.txt


def createListfromTXT(txt, list):
    try:
        file = open(txt, 'r')  # Trying to create a new file or open one
        # list = []
        for line in file:
            print('line', line)
            list.append(float(line))
        file.close()

    except:
        print('Something went wrong! Cannot tell what?', line, 'not read from list')

def plot1(data,title):
    plt.plot(data,'-g')
    plt.ylabel('speed in cm/s')
    plt.xlabel('measurements chronological order every 3 meters of conveyor')
    plt.title(title)
    plt.show()

def plot2(data1,data2,data3,data4,title):
    plt.plot(data1,data2,'-g',data3,data4,'--r')
    plt.ylabel('speed in cm/s')
    plt.xlabel('measurements chronological order every 3 meters of conveyor')
    plt.title(title)
    plt.show()

speed=[]
seven=[]
six=[]
five=[]
four=[]
three=[]
two=[]
one=[]

del speed[:]
createListfromTXT("speed_test_data.txt",speed)
plot1(speed,'Measurement with seven strips over time')
n=0
for s in speed:
    n=n+1
    if n is 7:
        seven.append(s)
        n=0
    elif n is 6:
        six.append(s)
    elif n is 5:
        five.append(s)
    elif n is 4:
        four.append(s)
    elif n is 3:
        three.append(s)
    elif n is 2:
        two.append(s)
    elif n is 1:
        one.append(s)

all=[one,two,three,four,five,six,seven]

averageall=[]
for i in range(len(one)):
    averageall.append((one[i]+two[i]+three[i]+four[i]+five[i]+six[i]+seven[i])/7)

plot1(averageall,'All Strips average')

# plot1(one,'one')
# plot1(two,'two')
# plot1(three,'three')
# plot1(four,'four')
# plot1(five,'five')
# plot1(six,'six')
# plot1(seven,'seven')

##Standard deviation
mean=[]
std=[]
for a in all:
    print(np.mean(a))
    mean.append(np.mean(a))
    print(np.std(a))
    std.append(np.std(a))
    print()

##Trendline
readings=[]
readingsall=[]
trendline=[]
trendlineall=[]
gain1=[]
gain2=[]
del readings[:]
for i in range(len(a)):
    readings.append(i)

del readingsall[:]
for i in range(len(speed)):
    readingsall.append(i)

fitall=np.poly1d(np.polyfit(range(len(speed)),speed,1))
gain1all=np.polyfit(range(len(speed)),speed,1)[0]
gain2all=np.polyfit(range(len(speed)),speed,1)[1]

for i in range(len(speed)):
    trendlineall.append(fitall(i))

plot2(readingsall, speed, readingsall, trendlineall, 'Speed of all 7 strips over 581 measurements')

n=0
for a in all:
    fit=np.poly1d(np.polyfit(readings,a,1))
    gain1.append(np.polyfit(readings,a,1)[0])
    gain2.append(np.polyfit(readings, a, 1)[1])
    for i in range(len(a)):
        trendline.append(fit(i))
    n=n+1

    plot2(readings, a, readings, trendline, 'Strip '+str(n))

    del trendline[:]

print(mean)
print(sum(speed)/len(speed))
print(std)
print(sum(std)/len(std))
print(np.std(speed))

print(gain1)
print(gain1all)
print(gain2)
print(sum(gain2)/len(gain2))
print(gain2all)

#
print(fitall(0),(fitall(580)))
