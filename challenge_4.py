# Challenge 4

option = int(input("Do you need to know the speed you need to travel at to arrive at your destination in the required amount of time OR know the distance travelled currently? Enter 1 for Speed OR 2 for Distance: "))
if option == 1:
    distance = int(input("How far, in miles, do you need to travel? Enter it here: "))
    time = int(input("How long do you have to get there, in minutes? Enter it here: "))
    conversion=0.0166667*time
    speed=distance/conversion
    print("You'll need to do",speed,"mph!")
elif option == 2:
    currentSpeed = int(input("What speed are you currently travelling at? Enter it here, in mph: "))
    currentDriveTime = int(input("How long have you been driving for, in minutes? Enter it here: "))
    conversion=0.0166667*currentDriveTime
    distance=currentSpeed*currentDriveTime
    print("You've driven",distance,"miles!")
else:
    print("Incorrect input, program ending!")
