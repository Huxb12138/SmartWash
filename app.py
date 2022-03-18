import random
import time
import numpy as np
from gpiozero import DistanceSensor
from flask import *

#initialize the sensor object
sensor = DistanceSensor(echo=17, trigger=4)

#setup flask
app = Flask(__name__)

#root path is set to run py code
@app.route('/')
def index():
    
    mybasket.update_amount()
    amount = mybasket.amount
    if(amount <= -5):
        amount = 0
    mybasket.check_laundry()
    mybasket.check_add()
    mybasket.check_amount()
    mybasket.check_time()
    if(mybasket.level == 0):
        level = 'Good job on doing your landry'
    elif(mybasket.level == 1):
        level = 'Inefficient: Amount of clothes is too less'
    elif(mybasket.level == 2):
        level = 'More clothes are required to reach efficient amount'
    elif(mybasket.level == 3):
        level = 'Efficient: Best time to do laundry'
    elif(mybasket.level == 4):
        level = 'Reminder: Time to do laundry'
    elif(mybasket.level == 5):
        level = 'Basket is open'
    #time is float, change type to int
    time =  round(mybasket.time)
    #fomular to change cycle of lanndry to water user will use
    cycle = mybasket.cycle * 50
    #cycle will not show up when it is int type
    if(cycle == 0):
        cycle = '0'
    

    #render to direct to html page and the variable connection
    return render_template('index.html', amount=amount, time=time, cycle=cycle, level=level )


@app.route('/minyu')
def minyu():
    return "Hello minyu"


#this function is to get stable data from sensor, by caculating the average data in 5 seconds
def getstable():
    while True:
        list = []
        list.append(55 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(55 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(55 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(55 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(55 - int(sensor.distance * 100))

        if len(list) == 5:
            medvalue = np.average(list)
            return medvalue
        break


class Basket:
    amount = 0
    level = 0  
    cycle = 0
    time_start = 0
    time_end = 0
    time = 0

    #cost 5 seconds
    def update_amount(self):
        self.amount = getstable()

    def show_amount(self):
        print(self.amount)

    #also called update_level
    def check_amount(self):
        if self.check_empty():
            self.level = 0
            self.time = 0
            print('it is level 0')
        elif self.amount <= 15 and self.amount >= 5:
            self.level = 1
            print('it is level 1')
        elif 15 < self.amount <= 35:
            self.level = 2
            print('it is level 2')
        elif self.amount > 35 and self.amount <= 40:
            self.level = 3
            print('it is level 3')
        elif self.amount > 40:
            self.level = 4
            print('it is level 4')
        elif self.amount < -5:
            self.level = 5
            print('Open dectected')
        return self.level

    #check whether user did laundry
    def check_laundry(self):
        if (self.amount == 0 and self.level != 0):
            self.cycle = self.cycle + 1
            self.time_end = time.time()
            print('Just done the laundry')                                            

    def check_empty(self):
        if(self.amount < 5 and self.amount > -5):
            return True
        else: return False

    #check whether user add something into the basket
    def check_add(self):
        if (self.level == 0 and self.check_empty()):
            self.time_start = time.time()

    #update the time they use 
    def check_time(self):
        if(self.time_start != 0):
            self.time = time.time() - self.time_start
            if (self.time >= 30):
                print("Long time no laundry")
            if (self.time_end != 0):
                self.time = self.time_end - self.time_start
                self.time_end = 0
                self.time_start = 0
    
                
        

#generate object
mybasket = Basket()
'''
mybasket = Basket()
#while True:
mybasket.update_amount()
mybasket.show_amount()
            # time.sleep(5)
mybasket.check_laundry()
mybasket.check_add()
mybasket.check_amount()'''




