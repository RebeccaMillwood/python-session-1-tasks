# Question 1:
# input True or False

moths_in_house = True

if moths_in_house:
    (print("Get the moths!"))

else:
    (print("No threats detected"))    

# Question 2:
# change True or False combos for different outputs

moths_in_house = True
mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths")

elif not moths_in_house and not mitch_is_home:  
    print("No threats detected") 

elif moths_in_house and not mitch_is_home:
    print("Meooooooooooow! Hisssss!")

elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch")        

# Question 3:
# Change light colour to Red/Green/Amber, and change car detected True/False combos
# for different outputs

light_colour = "Green"
car_detected = True

if light_colour == "Red" and not car_detected:
    print("Do nothing")

elif light_colour == "Red" and car_detected:
    print("Flash!")

elif light_colour == "Green" and not car_detected:
    print("Do nothing")

elif light_colour == "Green" and car_detected:
    print("Do nothing")

elif light_colour == "Amber" and not car_detected:
    print("Do nothing")

elif light_colour == "Amber" and car_detected:
    print("Do nothing")

# Question 4:

height = int (input ("Are you tall enough to ride the rollercoaster? What is your height in cms? "))

height >= 120

if height >= 120:
    print("Hop on!")

else:
    print("Sorry, not today :(")
