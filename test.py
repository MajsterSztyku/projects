text = "python pandas exercises are designed to challenge your logical muscle and to help internalize data manipulation with python’s favorite package for data analysis."
words = text.split()

print(len(words))

import pandas as pd

df = pd.DataFrame({'Lyrics': ['This is some life some collection of words',
                              'Lyrics abound lyrics here there eveywhere',
                              'Come fly come fly away']})
from collections import Counter
input =  ['a', 'a', 'b', 'b', 'b']
c = Counter(input )

print( c.items() )
#hello