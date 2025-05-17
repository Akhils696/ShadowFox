Australia=["Syndey","MMelbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Banglore","Chennai","Delhi"]
city1=input("Enter a city")
city2=input("Enter a city")
if city1 in Australia:
    if city2 in Australia:
        print("Both cities are in Australia")
    else:
        print("No cities are in different countries")
        
if city1 in Australia:
    if city2 in Australia:
        print("Both cities are in Australia")
    else:
        print("No cities are in different countries")
        
if city1 in India:
    if city2 in India:
        print("Both cities are in India")
    else:
        print("No cities are in different countries")
           