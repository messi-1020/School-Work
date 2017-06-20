# Python Code for Lab 03 Problem 2

room_length = float(input("Enter room length:"))
room_width = float(input("Enter room width:"))
room_height = float(input("Enter room height:"))
room_light = input("Does the room get a lot of sunlight?[y/n]")

room_volume = room_length * room_width * room_height
btu = room_volume * 3.5

if room_light == 'yes' or room_light =='y':
    btu_needed = btu + (btu * .20)
    print("BTU needed for the air conditioner:",btu_needed)

elif room_light == 'no' or room_light == 'n':
    print("BTU needed for the air conditioner:",btu)
