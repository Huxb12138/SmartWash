import random
import time
import numpy as np
from gpiozero import DistanceSensor
from flask import *
sensor = DistanceSensor(echo=17, trigger=4)
app = Flask(__name__)

@app.route('/')
def index():
    
    
    
    # while True:
    mybasket.update_amount()
    amount = mybasket.amount
    # time.sleep(5)
    mybasket.check_laundry()
    mybasket.check_add()
    mybasket.check_amount()
    mybasket.check_time()
    time =  round(mybasket.time)
    


    return render_template('index.html', amount=amount, time=time )


@app.route('/minyu')
def minyu():
    return "Hello minyu"



def getstable():
    while True:
        list = []
        list.append(100 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(100 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(100 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(100 - int(sensor.distance * 100))
        time.sleep(1)
        list.append(100 - int(sensor.distance * 100))

        if len(list) == 5:
            medvalue = np.median(list)
            return medvalue
        break


class Basket:
    amount = 0
    level = 0  # 0:a=0 1:a<=30  2:30<a<=70 3:70<a<=80 4:a>80
    cycle = 0
    time_start = 0
    time_end = 0
    time = 0

    def update_amount(self):
        self.amount = getstable()

    def show_amount(self):
        print(self.amount)

    def check_amount(self):
        if self.amount == 0:
            self.level = 0
            self.time = 0
            print('it is level 0')
        elif self.amount <= 30:
            self.level = 1
            print('it is level 1')
        elif 30 < self.amount <= 70:
            self.level = 2
            print('it is level 2')
        elif self.amount > 70 and self.amount <= 80:
            self.level = 3
            print('it is level 3')
        elif self.amount > 80:
            self.level = 4
            print('it is level 4')
        return self.level

    def check_laundry(self):
        if (self.amount == 0 and self.level != 0):
            self.cycle = self.cycle + 1
            self.time_end = time.time()
            print('Just done the laundry')                                            


    def check_add(self):
        if (self.level == 0 and self.amount != 0):
            self.time_start = time.time()

    def check_time(self):
        if(self.time_start != 0):
            self.time = time.time() - self.time_start
            if (self.time >= 30):
                print("Long time no laundry")
            if (self.time_end != 0):
                self.time = self.time_end - self.time_start
                self.time_end = 0
                self.time_start = 0
    
                
        


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




