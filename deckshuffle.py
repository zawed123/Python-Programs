# https://www.facebook.com/tanishka.gupta.52090/posts/687845045495680
# Subscribed by Tanishka Gupta

import itertools, random


deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))


random.shuffle(deck)


print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
