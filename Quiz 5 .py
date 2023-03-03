#Sarah Stephenson
#Problem 1
def tire_presure(p):
    if p < 28:
        print("Tire preasure is low")
    else:
        print("none")

tire_presure(29)
tire_presure(25)

# Problem 2
def thermostat(temp):
    if temp <= 52:
        print("The heater is on")
    elif 52 < temp < 71:
        print("Heater and AC are off")
    else:
        print(" The heater is off")

thermostat(80)
thermostat(40)
thermostat(60)

# problem 3
def fruit(n):
    if n =="Banana":
        print("Banana it is!")
    elif n == "Cherry":
        print("I Cherish you!")
    else:
        print("You are one in a Melon")

fruit("Banana")
fruit("Cherry")
fruit("melon")
