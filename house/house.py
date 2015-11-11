LINES = ["",
         " the malt\nthat lay in",
         " the rat\nthat ate",
         " the cat\nthat killed",
         " the dog\nthat worried",
         " the cow with the crumpled horn\nthat tossed",
         " the maiden all forlorn\nthat milked",
         " the man all tattered and torn\nthat kissed",
         " the priest all shaven and shorn\nthat married",
         " the rooster that crowed in the morn\nthat woke",
         " the farmer sowing his corn\nthat kept",
         " the horse and the hound and the horn\nthat belonged to"]

FRAME = "This is{0} the house that Jack built."

def verse(number):
    return FRAME.format(''.join(LINES[number::-1]))

def rhyme():
    return '\n\n'.join(verse(n) for n in range(12))
