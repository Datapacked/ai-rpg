import art

intro = art.text2art("AI  RPG", font='medium', space=1)

print(intro)

from ai import AI

initial_prompt = """
You, the AI, are now a master of a choice game world universe.
I, the person you are responding to right now, will give you a single letter that represents an action.
You are to give out possible moves that are labelled with letters, use as few letters as necessary.
An example of a letter-action move is "A) insert action here", when I give you the letter "A", you will respond with the next set of possible moves following what happened after the action took place.
"""

text, context = AI(initial_prompt)

with open('context.txt', 'w') as f:
	f.write(str(context))

T2, context = AI("start the game please, make the introduction and start the things", context)

print(text)

print("\n\n\n\n")

print(T2)