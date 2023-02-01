"""
Jakiel David
1/30/23

"""

# imports first
import random

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

#TAsk 4 Sting List 

list_teams = ["Eagles", "Bengals", "Chiefs", "49ers",] 

list_offense = ["caught","ran","threw"]

list_players = ["Hurts", "Burrow", "Mahomes" , "Deebo"]

list_outcomes = ["win", "lose", "draw"]

list_fb = ["football","pig skin", "it", "ball"]

#String List 1

team_outcome = list(zip(list_teams,list_outcomes))
print("Team_outcome: ", team_outcome)
print()
player_offense = set(zip(list_players,list_offense,list_fb))
print("Player-Offense: ", player_offense)
print()
list_lengths = [len(list_teams), len(list_offense), len(list_players), len(list_outcomes)]
print("List lengths: ", list_lengths)

#String List 2

print(random.choice(list_teams))
print()
print(random.choice(list_offense))
print()
print(random.choice(list_players))
print()
print(random.choice(list_outcomes))
print()
print(random.choice(list_fb))
print()


sentence1 = (f" Wooow {random.choice(list_players)} {random.choice(list_offense)} the {random.choice(list_fb)},touchdown!!!")
print()
sentence2 = (f" And just like that {random.choice(list_teams)} {random.choice(list_outcomes)} a close one")       
print()
sentence3 = (f" {random.choice(list_teams)} {random.choice(list_outcomes)} a close one")
print()

for team, outcome in team_outcome:
    print(f"{team} had a {outcome} in their game.")

def generate_sentence():
    player = random.choice(list_players)
    offense = random.choice(list_offense)
    
    sentence = f"{player} almost {offense} the ball."
    return sentence

print(generate_sentence())

#String List 3
with open("text_woodchuck.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()
    unique_words = set(list_words)
    word_ct = len(list_words)
    unique_word_ct = len(unique_words)

print("Woodchuck.txt")
print()
print(text)
print()
print("List of Woodchuck")
print(list_words)
print()
print("Unique words in text")
print(unique_words)
print()
asc = sorted(list_words)
print(asc)
desc = sorted(list_words, reverse = True)
print(desc)
print()
len(text)




