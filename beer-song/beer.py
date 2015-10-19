def verse(num):
    lyrics = "{0} of beer on the wall, {1} of beer.\n{2}, {3} of beer on the wall.\n"
    if num > 2:
        return lyrics.format(str(num) + " bottles",
                             str(num) + " bottles",
                             "Take one down and pass it around",
                             str(num - 1) + " bottles")
    if num == 2:
        return lyrics.format(str(num) + " bottles",
                             str(num) + " bottles",
                             "Take one down and pass it around",
                             str(num - 1) + " bottle")
    elif num == 1:
        return lyrics.format(str(num) + " bottle",
                             str(num) + " bottle",
                             "Take it down and pass it around",
                             "no more bottles")
    else:
        return lyrics.format("No more bottles",
                             "no more bottles",
                             "Go to the store and buy some more",
                             "99 bottles")

def song(start, stop=0):
    return "\n".join(list(verse(n) 
                          for n in range(start, stop-1, -1))) + "\n"

