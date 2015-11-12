COLORS = ["red", "green", "ivory", "yellow", "blue"]
NATIONS = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
PETS = ["dog", "snails", "fox", "horse", "zebra"]
BEVERAGES = ["coffee", "tea", "milk", "orange juice", "water"]
CIGARETTES = ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", 
              "Parliaments"]

class House:
    def __init__(self):
        self.color = COLORS
        self.nation = NATIONS
        self.pet = PETS
        self.beverage = BEVERAGES
        self.cigarette = CIGARETTES

rule2 = House()
rule2.nation = [NATIONS.pop(NATIONS.index("Englishman"))]
rule2.color = [COLORS.pop(COLORS.index("red"))]

rule3 = House()
rule3.nation = [NATIONS.pop(NATIONS.index("Spaniard"))]
rule3.pets = [PETS.pop(NATIONS.index("dog"))]
rule2.pets = PETS

rule4 = House()
rule4.color = [COLORS.pop(COLORS.index("green"))]
rule4.beverage = [BEVERAGES.pop(BEVERAGES.index("coffee"))]
rule2.beverage = BEVERAGES

rule5 = House()
rule5.nation = [NATIONS.pop(NATIONS.index("Ukrainian"))]
rule5.beverage = [BEVERAGES.pop(BEVERAGES.index("tea"))]
rule2.beverage = BEVERAGES
rule3.beverage = BEVERAGES

rule7 = House()
rule7.cigarette = [CIGARETTES.pop(CIGARETTES.index("Old Gold"))]
rule7.pet = [PETS.pop(PETS.index("snails"))]
rule3.cigarette = CIGARETTES

rule8 = House()
rule8.cigarette = [CIGARETTES.pop(CIGARETTES.index("Kools"))]
rule8.color = [COLORS.pop(COLORS.index("yellow"))]
rule7.color = COLORS
rule

def solution():
