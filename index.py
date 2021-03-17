import random

def madlib01():
    name1 = input("Enter a silly name: ")
    profession1 = input("Enter an unrealistic profession: ")
    country1 = input("Enter a country: ")
    name2 = input("Enter another silly name: ")
    color1 = input("Enter a color: ")
    adjective1 = input("Enter an adjective: ")
    adverb1 = input("Enter an adverb: ")
    name3 = input("Enter a third silly name: ")
    name4 = input("Enter a fourth silly name: ")
    facial1 = input("Enter a facial feature: ")
    city1 = input("Enter a US city: ")
    name5 = input("Last silly name, we promise: ")
    verb1 = input("Enter an action or verb: ")
    noun1 = input("Enter a noun: ")
    actor1 = input("Enter an older action actor: ")
    noun2 = input("Enter a noun: ")

    print("Meet our hero, " + name1 + ", a super-intelligent " + profession1 + ". A")
    print("run-in with the " + country1 + " military leads him to create his alter-ego")
    print(name2 + ", a " + color1 + " " + adjective1 + " giant capable of great")
    print("destruction. He " + adverb1 + " battles the military with his girlfriend")
    print(name3 + ". Eventually it is discovered that our hero's long-time")
    print("colleague " + name4 + ", distinguished by his " + facial1 + ", is trying to")
    print("turn " + name2 + " into a weapon, leading to a climactic (if pointless)")
    print("battle in downtown " + city1 + " with an evil version of the")
    print("same giant alter-ego called " + name5 + ". Eventually the enemy is")
    print("subdued by " + verb1 + "ing him with a " + noun1 + ". In the final reel,")
    print(actor1 + " appears to propose joining him in a")
    print(noun2 + ".")

def madlib02():
    color = input("Enter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")

    print("Roses are", color)
    print(pluralNoun + " are blue")
    print("I love", celebrity)

# mylibs = [madlib01, madlib02]
# random.choice(mylibs)()

madlib01()