# Challenge 4

option=input("Do you need to know the speed you need to travel at to arrive at your destination in the required amount of time OR know the distance travelled currently? Enter `Speed` OR `Distance`: ")
if option == "Speed"or"speed"or"SPEED":
    distance = int(input("How far, in miles, do you need to travel? Enter it here: "))
    time = int(input("How long do you have to get there, in minutes? Enter it here: "))
    conversion=0.0166667*time
    speed=distance/conversion
    print("You'll need to do",speed,"mph!")
elif option == "Distance"or"distance"or"DISTANCE":
    currentSpeed = int(input("What speed are you currently travelling at? Enter it here: "))
    currentDriveTime = int(input("How long have you been driving for, in minutes? Enter it here: "))
    conversion=0.0166667*currentDriveTime
    distance=currentSpeed*currentDriveTime
    print("You've driven",distance,"miles!")
else:
    print("Incorrect input, program ending!")
