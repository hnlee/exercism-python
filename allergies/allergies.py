class Allergies(object):
    def __init__(self, score):
        ALLERGENS = {0: 'eggs',
                     1: 'peanuts',
                     2: 'shellfish',
                     3: 'strawberries',
                     4: 'tomatoes',
                     5: 'chocolate',
                     6: 'pollen',
                     7: 'cats'}
        results = bin(score)[:1:-1]
        self.lst = list(ALLERGENS[i] for i, j in enumerate(results)
                         if j == '1')
    def is_allergic_to(self, allergen):
        return allergen in self.lst


            
