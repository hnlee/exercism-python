EQUAL = "List 1 is equal to list 2"
SUBLIST = "List 1 is a sublist of list 2"
SUPERLIST = "List 1 is a superlist of list 2"
UNEQUAL = "List 1 is not a superlist of, sublist of, or equal to list 2"

def check_lists(list1, list2):
    if list1 == list2:
        return EQUAL
    if len(list1) < len(list2):
        if sum(list2[i:i+len(list1)] == list1 
               for i in range(len(list2)-len(list1)+1)) > 0:
            return SUBLIST
    if len(list1) > len(list2):
        if sum(list1[i:i+len(list2)] == list2
               for i in range(len(list1)-len(list2)+1)) > 0:
            return SUPERLIST
    return UNEQUAL
