# adds folder to sys.path, can save custom modules in different folder now
import sys 

if 'customModules' not in sys.path:
    sys.path.append('customModules')


# import random -> 1st option

import random as r # 2nd option

# from random import randrange -> 3rd option (no need to dot notation)

# from random import randrange, randint -> multiple imports

from customModules.customModule7 import isPrime # custom module (camelCase)


print(f"random: {r.randrange(1,10)}")

answer = isPrime(int(input("Enter num for prime check: ")))
print(f"Prime: {answer}")