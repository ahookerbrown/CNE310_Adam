# This is my last submitted assignment for CNE330
# Lecture Activity Week 2: Mad Lib
# By Adam Hooker-Brown

# A Mad Lib is a fun, interactive word game where players fill in blanks with specific types of words
# (like nouns, verbs, adjectives, etc.) to create a humorous or surprising story.
# The structure of the story is pre-written, but key parts are left blank for the player to fill in
# without knowing the full context. Once all the blanks are filled, the story is revealed,
# often resulting in funny or unexpected outcomes.

# How it works:
# 1. The Setup: A short story is written with blanks where key words should be
#    (e.g., the name of a person, a place, or an action).
# 2. Prompting for Words: The player is asked to provide words to fill in the blanks without knowing the full story.
#    For example:
#       - "Give me a noun."
#       - "Give me an adjective."
#       - "Give me a verb."
# 3. Creating the Story: Once all the words are filled in, they are inserted into the story's template,
#    creating a unique and often humorous final story.

# Example:
# Story Template: One day, a {adjective} {noun} decided to {verb} to the {place}.
# User Input:
#     - Adjective: "happy"
#     - Noun: "dog"
#     - Verb: "run"
#     - Place: "park"
# Final Story: One day, a happy dog decided to run to the park.

# Assignment:
# Create a Python program that asks the user for various inputs and generates a fun Mad Lib story using
# input(), print(), and f-strings.

# Deliverables:
# 1. Pick a Mad Lib from https://www.thewordfinder.com/wordlibs/.
# 2. Use the input() function to gather words from the user in the console and save them to variables.
# 3. Create a template using your chosen Mad Lib and generate a fun story using f-strings to print the final result.

# Wedding Vows
# https://www.thewordfinder.com/wordlibs/story-21483/

movie_character=input("Enter movie character name: \n")
tv_character=input("Enter tv character name: \n")
plural_direction=input("Enter plural direction: \n")
body_part=input("Enter body part: \n")
body_organ=input("Enter body organ: \n")
noun=input("Enter noun: \n")
shape=input("Enter shape: \n")
time=input("Enter amount of time: \n")
adjective=input("Enter adjective: \n")
verb=input("Enter verb: \n")
verb2=input("Enter another verb: \n")

print(f"I, {movie_character}, choose you, {tv_character}, to be my spouse for life. \nTogether, we'll face the ups and {plural_direction}, always by each other's side. \nI offer you my {body_part} and {body_organ} as a safe haven filled with love and {noun}. \nI promise to stay faithful and devoted to you. \nLike this never-ending {shape}, my love for you will endure {time}. \nJust as this ring is made of {adjective} material, my commitment to you will never {verb}. \nWith this ring, I {verb2} you.")