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
    plt.ylabel('speed')
    plt.xlabel('measure ID in chronicle order')
    plt.title(title)
    plt.show()

def plot2(data1,data2,data3,data4,title):
    plt.plot(data1,data2,'-g',data3,data4,'--r')
    plt.ylabel('speed')
    plt.xlabel('measure ID in chronicle order')
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


plot1(one,'one')
plot1(two,'two')
plot1(three,'three')
plot1(four,'four')
plot1(five,'five')
plot1(six,'six')
plot1(seven,'seven')

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
trendline=[]
gain1=[]
gain2=[]
del readings[:]
for i in range(len(a)):
    readings.append(i)
n=0
for a in all:
    fit=np.poly1d(np.polyfit(readings,a,1))
    gain1.append(np.polyfit(readings,a,1)[0])
    gain2.append(np.polyfit(readings, a, 1)[1])
    for i in range(len(a)):
        trendline.append(fit(i))
    n=n+1

    plot2(readings, a, readings, trendline, 'run'+str(n))

    del trendline[:]

print(mean)
print(std)
print(gain1)
print(gain2)
