def speed_calculation(distance,time):
    time_in_secs=time*60
    speed=distance/time
    return speed
speed_calculated=speed_calculation(490,7)
print("The required speed is ",speed_calculated)