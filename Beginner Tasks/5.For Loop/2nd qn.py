count=0
Target=100
while Target>0:
    count+=10
    Target-=10
    opt1=input("Are u Tired: ")
    if opt1.lower() == "y" or opt1.lower() == "yes":
        opt2 = input("Do you want to skip the remaining sets? :")
        if opt2.lower() == "y" or opt2.lower() == "yes":
            print(f"You completed a total of {count} jumping jacks.")
            break
        elif opt2.lower() == "n" or opt2.lower() == "no":
            print(f"{Target} jumping jacks are remaining")
            continue
    elif opt1.lower() == "n" or opt1.lower() == "no":
        if Target == 0:
            print("Congratulations! You completed the workout.")
            break
        print(f"{Target} jumping jacks are remaining")
        continue
