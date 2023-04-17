# Coffee Shop Barista
# ___________________________

import datetime
import pytz
import pywhatkit
from myNum import Number
TelNumber = (Number)

date_today = datetime.datetime.now()
date_today

date_today.day
date_today.hour

# msg = ("Write Your MSG To Me :")
# time = ("Set A Send Time :")

app_lang = ["HTML", "CSS", "Python", "javaScript", "SASS"]
owner = ("Mulham Shaker Web / Applications Developer")
end = ("This Simply Robot Was Made By " + owner + " With " +
       app_lang[2] + " Programming Language \nI Hope That You Enjoyed Thank You ..\n ")

print("Welcome To Mulham coffee shop \nToday Date Time Is : " + str(date_today))

name = input("What is your name :")

if name == "" or name == "" or name == "":
    status = input("Are U Rich ?")
    if status == "no":
        print("Get Out Of Here")
        exit()
    elif status == "yes":
        print("You Are Welcome\n")
if name == "" or name == "":
    status = input("And Your Last Name Is ? \n")
    if status == "" or status == "" or status == "" or status == "":
        print("My Shop Is Free\n")
        print(end )
        exit()
if name == "mulham" or name == "molham":
    status = input("What Is Your LastName : ?")
    if status == "shaker":
        print("I'am The Coffee Shop Owner , I Don't Pay , But You Are Not ")
        exit()
else:
    print("Nice name " + name)


menu = ("coffee , latte , water , espresso")

print(name + " what you want to drink , \n" + menu)


order = input("")

price = 0

if order == "coffee":
    price = 2
elif order == "latte":
    price = 4
elif order == "espresso":
    price = 3
elif order == "water":
    print("Go To the Sea To Drink Water\n")
    print(end )
    exit()

print("How Many " + order + " you want")

orderNumber = input()

total = price * int(orderNumber)


print("cool, " + name + " your total is " + str(total) +
      " and your " + orderNumber + " " + order + " will come when i say so \n")

print(end)
# pywhatkit.sendwhatmsg(TelNumber,msg,int(time))