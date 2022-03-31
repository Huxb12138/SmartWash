# SmartWash
> A smart laundry soltuion

This project is a smart laundry basket that is designed to help maintain regular laundry habits and to also make the user more aware of their laundry water and energy consumption. The project is split into three hardware components:
1.  Ultrasonic Distance Sensor: calculate the amount of clothes in the basket and updates the information
2.  Respeberry Pi: as the sever and back-end of the web page.
3.  Display screen

## Features

The core software is working on sever (back-end) `app.py` based on python:
+ `update_amount`: caculate current amount of clothes and update to object
+ `check_amount`: check current amount of clothes and branch to different levels
+ `check_laundry`: check whether user has done the laundry and update the `cycle` and `start_time
+ `check_add`: check if user added some clothes in the basket and set time end
+ `check_time`: caculate time after adding clothes

And other part is front page based on HTML and CSS:
+ Amount of clothes: show percentage of clothes in the basket
+ Comsuption of water: show liters of water users have used in month
+ Timer: show time from back-end
+ Advise: show different context according to levels


## Frame
Python Flask framework to power the back-end


## Repository structure
This respository hosts the code for server (website).
+ `app.py`: start web server when invoked
+ **/template/**: `index.html` used as front-end
 + **/static/**: the `images` used by the website

  


## Installation - local development
You can run the sever by:
`flask run`
And view the website locally at `http://127.0.0.1:8080/`
This creates the flask application locally
