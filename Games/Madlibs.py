# string concatenation 
# suppose we want to create a string that says "subscribe to ___ "

# text = "subscribe to:"
# youtuber = " Hunter Nghiem"

# CTR + K + C = Comment out
# CTR + K + U = Uncomment 
# print (text + youtuber)
# print ("subcribe to {}".format(youtuber))
# print(f"{text} {youtuber}")
adj = input("Adj: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Per: ")

madlib = f"Computer programming is so {adj}! It makes me so excited because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}" 
print(madlib)