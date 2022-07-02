# Creates a string that says "Subscribe to _______ "
#youtuber = "Cosmo" # some string variable

# Madlib 1
#print("Subscribe to " + youtuber)

# Madlib 2 (formats the variable youtuber into the string using .format)

#print("Subscribe to {}".format(youtuber))

# Madlib 3
#print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("verb 2: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)