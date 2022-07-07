"""
Cours : Iterating Through Numpy Arrays
Lien : https://www.youtube.com/watch?v=oIyfZTYQbtk

Recours aux boucles

Éditeur : Laurent Reynaud
Date : 07-07-22
"""

import numpy as np

# 1-d Array
# np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# [print(x) for x in np1]
    
# 2-d Array
# np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# [print(x) for x in np2]
# [print(y) for x in np2 for y in x]

# 3-d Array
np3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# [print(z) for x in np3 for y in x for z in y]

# Use np.nditer()
[print(x) for x in np.nditer(np3)]
