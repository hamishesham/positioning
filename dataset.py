from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pylab
from pylab import *
import math
import csv



def position():
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlim3d(0, 4)
    ax.set_ylim3d(0,4)
    ax.set_zlim3d(0,3)
    ax.scatter(2,2 , 3, c='r', marker='s')
    # ax.scatter(3, 3, 3, c='r', marker='s')
    # ax.scatter(1, 1, 3, c='r', marker='s')
    # ax.scatter(3,1 , 3, c='r', marker='s')
    plt.show()
def distnace():
    x = 0
    y = 0
    distances = []
    x_position =[]
    y_position =[]
    for i in range (0,20):
        distance =sqrt((x-2)**2 +(y-2)**2)
        x =x + 0.1
        y =y + 0.1
        distances.append(distance)
        x_position.append(x)
        y_position.append(y)
    return distances
    return x_position
    return y_position

def incident_angle():
    d= distnace()
    incident_angles = []
    for x in range(len(d)):
        incident_angle = d[x]/ 3
        incident_angles.append(incident_angle)
    return incident_angles

def recieved_powers():
    theata=70
    P_LED=20
    nLED=60
    reciev_powers =[]
    P_total=nLED*nLED*P_LED
    Adet=1e-4
    Ts=1
    FOV=70
    d =distnace()
    incid_ang = incident_angle()
    lambertian_index = -np.log(2)/np.log(cos(theata))
    concentrator =(lambertian_index ** 2)/(sin(FOV)**2)
    for i in range(len(incid_ang)):
        recieved_power = (P_total *Adet*concentrator * 9)/((22/7)*(d[i] **4))
        reciev_powers.append(recieved_power)
    return reciev_powers

def dataset():
    d = distnace()
    re_p = recieved_powers()
    datasets = list(zip(d,re_p))
    guestFile = open("N:\Codes\dataset.txt","w")
    guestFile.close()
    for entries in range(len(datasets)) :
        guestFile = open("N:\Codes\dataset.txt","a")
        guestFile.write(datasets.index(datasets),str(datasets[entries]))
        guestFile.write("\n")
        guestFile.close()
    with open('N:\Codes\dataset.txt', 'r') as my_file:
        text = my_file.read()
        text = text.replace("(", "")
        text = text.replace(")", "")

# If you wish to save the updates back into a cleaned up file
    with open('N:\Codes\dataset.txt', 'w') as my_file:
        my_file.write(text)
dataset()

    # def recieved_power_point(distance,incident_angle):
#     P_LED=20
#     nLED=60
#     trans_power = nLED*nLED*P_LED

    

# print(transimitted_power())


# position()
