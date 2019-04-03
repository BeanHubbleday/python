# Challenge 3

option = input("Do you want to find the area of a rectangle or the volume of a cuboid? Enter `Volume` OR `Area` Here: ")
if option == "Area"or"area"or"AREA":
    width=int(input("Enter the width of your rectangle: "))
    length=int(input("Enter the length of your rectangle: "))
    area=width*length
    print("The area of your rectangle is:",area)
elif option == "Volume"or"volume"or"VOLUME":
    width=int(input("Enter the width of your rectangle: "))
    length=int(input("Enter the length of your rectangle: "))
    height=int(input("Enter the height of your rectangle: "))
    volume=width*length*height
    print("The volume of your cuboid is:",volume)
else:
    print("Incorrect input, try again!")
