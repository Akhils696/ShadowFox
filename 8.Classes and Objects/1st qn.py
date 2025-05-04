class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
        print("---------------------------")

    def is_leader(self):
        if self.name == "Captain America":
            return True
        else:
            return False


Captain_America=Avenger("Captain America", 100, "Male", "Super strength", "Shield")
Iron_Man=Avenger("Iron Man", 48, "Male", "Technology", "Armor")
Black_Widow=Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
Hulk=Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")
Thor=Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
Hawkeye=Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
Avengers=[Captain_America,Iron_Man,Black_Widow,Hulk,Thor,Hawkeye]

for marvel in Avengers:
    marvel.get_info()
    if marvel.is_leader():
        print("Leader")
    print()