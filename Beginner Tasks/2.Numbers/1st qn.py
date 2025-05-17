import math
def area_pond(radius):
    pi=math.pi
    area=pi*(radius**2)
    return area 
result=int(area_pond(84))
print("The Area is ", result)
def water_pond(result):
    return 1.4*result
print("The amount of water in the pond ", water_pond(result))
    

    


    
    