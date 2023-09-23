import itertools
import math
from itertools import combinations_with_replacement
from collections import Counter

def picking_cards(L: list)->int:
    if len(L)<=max(L):
        return 0
    freq = Counter(L)
    #print(freq)
    produit = 1
    for key in freq:
        produit*=math.factorial(freq[key])
   # print(produit)
    set_=set(L)
    return math.factorial(len(set_))*produit
print("############")
print(picking_cards([0,0,0]))
print(picking_cards([0,1,0]))
print(picking_cards([0,3,3]))

print("###############")
t = "AB"

# iterator = itertools.cycle(t)

# for i in range(6):

#     print(next(iterator))
print(list(combinations_with_replacement("ABC",2)))
print("###############")
p = "ABC"
print(list(itertools.combinations(p,3)))