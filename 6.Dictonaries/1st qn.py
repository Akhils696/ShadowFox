num_friends = int(input("How many friends' names do you want to enter? "))
friends=[]
for i in range(num_friends):
    name = input(f"Enter name of friend {i+1}: ")
    friends.append((name, len(name)))
for i in friends:
    print(i)