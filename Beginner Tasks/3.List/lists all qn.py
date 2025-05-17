justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

#1
print("Number of members of Justice League =", len(justice_league))

#2
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

#3
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman is now the leader:", justice_league)

#4
# Separate Aquaman and Flash by inserting Green Lantern between them
justice_league.remove("Green Lantern")
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash + 1, "Green Lantern")
print("After separating Aquaman and Flash with Green Lantern:", justice_league)

#5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

#6
justice_league.sort()
print("Justice League sorted alphabetically:", justice_league)
print("New leader is:", justice_league[0])
