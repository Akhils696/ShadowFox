import random


die_outcomes=[]
for _ in range(0,20):
    i=random.randint(1,6)
    die_outcomes.append(i)
print("Outcomes:",die_outcomes)
print("Number of Times rolled a 6:",die_outcomes.count(6))
print("Number of Times rolled a 1:",die_outcomes.count(1))
count=0
for i in range(len(die_outcomes)):
    if die_outcomes[i]==6 and die_outcomes[i-1]==die_outcomes[i]:
        count+=1
        continue
print("Number of Time rolled two 6 in a row:",count)