### Question 1
# You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft, if it
# is less than that tell the pilot to land the plane, or it is more than that but less than 5000ft ask the
# pilot to "come down to 1000ft", else if it is more than 5000ft ask the pilot to "go around and try
# later"




altitude = int(input("Enter the Altitude: ")) # int() converts string input to a integer

if altitude <= 1000:
    print("Its Safe to land Now")                           # if altitude is less than equals to 1000ft it will execute if part
elif altitude <= 4999:
    print("Bring down the altitude to 1000ft")              # if altitude is less than equals to 4999ft it will execute elif part
else:
    print("go around and try Later")                        # if altitude is more then 5000ft it will execute else part


#### END OF CODE ####