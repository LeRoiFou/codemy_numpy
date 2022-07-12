"""
Cours : 
Lien : https://www.youtube.com/watch?v=eQAuGKayM80

Trie des composants d'un array avec l'instruction sort()

Éditeur : Laurent Reynaud
Date : 12-07-2022
"""

import numpy as np

# Numerical
np1 = np.array([6,7,9,0,2,1])
print(np.sort(np1))

# Alphabetical
np2 = np.array(["John", "Tina", "Aaron", "Zed"])
print(np.sort(np2))

# Booleans
np3 = np.array([True, False, False, True])
print(np.sort(np3))

# Return a copy not change the original
print(np1)

# 2-d
np4 = np.array([[6,7,1,9],[8,3,5,0]])
print(np.sort(np4))
