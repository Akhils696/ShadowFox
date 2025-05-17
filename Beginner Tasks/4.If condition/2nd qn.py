Australia=["Syndey","MMelbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Banglore","Chennai","Delhi"]
city=input("Enter a city")
if city in Australia:
    print(city ,"is in Australia")
elif city in UAE:
     print(city ,"is in UAE")
elif city in India:
     print(city ,"is in India")
else:
     print("Enter the correct city name")
    