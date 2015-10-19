GIFTS = {1: ("first", "a Partridge in a Pear Tree.\n"),
         2: ("second", "two Turtle Doves"),
         3: ("third", "three French Hens"),
         4: ("fourth", "four Calling Birds"),
         5: ("fifth", "five Gold Rings"),
         6: ("sixth", "six Geese-a-Laying"),
         7: ("seventh", "seven Swans-a-Swimming"),
         8: ("eighth", "eight Maids-a-Milking"),
         9: ("ninth", "nine Ladies Dancing"),
         10: ("tenth", "ten Lords-a-Leaping"),
         11: ("eleventh", "eleven Pipers Piping"),
         12: ("twelfth", "twelve Drummers Drumming")}
PREFACE = "On the {} day of Christmas my true love gave to me, "

def verse(number):
    if number == 1:
        return PREFACE.format(GIFTS[number][0]) + GIFTS[number][1]
    else:
        return PREFACE.format(GIFTS[number][0]) + "{}, and {}".format(
            ", ".join(GIFTS[n][1] for n in range(number, 1, -1)),
            GIFTS[1][1]
            )

def verses(minimum, maximum):
    return "\n".join(verse(n) for n in range(minimum, maximum+1)) + "\n"

def sing():
    return verses(1, 12)
