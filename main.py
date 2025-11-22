#1-misol
import random

print("Zar:", random.randint(1, 6))


#2-misol
import random

son = random.randint(1000, 9999)
print(son)


#3-misol
import random

lst = ["olma", "banan", "gilos", "uzum", "nok"]
print(random.sample(lst, 2))


#4-misol
import random

son = random.randint(0, 100)
print("Son:", son)

if son % 2 == 0:
    print("Bu juft son.")
else:
    print("Bu toq son.")


#5-misol
import random
import string

satr = ''.join(random.choice(string.ascii_letters) for _ in range(10))
print(satr)

