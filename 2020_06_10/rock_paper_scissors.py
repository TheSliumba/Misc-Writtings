"""
Okay, so here's a little app that asks the user to choose between rock
paper and scissors, and the rest is pretty much apparent I hope.
"""
from random import randint

def user_selection():
    user_selected = input("Make the choice; [P]aper, [R]ock, or [S]cissors\n")
    print(f"You have selected {user_selected}")
    return user_selected.upper()


def machine_selection():
    machine_selected = randint(0, 2)
    choices = "PRS"
    selection = choices[machine_selected]
    print(f"The machine has selected {selection}")
    return selection


def determine(user, machine):
    if user == "P" and machine == "R":
        return "User wins this round"
    if user == "P" and machine == "S":
        return "Machine wins this round"
    if user == "R" and machine == "S":
        return "User wins this round"
    if user == "R" and machine == "P":
        return "Machine wins this round"
    if user == "S" and machine == "R":
        return "Machine wins this round"
    if user == "S" and machine == "P":
        return "User wins this round"
    if user == machine:
        return "Draw"


score = {"user": 0, "machine": 0}
while abs(score['user'] - score['machine']) != 2:
    user = user_selection()
    machine = machine_selection()
    tally_nfo = determine(user, machine)
    print(tally_nfo)
    if tally_nfo.split()[0] == "User":
        score["user"] += 1
    if tally_nfo.split()[0] == "Machine":
        score["machine"] += 1
    print(score)
winner = max(score)
print(f"The winner is {winner}, congrats!")
